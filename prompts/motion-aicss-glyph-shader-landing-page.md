# Glyph Shader Landing Page

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/glyph-shader-landing-page) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/glyph-shader-landing-page)

- **作者：** Wu Chenmu
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** interactive
- **作品发布时间：** 2026-10-05
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
# Glyph landing page

One subject → one page. The subject loops (a Kling clip pinned so its last frame is its first); the shader draws it as
glyphs over an animated backdrop. On the page:

- **Hero:** cursor X splits *photo ← | → glyphs*; cursor Y sets the grid size; a ring and crosshair follow the cursor.
  The title — one word split in two — is drawn by the shader as the inverse of a blurred backdrop. Dense line art,
  some of it tracking the subject.
- **Sections:** manifesto (a true fact with a turn), marquee, four specs, a closing CTA over the subject again.
  Scrolling dissolves the grid into big pixels and back.
- **Series:** several pages share one engine and a page switcher; each page gets its own palette, background effect,
  glyph renderer, fonts, line art and copy.

`assets/examples/pages/` holds five complete pages that show the range (astronaut on a night sky, a poppy on paper, the
1984 Mac as a blueprint, a cloud with halftone and isobars, jellyfish in neon braille). Read one or two before writing a
page; never copy one wholesale — each page is designed fresh for its subject.
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
