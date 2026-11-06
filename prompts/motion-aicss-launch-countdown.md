# Mechanical Launch Countdown

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/launch-countdown) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/launch-countdown)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** explainers-data
- **作品发布时间：** 2026-10-19
- **收集日期：** 2026-11-05
- **文本类型：** 作者公开完整可复用模板
- **参考素材：** 参见正文要求
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second event countdown from 10 to 0 on mechanical number drums, revealing the event at zero.

<inputs>
Event: SABLEWOOD. Line: "Design Conference 2026 - Doors open". Details: "Pier Hall - 16 October - 19:00". Count from: 10. Duration: 10s. If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Palette: concrete #E5E2DA, plate #D6D2C8, ink #161616, drum face #F5F2EB, inset well #1C1C1C, ring track #C9C4B9, and signal orange #FF5A1F.
Type: Barlow Condensed 600 for the digits (330px) and 800 for the event name (150px); IBM Plex Mono 500, 22px, for labels.
Instrument: a ring 820px across with a 16px stroke. The time remaining is an orange arc from 12 o'clock running clockwise, shrinking as time passes; 60 tick marks sit outside it. Inside, a plate with two drums side by side.
Drums: each a 10-face prism in CSS 3D, faces 300px tall. Shade each face by its angle to the viewer.
Timing: a tick every 0.7s. Each tick turns with overshoot, settled by 0.35s, like a detent.
Reveal: at zero the ring fills orange; the plate drops and the event name rises.
Banned: glow, neon, seven-segment or LED digits, confetti, fireworks, camera shake, lens flares.
</direction>

<structure>
0.0-0.4s: concrete ground; the ring track draws.
0.4-7.4s: the ring drains while ten ticks take the drums from 10 down to 00.
7.4-8.4s: the reveal: SABLEWOOD rises centered.
8.4-10.0s: hold the lockup inside the full orange ring.
</structure>

<build>
One self-contained index.html, CSS and JS inline. The stage is 1920x1080 (16:9). Engine: HTML/CSS with CSS 3D transforms for the drums and inline SVG for the ring and ticks. No canvas or three.js.
</build>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline. The prompt specifies a self-contained HTML file with inline CSS and JS, designed for 60fps playback with seek-based animation.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt. Note the technical constraints and how they shape the output.
