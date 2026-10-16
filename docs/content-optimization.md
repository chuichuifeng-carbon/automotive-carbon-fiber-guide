# 内容优化记录 · 2026-10-16

## 本站与主站的关系

- **ccfrp.com**：CCF 官方 B2B 商业网站，负责产品、企业核验、合作和询盘。
- **GitHub Pages**：配套英文采购知识库，帮助买家准备需求、比较证据并进入主站。
- 保留原有 14 篇文章 URL，不因修改标题改变路径。原创知识库文章使用自身 canonical；企业发布者的结构化身份指向 `https://ccfrp.com/#organization`。没有把所有文章 canonical 到主站首页。

## 修改范围

14 篇文章、5 个业务页、首页、指南目录，以及配套元数据和模板。保留企业介绍中的主体与历史资料；纠正其开发流程，使之与主站五阶段流程一致。其余文章按不同采购决策重写，减少重复和没有依据的泛化结论。

| 内容 | 主要服务的买家任务 |
|---|---|
| Manufacturer verification | 核验主体、生产现场及工序责任 |
| Supplier selection | 比较已经初步核验的供应商报价 |
| Questions to ask | 获取可以复制发送的供应商问询文本 |
| Wholesale | 规划首批采购与补货 |
| MOQ | 分清样品、SKU 最小量、包装最小量和模具成本 |
| Sample evaluation | 建立验收和放行记录 |
| Dry vs wet | 区分工艺、材料结构和表面效果 |
| Fitment cost | 计算安装返工及售后成本 |
| BMW guide | 按车型配置和 SKU 核验适配 |
| OEM/ODM | 确定开发责任、模具条款和阶段审批 |
| Import | 准备运输、报关、收货和成本记录 |
| Amazon / ACES | 管理有依据的适配数据与渠道更新 |
| Business launch | 用样品、需求和贡献利润决定首批库存 |
| Company profile | 了解 CCF 并准备企业核验 |

## 可信度与利他原则

- 删除没有依据的统一 MOQ/交期/税率表、减重表、缺陷率和固定允差。
- 算术示例明确标为示例，不作为工厂报价或行业统计。
- 修正 AQL 的错误解释，不用外观、手弯或敲击声证明结构性能。
- 不将付款比例、特定设备、贸易公司身份或拒绝一次视频通话作为单一可靠性判断。
- 明确样品验收、工程验证和市场合规的不同范围。
- 不承诺所有产品完美适配、所有询盘固定时限回复或第三方检验必然通过。
- 保留适合实际采购使用的 RFQ、对照表、验收清单和明确的下一步。

## SEO 与 GEO 的实施

- 每篇文章有独立搜索意图、直接开篇答案、标题、描述和真实更新日期。
- 清除正文重复 H1；添加相关指南链接，使用 Hugo `relref` 解析内部地址。
- 首页与指南页按任务组织内容；文章页增加相关资源及明确的主站询盘入口。
- `Organization` 使用 CCF 的企业身份；指南为 `BlogPosting`，业务页为 `WebPage`，提供日期及面包屑数据。
- 未添加虚构个人作者、评分、测试报告或不可见 FAQ 数据。
- 未添加所谓必须的 AI 专用文件或承诺 AI 引用。Google 的 AI 搜索指导仍强调有用、可靠的内容和基础 SEO。
- 文章末尾主站询盘按钮带 `utm_source=github_pages`、`utm_medium=referral`、`utm_campaign=buyer_guides` 和文章标识。参数用于主站分析归因；本项目未安装统计服务，不能据此宣称已测得询盘。

## 参考资料

核对日期：2026-10-16。主站资料是企业自述，不能替代买家独立核验；产品及商业条款仍需订单确认。

- [CCF 企业及工厂资料](https://ccfrp.com/about/)
- [CCF 联系及采购要求](https://ccfrp.com/contact/)
- [CCF OEM/ODM 流程](https://ccfrp.com/grow/oem-odm/)
- [CCF 批发合作](https://ccfrp.com/grow/wholesale/)
- [Google：AI 搜索与网站](https://developers.google.com/search/docs/appearance/ai-features)
- [Google：面向用户的有用内容](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Auto Care Association：ACES](https://www.autocare.org/aces)
- [Auto Care Association：数据标准](https://www.autocare.org/data-standards)
- [ISO 2859-1：AQL 抽样概述](https://www.iso.org/standard/2859-1)
- [CBP：具体商品进口要求](https://www.help.cbp.gov/s/article/Article-1397)
- [CBP：商业发票价值](https://www.help.cbp.gov/s/article/Article-1162?language=en_US)
- [USITC：美国税则](https://hts.usitc.gov/)
- [欧盟 TARIC](https://taxation-customs.ec.europa.eu/online-services/online-services-and-databases-customs/eu-customs-tariff-taric_en)

## 验证与维护

已用 Hugo Extended 0.168.0 执行生产构建，工作流固定到该版本。主题目前有语言 API 弃用提示，但构建通过；主题升级可另行处理。

```powershell
hugo --gc --minify
python scripts/check_site.py public
git diff --check
```

检查脚本使用 Python 标准库，检查生成 HTML 的 H1、description、canonical、JSON-LD、主站企业身份、内部页面/资源、锚点和 sitemap，并确认 14 篇原文章仍存在。脚本不验证外部站点 HTTP 状态，也不保证搜索引擎收录或富结果资格。

后续应优先补充有授权且对应 SKU 的真实测量、测试安装与检验案例。没有实测时，不将推测改写为工厂事实。只有实质修改内容时才更新 lastmod。

## 第二轮：样式、结构与版块

- 首页缩短首屏、明确知识库定位，增加四步采购路径与五类专题入口。
- 指南目录改为按任务分组的完整列表，14 篇指南一次可达，不再依赖按日期分页寻找。
- 分类配置集中在 `data/buyer_topics.json`；新增文章时需将其加入对应专题。
- 文章正文限制阅读宽度；桌面右侧提供滚动目录，较窄屏幕使用默认收起的原生 details 目录。
- 手机端隐藏装饰性封面，缩短面包屑；表格拥有独立横向滚动区并支持键盘聚焦。
- 文章末尾依据主题进入主站样品询盘、批发、车型目录或 OEM/ODM 页面，保留来源参数。
- 移动导航改为换行，避免 Contact 和 ccfrp.com 入口只能通过横向滚动找到。
- 页脚补充采购资源、官方企业资料、询盘及联系方式；保留主题署名。
- 所有模板覆盖位于项目 `layouts/`，没有修改供应商主题源码。

排版检查覆盖默认桌面视口与 390px 手机视口：检查首页、分类目录和代表性文章；验证折叠目录交互、侧栏显示及表格滚动。检查脚本新增重复 ID 和专题完整性检查。
