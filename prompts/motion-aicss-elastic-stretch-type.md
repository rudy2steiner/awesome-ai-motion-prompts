# Elastic Stretch Type

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/elastic-stretch-type) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/elastic-stretch-type)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** motion-studies
- **作品发布时间：** 2026-10-19
- **收集日期：** 2026-11-05
- **文本类型：** 作者公开完整可复用模板
- **参考素材：** 参见正文要求
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second elastic type piece: heavy letters are grabbed and stretched like rubber by an invisible hand, then snap back on springs with overshoot.

<inputs>
Word: LIMBER (a fictional stretching app).
Tagline: "Stretch a little every day."
Details: New classes every Monday
Length: 10 seconds.
</inputs>

<direction>
Palette: ground violet #6B4BFF; letters lime #D6FF4A; shadow deep violet #3A22B8; stretched-thin areas lighten toward #F1FFC2.
Type: "Dela Gothic One" 400 for the word, cap height 300px; "Space Grotesk" 500 for the tagline.
Rubber, not scaling: render each letter at 2x into its own texture on a 96x96-segment plane mesh in WebGL. Each grab is an anchor point and drag vector. A vertex moves by D*w with Gaussian falloff. Keep area roughly constant: stretched region gets thinner. Lighten color by local area stretch.
Springs: on release, D(s) = D0*e^(-zw*s)*cos(wd*s) with about three visible overshoots, settled within 1.4s.
Banned: uniform scaling or skewing of whole letters, a visible cursor or hand, wobble that never settles, motion blur, glow.
</direction>

<structure>
0.0-1.0s: letters drop in and squash onto the baseline.
1.0-2.0s: the L's stem is grabbed and pulled up, held, released: it snaps back.
2.0-3.0s: the I is pinched and pulled right.
3.0-4.0s: the B's lower bowl is pulled into a teardrop.
4.0-4.8s: both ends grabbed and pulled outward.
5.0-5.8s: the tagline rises.
6.6-7.6s: a last wink: the R's leg is tugged.
8.8-10.0s: hold.
</structure>

<build>
One self-contained index.html. One WebGL canvas, each letter's texture built on an offscreen 2D canvas. No libraries.
</build>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline. The prompt specifies a self-contained HTML file with inline CSS and JS, designed for 60fps playback with seek-based animation.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt. Note the technical constraints and how they shape the output.
