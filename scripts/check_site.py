"""Check a Hugo production output: python scripts/check_site.py PATH_TO_PUBLIC.

Uses only Python's standard library. Does not request external URLs.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys
import xml.etree.ElementTree as ET

BASE = 'https://chuichuifeng-carbon.github.io/automotive-carbon-fiber-guide/'
PREFIX = urlsplit(BASE).path
ROOT = Path(sys.argv[1]).resolve()
errors = []

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.h1 = 0
        self.ids = set()
        self.links = []
        self.canonical = []
        self.descriptions = []
        self.schemas = []
        self.json_script = False
        self.json_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'{self.path}: duplicate HTML id {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'meta' and attrs.get('name') == 'description':
            self.descriptions.append(attrs.get('content', ''))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs.get('href'))
        if tag == 'img' and not attrs.get('alt'):
            errors.append(f'{self.path}: image missing alt text')
        if tag == 'a' and attrs.get('href'):
            self.links.append((attrs['href'], True))
        if tag in ('img', 'script', 'link'):
            value = attrs.get('src') or (attrs.get('href') if tag == 'link' and attrs.get('rel') in ('stylesheet', 'preload stylesheet', 'icon', 'apple-touch-icon', 'mask-icon') else None)
            if value:
                self.links.append((value, False))
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.json_script = True
            self.json_parts = []

    def handle_data(self, data):
        if self.json_script:
            self.json_parts.append(data)

    def handle_endtag(self, tag):
        if tag == 'script' and self.json_script:
            try:
                self.schemas.append(json.loads(''.join(self.json_parts)))
            except ValueError as exc:
                errors.append(f'{self.path}: invalid JSON-LD: {exc}')
            self.json_script = False

pages = {}
for path in ROOT.rglob('*.html'):
    page = Page(path.relative_to(ROOT))
    page.feed(path.read_text(encoding='utf-8'))
    pages[path.resolve()] = page

for path, page in pages.items():
    rel = path.relative_to(ROOT).as_posix()
    # Hugo paginator aliases intentionally have only redirect markup.
    alias = '/page/' in '/' + rel and not page.h1
    if not alias:
        if rel != '404.html' and page.h1 != 1:
            errors.append(f'{rel}: expected one h1, got {page.h1}')
        if len(page.descriptions) != 1 or not page.descriptions[0]:
            errors.append(f'{rel}: missing/duplicate description')
        if len(page.canonical) != 1:
            errors.append(f'{rel}: missing/duplicate canonical')
        else:
            canonical = page.canonical[0]
            if not canonical.startswith(BASE):
                errors.append(f'{rel}: unexpected canonical {canonical}')
        graph = [item for schema in page.schemas for item in schema.get('@graph', [])]
        organization = next((item for item in graph if item.get('@type') == 'Organization'), {})
        if rel != '404.html' and organization.get('url') != 'https://ccfrp.com/':
            errors.append(f'{rel}: CCF organization URL missing or incorrect')
        if rel.startswith('posts/') and rel.count('/') == 2:
            article = next((item for item in graph if item.get('@type') == 'BlogPosting'), {})
            if not article.get('dateModified') or article.get('author', {}).get('@id') != 'https://ccfrp.com/#organization':
                errors.append(f'{rel}: article metadata incomplete')
    for href, check_anchor in page.links:
        parsed = urlsplit(href)
        if parsed.scheme and parsed.scheme not in ('http', 'https'):
            continue
        if parsed.netloc and parsed.netloc != urlsplit(BASE).netloc:
            continue
        target_path = unquote(parsed.path)
        if target_path.startswith(PREFIX):
            target = ROOT / target_path[len(PREFIX):]
        elif target_path.startswith('/'):
            errors.append(f'{rel}: link escapes project prefix: {href}')
            continue
        elif target_path:
            target = path.parent / target_path
        else:
            target = path
        if target.is_dir():
            target /= 'index.html'
        target = target.resolve()
        if not target.is_file():
            errors.append(f'{rel}: missing local target {href}')
        elif check_anchor and parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f'{rel}: missing anchor {href}')

ET.parse(ROOT / 'sitemap.xml')
if len(list((ROOT / 'posts').glob('*/index.html'))) != 14:
    errors.append('Expected all 14 existing guide pages')

# Keep the grouped directory complete as editors maintain the topic data.
topics = json.loads((Path(__file__).resolve().parents[1] / 'data/buyer_topics.json').read_text(encoding='utf-8'))
grouped = [slug for topic in topics for slug in topic['guides']]
existing = {p.parent.name for p in (ROOT / 'posts').glob('*/index.html')}
if len(grouped) != len(set(grouped)) or set(grouped) != existing:
    errors.append('Guide topics must include every published guide exactly once')
directory_links = {urlsplit(href).path for href, _ in pages[(ROOT / 'posts/index.html').resolve()].links}
for slug in grouped:
    if PREFIX + 'posts/' + slug + '/' not in directory_links:
        errors.append(f'Grouped directory missing link to {slug}')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {len(pages)} HTML files; headings, metadata, JSON-LD, local links/assets, anchors and sitemap checked.')
