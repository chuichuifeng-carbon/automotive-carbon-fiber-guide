# 网站美化方案:深色科技感 + 全站配图

## Context(背景)

CHUICHUIFENG Carbon Fiber 的 Hugo 博客站(currently hosted on GitHub Pages)目前内容扎实(5 篇深度 B2B 指南 + 5 个业务页),但存在三个影响品牌形象与 SEO 的问题:

1. **全站零图片** —— 5 篇文章 + 5 个业务页全是纯文字,首页 hero 也是纯文字 + CSS 纹理,缺乏视觉冲击,与"碳纤维高性能"调性不符。
2. **front matter bug** —— `content/` 根目录 5 个页面(about/products/sourcing/oem/contact)的结束分隔符误写为 `------------`(12 连字符),Hugo 只识别 `---`,导致这些页面的 title/description/keywords 全部失效,SEO 归零。
3. **设计未充分释放** —— 已有的 [custom.css](file:///d:/website/github/automotive-carbon-fiber-guide/assets/css/extended/custom.css) 设计系统不错(黑+绿品牌色、卡片、按钮),但首页 hero 偏浅色平淡,文章卡片无封面,业务页无 hero 图,大气感不足。

用户目标:把网站做漂亮、大气,但不能搞崩。已确认方向 = **深色科技感**(黑 hero + 碳纤维纹理 + 绿点缀,内容区保持浅色可读)+ **完整美化**(修 bug + 首页 hero 大图 + 5 篇文章封面 + 5 业务页 hero + 卡片视觉升级)+ **网络真实照片**(免版权图库)。

## 设计原则(保证不搞崩)

- **只加法、不破坏**:不动 `themes/PaperMod/` 任何模板文件(避免主题更新冲突),全部通过 `assets/css/extended/custom.css` 覆盖 + 文章 front matter + 正文 HTML 实现。
- **图片本地化**:所有图片下载到 `static/images/` 用绝对路径引用,不依赖外链 CDN(避免外链失效导致破图)。因用户明确选"网络真实照片",使用 Unsplash/Pexels 免版权(CC0)图库下载。
- **渐进式 CSS**:custom.css 只追加新规则、不删减现有规则,新规则用更高特异性或 `!important` 覆盖冲突点。
- **front matter 修复优先**:先修 bug 再加图,确保构建稳定。

## SEO、GEO 与性能保障措施(硬约束)

本方案对 SEO/GEO 整体是**改善而非损害**:修 front matter bug 让 5 个业务页的 title/description/keywords 重新生效(当前全部失效,是 SEO/GEO 负资产);加配图并带 alt 文本带来图片 SEO 收益;Hugo 静态 HTML 输出对 AI 爬虫天然友好;文章正文、H2/H3、列表、对比表格结构完全保留,这些正是 GEO(LLM 引用)最爱的可引用结构。以下为实施时必须守住的硬约束,防止反向拖累:

### SEO 保障

1. **文字标题不图片化**:所有 h1/h2/h3 保持 HTML 文字,绝不用图片代替标题文字。hero 背景图上的标题必须是 HTML 文本层,不做成图片。
2. **alt 文本语义化**:每张 `<img>` 写描述性、自然含主题词的 alt(如 `alt="碳纤维后扰流板模具特写"`),禁止空 alt 或堆砌关键词。
3. **图片文件名含关键词**:下载时用语义文件名(如 `carbon-fiber-rear-spoiler.jpg`),而非图库随机 ID,搜索引擎与 LLM 都会读 URL。
4. **URL 结构不变**:不改 permalink 与文章 slug,不产生 404 或重定向,现有排名与外链不受冲击。
5. **meta 标签完整**:front matter 修复后确认每页生成的 `<title>` 与 `<meta name="description">` 正确(验证步骤覆盖)。

### GEO 保障(面向 ChatGPT / Perplexity / Google AI Overviews)

1. **内容结构保留**:文章正文、H2/H3 层级、列表、对比表格一律不动 —— 这些可引用结构是 GEO 的核心资产。
2. **纯静态 HTML**:只加 `<img>` 与 CSS,不引入 JS 渲染依赖,AI 爬虫无需执行 JS 即可读全文。
3. **alt 服务语义理解**:alt 文本帮助 AI 理解图片语境,与 SEO 保障第 2 条一致。
4. **事实性文字保留**:指南中的数据、流程、checklist 全部保留,这些是 LLM 提取引用的高价值内容。
5. **(本次不做,记为后续提升)**:schema.org JSON-LD(`Article`/`BreadcrumbList`/`FAQPage`)、FAQ 段落、作者/工厂 E-E-A-T 信号 —— 本次范围外,作为独立的 GEO 提升任务另行规划。

### 性能与 Core Web Vitals 保障

1. **LCP**:hero 大图用压缩后的 WebP/JPG(单张 < 200KB),首图设 `fetchpriority="high"` + `loading="eager"`;图片本地化避免外链握手延迟。
2. **CLS**:所有 `<img>` 设 `width`/`height` 属性,或容器用 `aspect-ratio` 预占位,杜绝加载跳动。
3. **图片压缩**:下载后压缩,优先 WebP 格式(PaperMod cover.html 已支持 webp)。
4. **文字对比度**:深色 hero 上文字对比度达 WCAG AA(≥ 4.5:1),保证可读性与用户体验信号。
5. **hover 仅装饰**:卡片 hover 的 `transform` 不影响布局与 SEO。

## 实施步骤

### Step 1:修复 front matter bug(5 个文件)

修改文件:
- [content/about.md](file:///d:/website/github/automotive-carbon-fiber-guide/content/about.md)
- [content/products.md](file:///d:/website/github/automotive-carbon-fiber-guide/content/products.md)
- [content/sourcing.md](file:///d:/website/github/automotive-carbon-fiber-guide/content/sourcing.md)
- [content/oem.md](file:///d:/website/github/automotive-carbon-fiber-guide/content/oem.md)
- [content/contact.md](file:///d:/website/github/automotive-carbon-fiber-guide/content/contact.md)

改动:把第 8 行 `------------` 改为 `---`,删除第 2 行多余空行。`posts/` 下文章不动(front matter 已正确)。

### Step 2:准备图片资源(下载到本地)

在 `static/images/` 下建子目录:
- `static/images/hero/` — 首页大图
- `static/images/posts/` — 文章封面
- `static/images/pages/` — 业务页 hero

共约 11 张图,全部从 Unsplash/Pexels 找 CC0 授权的真实照片,用 PowerShell `Invoke-WebRequest` 下载到本地。图片清单:

| 用途 | 主题关键词 | 放置路径 |
|---|---|---|
| 首页 hero | 深色碳纤维纹理特写 / 黑色跑车尾翼 | `hero/hero-bg.jpg` |
| 文章:how-to-start...business | 商务谈判/创业办公 | `posts/start-business.jpg` |
| 文章:how-to-choose...supplier | 质检/对比/检查清单 | `posts/choose-supplier.jpg` |
| 文章:wholesale-guide | 仓库/批量货架 | `posts/wholesale.jpg` |
| 文章:oem-odm-complete-guide | 工厂车间/模具 | `posts/oem-odm.jpg` |
| 文章:how-to-find...manufacturer | 制造商/工厂产线 | `posts/find-manufacturer.jpg` |
| 页面:about | 工厂全景/团队 | `pages/about.jpg` |
| 页面:products | 碳纤维配件阵列 | `pages/products.jpg` |
| 页面:sourcing | 供应链/装箱发货 | `pages/sourcing.jpg` |
| 页面:oem | 模具/CAD 设计 | `pages/oem.jpg` |
| 页面:contact | 商务沟通/握手 | `pages/contact.jpg` |

### Step 3:首页深色 Hero 改造

**方式**:纯 CSS 改造 `.profile`(不动 hugo.yaml 的 profileMode 结构,保留两个 CTA 按钮)。

在 [custom.css](file:///d:/website/github/automotive-carbon-fiber-guide/assets/css/extended/custom.css) 的 `HOMEPAGE HERO` 区块追加/覆盖:
- `.profile` 背景改为 `linear-gradient(rgba(10,10,12,0.78), rgba(10,10,12,0.88))`, 上叠 `url("/images/hero/hero-bg.jpg")` 深色汽车碳纤维图
- 保留现有 `::before` 碳纤维纹理(增强质感),调整 `::after` 绿色光晕保留品牌色点缀
- `.profile h1` 改为白色 `#fff`
- `.profile .profile_inner > span` 副标题改为浅灰 `#b8b8b8`
- 按钮:`.button:first-child`(Explore Guides)改为白底黑字高对比;`.button:last-child`(Work With Our Factory)保留绿色 CTA,增强阴影
- 加遮罩保证文字可读性

### Step 4:文章封面图(5 篇)

PaperMod 的 [cover.html](file:///d:/website/github/automotive-carbon-fiber-guide/themes/PaperMod/layouts/_partials/cover.html) 已原生支持 front matter `cover.image` 字段。给 5 篇文章 front matter 追加:

```yaml
cover:
  image: "/images/posts/xxx.jpg"
  alt: "描述性 alt 文本"
```

绝对路径 `/images/posts/xxx.jpg` 指向 Step 2 下载到 `static/images/posts/` 的图片。PaperMod 会在文章列表卡片顶部显示封面(cover.html 第 50 行处理绝对 URL)。

### Step 5:业务页 hero 图(5 个)

在每个业务页的 H1 下方插入一张 hero 图。因 [hugo.yaml](file:///d:/website/github/automotive-carbon-fiber-guide/hugo.yaml) 已设 `markup.goldmark.renderer.unsafe: true`,可直接在 markdown 写 HTML:

```html
<figure class="page-hero">
  <img src="/images/pages/about.jpg" alt="CHUICHUIFENG 工厂" loading="lazy" />
</figure>
```

5 个页面:H1(`# 标题`)之后紧跟 `<figure class="page-hero">`。

### Step 6:custom.css 卡片与页面图视觉升级

在 [custom.css](file:///d:/website/github/automotive-carbon-fiber-guide/assets/css/extended/custom.css) 追加:
- `.entry-cover`(PaperMod 文章卡片封面容器):全宽圆角、hover 时图片轻微放大 `transform: scale(1.02)`
- `.page-hero`:全宽 16:9 比例圆角图、阴影、`margin-bottom: 30px`
- 文章卡片 `.post-entry` 在有封面时调整间距,让封面贴顶显示
- 响应式:`@media (max-width:768px)` 调整 hero 字号、页面图比例

## 关键文件清单

| 文件 | 改动类型 |
|---|---|
| content/about.md, products.md, sourcing.md, oem.md, contact.md | 修 front matter + 加 hero 图 |
| content/posts/*.md(5 篇) | 加 cover front matter |
| assets/css/extended/custom.css | 追加深色 hero + 卡片 + 页面图样式 |
| static/images/hero/, posts/, pages/(新建) | 下载图片资源 |

**不改动**:`themes/PaperMod/*`、`hugo.yaml`(profileMode 结构保留)、`.github/workflows/*`、`content/posts/*.md` 正文。

## 验证方法(确保不搞崩)

1. **本地构建验证**(必做):
   ```powershell
   hugo server --disableFastRender
   ```
   访问 http://localhost:1313/automotive-carbon-fiber-guide/ 逐页检查:
   - 首页 hero 深色背景 + 图片显示 + 文字可读
   - /posts/ 列表页 5 张封面图正常显示
   - /about/ /products/ /sourcing/ /oem/ /contact/ 5 页 hero 图显示 + title 正常(验证 front matter 修复)
   - 5 篇文章详情页封面图显示
   - 控制台无 404 破图、无 CSS 报错

2. **front matter 验证**:用 `hugo --logLevel debug` 构建,确认 5 个业务页不再有 front matter 解析警告,且生成的 HTML `<title>` 和 `<meta name="description">` 正确。

3. **移动端验证**:DevTools 切到 375px 宽度,确认 hero 字号、卡片、页面图自适应无溢出。

4. **图片完整性**:确认 `static/images/` 下所有图片文件存在且被正确引用(无破图)。

5. **不回归**:对比改动前后,确认原有文章正文、表格、引用、面包屑、TOC、上下篇导航功能正常。

完成本地验证后,`git push origin main` 触发 GitHub Actions 自动部署。
