"""Publish one locally prepared article. Default: isolated preview only.

python scripts/publish_daily_blog.py --date 2026-10-19
python scripts/publish_daily_blog.py --commit --push

Drafts and the release plan live under ignored docs/private-drafts/.
"""
import argparse
from datetime import datetime, timedelta, timezone, date
from pathlib import Path
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit

PROJECT = Path(__file__).resolve().parents[1]
PRIVATE = PROJECT / 'docs/private-drafts'
CHINA = timezone(timedelta(hours=8))
ORIGIN = 'https://github.com/chuichuifeng-carbon/automotive-carbon-fiber-guide.git'


def run(*args, env=None):
    execution_env = (env or os.environ).copy()
    if str(args[0]) == 'git':
        execution_env['GIT_TERMINAL_PROMPT'] = '0'
        execution_env['GCM_INTERACTIVE'] = 'never'
    result = subprocess.run(list(map(str, args)), cwd=PROJECT, env=execution_env,
                            text=True, encoding='utf-8', errors='replace',
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            timeout=180)
    if result.returncode:
        raise RuntimeError(f'{args[0]} failed:\n{result.stdout[-5000:]}')
    return result.stdout.strip()


def inspect(entry):
    source = (PRIVATE / entry['file']).resolve()
    if not source.is_relative_to(PRIVATE.resolve()) or not source.is_file():
        raise RuntimeError('Missing draft or draft path outside private directory')
    slug = entry['slug']
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise RuntimeError('Invalid article slug')
    text = source.read_text(encoding='utf-8')
    if not text.startswith('---\n') or text.count('\n---\n') < 1:
        raise RuntimeError('Invalid front matter')
    front, body = text[4:].split('\n---\n', 1)
    if not re.search(r'^date: ' + re.escape(entry['date']) + r'T20:00:00\+08:00$', front, re.M):
        raise RuntimeError('Draft must use its scheduled date at 20:00 China time')
    if not re.search(r'^draft: false$', front, re.M):
        raise RuntimeError('Release draft flag must be false')
    if re.search(r'^# ', body, re.M):
        raise RuntimeError('Body must not duplicate the theme H1')
    targets = {urlsplit(url)._replace(query='', fragment='').geturl()
               for url in re.findall(r'\]\((https://ccfrp\.com/[^)\s]+)\)', body)}
    if len(targets) < 5:
        raise RuntimeError('At least five distinct main-site pages required in article body')
    topic_data = json.loads((PROJECT / 'data/buyer_topics.json').read_text(encoding='utf-8'))
    if entry['topic'] not in {topic['id'] for topic in topic_data}:
        raise RuntimeError('Unknown guide topic')
    words = len(re.findall(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b", body))
    if words < 1200:
        raise RuntimeError(f'Unexpectedly short prepared article: {words} English words')
    print(f"Checked {entry['date']}: {slug}; {words} English words; {len(targets)} main-site targets.")
    return text


def add_topic(topics, entry):
    for topic in topics:
        if entry['slug'] in topic['guides']:
            if topic['id'] != entry['topic']:
                raise RuntimeError('Article already assigned to a different topic')
            return
    next(topic for topic in topics if topic['id'] == entry['topic'])['guides'].append(entry['slug'])


def find_hugo(explicit):
    candidates = [explicit, shutil.which('hugo'),
                  str(Path(tempfile.gettempdir()) / 'ccf-hugo-check/hugo.exe')]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            if 'v0.168.0' not in run(candidate, 'version'):
                raise RuntimeError('Use the workflow-pinned Hugo 0.168.0 for release checks')
            return candidate
    raise RuntimeError('Hugo 0.168.0 unavailable; provide --hugo PATH')


def build_preview(entries, hugo):
    preview_root = (PROJECT / 'public/release-checks').resolve()
    preview_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='ccf-blog-preview-', dir=preview_root) as tmp:
        workspace = Path(tmp)
        if not workspace.resolve().is_relative_to((PROJECT / 'public').resolve()):
            raise RuntimeError('Preview directory must stay inside the ignored workspace output')
        shutil.copytree(PROJECT / 'content', workspace / 'content')
        shutil.copytree(PROJECT / 'data', workspace / 'data')
        topics = json.loads((workspace / 'data/buyer_topics.json').read_text(encoding='utf-8'))
        for entry in entries:
            text = inspect(entry)
            (workspace / 'content/posts' / (entry['slug'] + '.md')).write_text(text, encoding='utf-8')
            add_topic(topics, entry)
        topics_file = workspace / 'data/buyer_topics.json'
        topics_file.write_text(json.dumps(topics, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        env = os.environ.copy()
        for key, value in [('CONTENTDIR', 'content'), ('DATADIR', 'data'),
                           ('RESOURCEDIR', 'resources'), ('CACHEDIR', 'cache')]:
            env['HUGO_' + key] = str(workspace / value)
        clock = max(entry['date'] for entry in entries) + 'T20:00:00+08:00'
        output = run(hugo, '--gc', '--minify', '--clock', clock,
                     '--destination', workspace / 'public', '--printPathWarnings', env=env)
        print(output)
        print(run(sys.executable, PROJECT / 'scripts/check_site.py', workspace / 'public',
                  '--topics', topics_file, '--content-dir', workspace / 'content'))
        for entry in entries:
            page = workspace / 'public/posts' / entry['slug'] / 'index.html'
            if not page.is_file():
                raise RuntimeError('Prepared article missing from preview output')


def push_one(entry):
    run('git', 'fetch', 'origin', 'main')
    if run('git', 'rev-list', '--count', 'HEAD..origin/main') != '0':
        raise RuntimeError('Remote main has newer commits; resolve without force-pushing')
    outgoing = run('git', 'diff', '--name-only', 'origin/main', 'HEAD', '--', 'content/posts')
    expected = f"content/posts/{entry['slug']}.md"
    if set(outgoing.splitlines()) - {expected}:
        raise RuntimeError('Push would include another article; refusing batch publication')
    run('git', 'push', 'origin', 'HEAD:main')
    print('Pushed the selected article. GitHub Pages deployment is asynchronous; verify its workflow result.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', help='Scheduled date; future dates can only be previewed')
    parser.add_argument('--validate-all', action='store_true', help='Preview the full private batch without publishing')
    parser.add_argument('--commit', action='store_true', help='Commit only the article scheduled for today and its topic entry')
    parser.add_argument('--push', action='store_true', help='Also push that release to origin/main')
    parser.add_argument('--hugo', help='Path to Hugo 0.168.0')
    args = parser.parse_args()
    if args.push and not args.commit:
        raise RuntimeError('--push requires --commit')
    if args.validate_all and (args.commit or args.push):
        raise RuntimeError('Batch preview cannot commit or push')
    plan = json.loads((PRIVATE / 'release-plan.json').read_text(encoding='utf-8'))
    today = datetime.now(CHINA).date().isoformat()
    requested = args.date or today
    date.fromisoformat(requested)
    selected = [item for item in plan if item['date'] == requested]
    if len(selected) != 1 and not args.validate_all:
        raise RuntimeError(f'No single article scheduled for {requested}; nothing published')
    if args.commit and requested != today:
        raise RuntimeError('Only today\'s scheduled article may be committed; use preview for other dates')
    if args.commit and datetime.now(CHINA).hour < 20:
        raise RuntimeError('Publication is scheduled for 20:00 China time; preview is available earlier')
    hugo = find_hugo(args.hugo)
    if args.validate_all:
        build_preview(plan, hugo)
        print('Batch validated in isolation. Repository content and Git index unchanged.')
        return
    entry = selected[0]
    body = inspect(entry)
    target = PROJECT / 'content/posts' / (entry['slug'] + '.md')
    if args.commit:
        if run('git', 'branch', '--show-current') != 'main':
            raise RuntimeError('Release must run on main')
        if run('git', 'remote', 'get-url', 'origin') != ORIGIN:
            raise RuntimeError('Unexpected Git origin')
        if run('git', 'status', '--porcelain', '--untracked-files=normal'):
            raise RuntimeError('Working tree or index has other changes; refusing to mix work into release')
        if target.exists():
            if target.read_text(encoding='utf-8') != body:
                raise RuntimeError('Published target differs from private draft')
            print('Article already exists; no duplicate commit created.')
            if args.push:
                push_one(entry)
            return
        if run('git', 'log', '-1', '--format=%H', '--grep=^Publish blog: ' + today + ' '):
            raise RuntimeError('A blog release for today is already recorded')
        if args.push:
            run('git', 'fetch', 'origin', 'main')
            if run('git', 'rev-list', '--count', 'HEAD..origin/main') != '0':
                raise RuntimeError('Remote main is ahead; no files changed')
            if run('git', 'diff', '--name-only', 'origin/main', 'HEAD', '--', 'content/posts'):
                raise RuntimeError('An earlier article commit is unpushed; resolve it separately')
    build_preview([entry], hugo)
    if not args.commit:
        print('Preview passed. No article copied into repository content; no commit or push performed.')
        return
    topics_file = PROJECT / 'data/buyer_topics.json'
    topics = json.loads(topics_file.read_text(encoding='utf-8'))
    add_topic(topics, entry)
    target.write_text(body, encoding='utf-8')
    topics_file.write_text(json.dumps(topics, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    relative = target.relative_to(PROJECT).as_posix()
    run('git', 'add', '--', relative, 'data/buyer_topics.json')
    staged = set(run('git', 'diff', '--cached', '--name-only').splitlines())
    if staged != {relative, 'data/buyer_topics.json'}:
        raise RuntimeError('Unexpected staged files; nothing committed')
    run('git', 'commit', '-m', f"Publish blog: {today} {entry['slug']}", '--', relative, 'data/buyer_topics.json')
    print('Committed one article and its directory entry: ' + run('git', 'rev-parse', '--short', 'HEAD'))
    if args.push:
        push_one(entry)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('STOP: ' + str(exc), file=sys.stderr)
        sys.exit(1)
