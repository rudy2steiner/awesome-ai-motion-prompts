# Isometric Hairline Explainer

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/isometric-hairline) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/isometric-hairline)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** explainers-data
- **作品发布时间：** 2026-10-12
- **收集日期：** 2026-11-05
- **文本类型：** 作者公开完整可复用模板
- **参考素材：** 参见正文要求
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
<inputs>
You're making a short isometric line-art explainer. I may supply any of these; if I don't give you something, use the default and don't ask.
- Subject: "From order to doorstep" for Parcelwing, a fictional courier.
- Stations: warehouse shelves -> conveyor -> van -> front door.
- Title: "Order to doorstep".
- Accent color: #FF4F2E.
- Length: 10 seconds.
</inputs>

<direction>
Ground #F6F5F1, ink #1C1D21, every face filled #FFFFFF and drawn back to front so near objects hide far lines. The accent fills only the hero object (the parcel) and the route dashes, under 8% of the frame. A dot grid (1.5px, #D6D5D0) marks the floor.
True isometric with unit u = 28px: screenX = (x-y)*cos30*u, screenY = (x+y)*sin30*u - z*u. Every edge follows one of the three axes; footprints snap to half units; no perspective.
One stroke: 2px, round caps and joins, non-scaling, so a pencil and a building share the same line. Detail means more lines, never heavier ones. Figures are 1.6 units tall: capsule body, circle head, no face.
Type: "IBM Plex Sans" 600 for the title (56px); "IBM Plex Mono" 500 for labels (18px, uppercase, tracking 0.08em), upright, on a horizontal hairline leader ending in a 5px dot.
Motion: parts assemble. A footprint draws on (0.3s, easeOutQuad), walls extrude up from z=0 (0.5-0.7s, easeOutCubic), then inner lines draw. Siblings stagger 80-120ms. Drops use easeOutBack with <=4% overshoot. Movers travel only along grid axes, easeInOutSine per leg, turning at right angles. Figures bob between two poses at 4 steps per second. The camera is locked apart from a 3% push across the whole piece.
Authentic: generous white space, a weight that never changes, the accent used like a highlighter. Cheap: depth faked with gray fills, objects drifting off-axis.
Banned: gradients, shadows, gray fills, vanishing points, mixed stroke weights, a second accent, emoji, icon libraries.
</direction>

<structure>
- 0-0.8s: grid dots ripple in from the center; the title draws on top-left.
- 0.8-2.6s: warehouse slab and shelves extrude; a figure pops in holding the accent parcel.
- 2.6-4.4s: the conveyor assembles segment by segment, roller ticks turning; the parcel rides it.
- 4.4-6.6s: the van body extrudes, wheels follow; the parcel loads; the van drives the x-axis road as accent dashes draw behind it.
- 6.6-8.4s: the house assembles; its door swings open as a parallelogram; a second figure takes the parcel.
- 8.4-9.0s: three labels pop on 150ms apart, leader first.
- 9.0-10s: hold.
Other lengths: scale the beats proportionally, keep entrance timings in range, end on at least 1s of hold.
</structure>

<build>
One self-contained index.html (inline CSS and JS; Google Fonts via <link> are fine), a 1920x1080 (16:9) stage scaled to fit the window, built for 60fps. Draw it all in SVG; three.js isn't needed.
window.seek(t) (t in seconds) sets every visual from t alone, clamping past the end to the last frame. No CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames. Any randomness comes from a seeded PRNG keyed to the frame, never Math.random.
With no ?render in the URL, call seek from requestAnimationFrame so it plays in a browser; with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second (0-10s) and look at each. Fix overlaps, clipped or cramped text and anything off-style: every edge on an axis, one stroke weight throughout, no line showing through a white face, labels clear of objects. Confirm the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline. The prompt specifies a self-contained HTML file with inline CSS and JS, designed for 60fps playback with seek-based animation.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt. Note the technical constraints and how they shape the output.
