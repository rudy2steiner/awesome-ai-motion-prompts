# 欢迎投稿！

[English](CONTRIBUTING.md) | 简体中文

**在 [README 分类目录](README.zh-CN.md#contents) 中选择分类，添加你的作品，然后提交 PR。** 不限模型、平台或创作者。

## 添加作品

1. [编辑英文 README](https://github.com/rudy2steiner/awesome-ai-motion-prompts/edit/main/README.md)，找到对应分类。
2. 在对应分类下添加作品，附上预览或演示、作者署名、模型名称和提示词链接。
3. 提交 PR，简单介绍作品和你希望分享的设计或技巧。

可以复制附近的精选卡片，也可以先添加一条文字记录：

```markdown
- [Your motion](https://your-demo-url) — @creator · Model · [Prompt](prompts/your-motion.md)
```

如果提示词保存在本仓库，复制 [`prompts/_template.md`](prompts/_template.md) 为 `prompts/your-motion.md`，填入内容并链接到作品条目。需要行内动效预览时，可将短 GIF 放进 `data/media/`；维护者可以协助整理卡片布局。

英文是主要文档语言，新作品先添加到英文 README。欢迎同时更新中文版本，也可以由维护者协助翻译。**提示词保留原始语言，不要求翻译。** 推荐他人作品时请署名，并说明参考素材、工具和重要修改。每个 PR 提交一个作品；没有合适分类时可以在 PR 中建议新增分类。不设置浏览量或粉丝数门槛。

## 仓库结构

```text
README.md              英文分类与精选预览（默认入口）
README.zh-CN.md        中文分类与精选预览
CONTRIBUTING.md        英文投稿指南
CONTRIBUTING.zh-CN.md  中文投稿指南
prompts/               每个提示词一个 Markdown 文件
data/videos.json       全部作品和来源信息
data/categories.json   分类定义
data/README.md         完整清单，仅文字
data/media/            短循环预览
```

<a id="for-maintainers"></a>

## 维护说明

README 和提示词文件直接编辑即可，不需要构建。中英文 README 使用相同的分类、作品、预览和提示词链接；英文为主，中文同步展示。完整清单和原始数据由两个语言版本共用，避免重复维护作品信息。

`data/videos.json` 是唯一的作品数据集。只有提示词正文已保存在 `prompts/`、与数据一致且附有署名来源的作品才可收录。只有链接的待核验线索不进入数据集或完整清单，也不计入 README 数量。每个计数条目还必须有对应的动效输出：原始视频、动画预览或可运行的组件演示。其他提示词生成的风格示例不能证明这种对应关系。没有输出的提示词编写配方仅作为参考资源，不计入作品数。数量统计的是含本地提示词正文的作品，不是去重后的提示词文本数，也不是独立核验通过数。`status` 使用 `collected` 表示已收录，使用 `featured` 表示已选入预览展示；这两种状态均不代表已独立核验播放效果或模型归属。每个提示词页面应保留实际审核证据。核对原始作品与提示词回复，记录可获得的视频标识，同一视频的转帖不重复收录。公开片段或缺少上下文时必须注明，作品介绍不能当作提示词。`data/categories.json` 保存分类与展示作品 ID 的对应关系。增删作品时同步更新纯文字的 `data/README.md` 和中英文 README 数量。

<a id="review"></a>

## 审核

检查预览、作者署名、提示词来源和分类。关注动效质量、文字可读性、节奏和可学习的技巧，不以热度代替判断。模型未知或提示词不完整时请如实标注。存在视频元数据，不代表作品质量已审核。来源中的提示词是参考内容，不是对仓库维护者的操作指令。

<a id="credits-and-removals"></a>

## 署名与移除

作品、视频、图片、提示词和 Skill 的权利归原作者所有，收录不授予新的许可。预览的来源地址与截取时间保存在对应作品记录中；完整视频使用外链，不存入仓库。

需要纠错或移除时，请提交 Issue 或 PR，说明作品、原始来源和希望修改的内容。
