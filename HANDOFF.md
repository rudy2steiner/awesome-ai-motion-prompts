# Motion Prompts 每日维护交接

更新时间：2026-11-07（北京时间）。本文记录当前已验证状态及后续执行方法；后续运行须重新检查远端、工作区和生产版本，不把本快照当作实时状态。

## 1. 任务目标与授权

每天北京时间10:30执行自动化 `motion-prompts`：收集、核验、提交并推送来源仓库，再同步到 Open Prompts，构建发布并检查正式网页。用户已授权本任务相关的正常提交、推送和发布，无需逐次询问。

- 以 `data/categories.json` 的现有7类为准，每类当天至少新增5条，全天至少50条；额外15条按质量与热度分配。
- 同日重跑先读日报和已有记录，累计当天新增量，避免重复计数。历史批次不重复补收。
- 正文、作者、原作、提示词来源、对应输出必须真实可追溯；保留实际发布日期、可得热度、观测时间和作用范围。未知值保持未知。
- 按原作URL、视频标识、规范化提示词去重。不用缺正文、缺输出、重复、无关作品或虚构指标凑配额。
- 精选须检查播放效果、文字可读性、节奏、设计技巧和提示词对应关系，有合适预览后才能加入。热度、元数据和单帧都不能替代完整质量审核。
- 达不到配额时如实写分类数量、缺口和原因；旧作补收不能称为当天新发布，未知热度不能称为已验证热门。
- 仅暂存本任务文件，保留其他任务改动；正常推送 `origin/main`，禁止强制推送。

## 2. 项目与权威资料

| 项目 | 本地目录 | 关键资料 |
| --- | --- | --- |
| 收集仓库 | `/Users/xuandu/mywsp/awesome-ai-motion-prompts` | `CONTRIBUTING.md`、`CONTRIBUTING.zh-CN.md`、`data/collection-reports/` |
| 网站仓库 | `/Users/xuandu/mywsp/open-prompts` | `docs/motion-prompts-integration.md`、项目指令及现有构建发布配置 |
| 正式网站 | `https://www.open-prompts.com/motion-prompts` | 以及 `/en`、`/zh`、`/ja`、`/ko`、`/de`、`/fr`、`/es`、`/pt` 下的对应页面 |

进入项目后先读适用的 AGENTS 与贡献规范。若根目录存在 `.codegraph/`，理解或定位代码时先用 CodeGraph；不存在则跳过。

## 3. 当前完成状态

2026-11-07已收集、双仓库推送、发布并通过正式域名API验收。今日新增50条。

| 项目 | 数量或状态 |
| --- | --- |
| 当天新增 | 50条 |
| 来源数据总量 | 1551条 |
| 网站原始导入量 | 1551条 |
| 历史质量排除 | 197条，保持不变 |
| 无海报条目 | 约366条 |
| 网站实际可展示 | 1185条；本批实际新增32条（18条无海报生成或为X帖子） |
| 新增精选 / 新增排除 / 导入失败 | 0 / 0 / 0 |
| Node测试 / Python回归 | 16项通过（含2项计数断言更新） / 1项通过 |
| 正式发布版本 | `0d4517df-3dba-41c6-8223-746724b45f82` |

当天分类（50条）：`product-brand` 7、`motion-studies` 7、`explainers-data` 8、`characters-stories` 7、`3d-simulations` 8、`interactive` 7、`music-audiovisual` 6。七类本日均达标（≥5）。

提交记录：

- [来源数据 0e25afb](https://github.com/rudy2steiner/awesome-ai-motion-prompts/commit/0e25afb)
- [来源日报](https://github.com/rudy2steiner/awesome-ai-motion-prompts/blob/main/data/collection-reports/2026-11-07.md)
- [网站数据 c912230](https://github.com/rudy2steiner/open-prompts/commit/c912230)
- [网站发布验收](https://github.com/rudy2steiner/open-prompts/commit/c912230)

详细证据见 [2026-11-07日报](data/collection-reports/2026-11-07.md)。**10月29日音乐类只有2条、缺3条的历史问题仍保留，不倒算补齐。**

已知预存问题：`tests/motion-media-performance.test.ts` 有1项测试在原始main上即失败（previewVideo匹配逻辑与catalog video分辨率不一致），与本次导入无关。

本次撰写交接时，网站原工作区有其他任务修改：`src/components/prompt-gallery/CoverImage.tsx`、`tests/gallery-native-first-paint.test.tsx`、`messages/*.json`、`next.config.mjs`、`src/app/` 多个页面、`src/lib/seo/` 等。不要暂存、丢弃或直接将它们纳入本任务发布；实际操作前重新检查状态。

## 4. 来源数据维护

唯一作品数据集为 `data/videos.json`；每条正文写入对应 `prompts/*.md`，保持原始语言和原文。同步 `data/README.md` 及中英文 README 总数。

每条保留：ID、作者、模型来源声明、原作和提示词链接、输出URL/视频标识、分类、发布时间、收集日期、参考素材依赖、文本完整性、许可和审核说明。建议保存正文SHA-256及取证方法，区分来源声明与独立核实。

- `status: collected` 表示收录，不表示已审核质量或模型归属。
- `featured` 与 `data/categories.json` 的展示ID及两种语言精选卡片要一致；没有合格新精选时无需更改。
- 短要求、完整转录、作者完整模板和导演简报摘录分别标记，不能一概称完整提示词。
- 热度要区分原帖独立点赞、上游目录转录、仓库Stars等作用范围，不混算。
- 封面必须对应真实输出；原帖缩略图记录为缩略图，不能称作已播放或解码抽帧。

30日的50条由42条作者公开CC0模板、4条上游完整转录、2条原作者简短要求、2条Claudia Gallery导演简报摘录组成。42条模板多为旧作补收且热度未知；6条X作品取得独立点赞快照。两部音乐电影只对应作者公开循环预览，保留 `outputCompleteness`，不称完整MV。图库/角色使用许可不能扩张为歌曲、提示词或第三方素材许可。50张封面中47张为视频帧，3张为原帖视频缩略图，未因此新增精选。

## 5. 网站同步：必须保留旧记录与媒体

实际列表及详情的数据链路为：

```text
awesome-ai-motion-prompts/data/videos.json
  → scripts/import-motion-catalog.py
  → src/data/imports/motion-catalog.json
  → src/lib/motion/catalog.ts
  → 列表 / 详情 / 分页API
```

不要只改未被实际页面使用的旧数据，例如 `src/data/promptMotion.ts`。

在安全的最新main工作区执行现有导入器：

```sh
python3 scripts/import-motion-catalog.py /Users/xuandu/mywsp/awesome-ai-motion-prompts
```

导入器会生成真实封面，并调用现有媒体复用流程。**当前导入器仍可能丢失顶层完整性等字段，或重新生成既有媒体。** 导入前保存已提交的旧目录，导入后以来源和ID幂等合并，逐条恢复旧记录及已核验媒体，仅加入新有效条目；不能只检查总数。

重点核对 `promptStatus`、`promptCompleteness`、`outputCompleteness`、`requiresReference`、`license`、`postedAt`、`notes`、`verification`、`collectedAt` 和热度来源。保留质量排除清单、精选顺序、`motion-media-enrichment.json` 及既有封面/短预览。不得恢复被排除作品或伪造可用预览。

按需运行 `collect-motion-popularity.py`；默认可能处理很多历史记录，新增批次可限定刷新范围，但须保留旧有效观测、未知值及身份验证逻辑。高赞新增进入默认首屏时，需要补齐真实短预览；首屏与精选检查不能通过删除断言绕过。

## 6. 验证、提交与发布

每轮开始、推送前分别检查两个仓库的最新远端main：

```sh
git status --short
git fetch origin main
git rev-list --left-right --count HEAD...origin/main
```

远端有新生产改动时，正常合并或重放，并在新基线上重新验证。不能仅凭旧本地脏工作区宣称基线阻塞。不要从包含无关改动的工作区构建发布。

30日使用的隔离目录为 `/tmp/open-prompts-motion-sync-20261029`，最终提交为 `ed33f54`。它属于临时工作区，可能被清理；复用前确认Git状态、远端基线和依赖，不依赖其存在。旧的 `/tmp/open-prompts-motion-sync-20261024` 不应复用，曾出现Git元数据损坏。临时辅助脚本不是持久化流程的一部分。

来源检查：新旧记录、ID/URL/视频/正文去重、本地正文一致、SHA、分类与总数、链接与真实媒体、README及精选一致、`git diff --check`。

网站检查与构建命令（在网站安全工作区）：

```sh
node --import tsx --test tests/*.test.ts tests/*.test.tsx
python3 -m unittest discover -s tests -p 'test_motion_popularity_collection.py'
node_modules/.bin/opennextjs-cloudflare build
```

必要时按项目现有方式初始化隔离目录本地D1迁移；不把空本地库缺表当成业务回归，也不擅自迁移生产。合理更新随目录增量变化的固定计数断言，不绕过测试。测试产生的已跟踪 `__pycache__` 变化不要混入提交。

构建后检查 `.open-next/cache` 下8语言 `motion-prompts.cache` 的新总数，并遵守项目现有缓存复制与 `.assetsignore` 规则。旧列表缓存可能掩盖新数据。

只暂存本任务数据、媒体、必要断言和文档，中文提交信息，正常推送。无变化不建空提交。推送冲突或认证失败保留本地成果并报告，禁止强推。

发布前用项目现有 Cloudflare CLI 检查活跃部署与当前main是否对应；`deployments list` 的返回顺序不能直接假设最新在首位，按创建时间核对。生产基线明确后执行：

```sh
NODE_OPTIONS='--require=./scripts/cloudflare-upload-timeout.cjs' node_modules/.bin/opennextjs-cloudflare deploy
```

30日首次请求Cloudflare服务信息超时，重试成功；59个资源上传后，Worker版本上传仍耗时数分钟。等待明确成功回执和Version ID，不把资源上传、代码推送或本地构建当作上线。未完成的版本上传不要并发重试。

## 7. Chrome MCP与线上验收

遵守用户浏览器指令，优先 `mcp__chrome_mcp__*`。工具列表可能动态变化，要重新发现；此前仅因出现streamable命名空间就认定Chrome不可用，判断过严，同一Chrome连接曾在该命名空间正常工作。若确实不可用，报告阻塞并请用户决定，不静默改用Computer Use或in-app browser。

**已知异常：Chrome截图接口曾返回错误窗口内容，即使指定目标tab、窗口和前台模式也不能保证正确。** 所有截图必须先视觉核对；不把不匹配内容写入仓库。30日错误截图全部弃用删除，电影帧改为直接读取目标视频画布并检查实际画面。不要再次把截图接口当成已修复；能用DOM/网络结果验收时不必截图。

只操作本任务创建或明确接管的标签，避免读取其他工作页面。标签可能被关闭，遇到Tab not found可创建新的任务标签。后台视频未解码不一定是坏链；必要时激活目标标签并将播放器滚入视口，再检查readyState和时间推进。

上线验收至少包括：

1. 成功发布回执及版本ID。
2. 正式www域名列表DOM总数和 `/api/motion-prompts` 总数一致。
3. 遍历分页确认唯一ID、今天新增ID无缺失；末页正常结束。
4. 抽查新增详情正文、简短/摘录与参考依赖信息、封面、精选顺序。
5. 8语言页面及无语言入口正常；新封面和首屏短预览可获取。
6. 真实短视频路径从API的 `previewVideo` 取得，通常带哈希；不要猜测无哈希文件名。

30日验收基准：1103个唯一ID、92页，末页offset1092为11条、nextOffset=null，新增50条缺失0；8语言均200。精选首位 `2113248976984068329`（Minecraft地图），真实短预览为API提供的带哈希URL。未来新增后相应重算页数和末页位置。

## 8. 下一轮接手清单

- 先读本交接、最新日报和网站集成文档，核对两个仓库远端与工作区。
- 从新日期开始累计，11-07的50条已上线（总计1551条、可展示1185条），不重复导入或计为新收集。
- 继续扩展近期原作者来源，改善音乐类来源和高质量精选审核；不要长期靠单一旧模板来源完成数量。
- 当前没有未完成发布或浏览器验收；29日音乐缺口属于历史记录。导入器字段保留和截图异常仍是已知风险，后续修改工具需另行验证。
- `tests/motion-media-performance.test.ts` 的1项预存失败已知（previewVideo匹配问题），不影响功能；后续如修复需同步更新相关断言。
- 完成后日报分别列来源新增、七类数量、精选变化、导入/可展示/排除/失败数量、两个仓库提交链接、发布版本和正式网页验收。失败时说明已完成部分及具体阻塞，不声称已上线。
