# Whiteboard Doodle Explainer

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/whiteboard-doodle) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/whiteboard-doodle)

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
You're making a whiteboard doodle explainer drawn in marker. I may supply any of these; if I don't give you something, use the default and don't ask.
- Title: "How a Rain Garden Works".
- Beats: rain hits a roof -> the downspout feeds a planted dip -> water soaks down through the soil -> less runoff reaches the street.
- Labels: "slows", "soaks", "filters", "less runoff!"
- Length: 10 seconds.
</inputs>

<direction>
Board #F8F8F5 with the ghost of old erased marker (three large soft gray smudges at 3-5%) and a faint vignette. Markers: black #1E1F24, blue #1E5BB8, red #D23A2F, green #2F8A4F, nothing else.
Strokes are 6px marker lines (title 9px), round-capped, 0.92 opacity, roughened with an feTurbulence + feDisplacementMap filter at scale ~2. Build shapes from hand-plotted point lists, never perfect primitives: corners overshoot 4-8px, circles miss closing by a few pixels, arrowheads are two separate flicks, baselines wander +/-3px. Shade with quick 45-degree hatching, never flat fills.
Line boil: boil = floor(t*12) mod 3. Offset each point +/-1.2px with a PRNG seeded by (strokeId, boil), and set the turbulence seed to one of three values by boil. Finished lines keep boiling during holds; the board never freezes.
Type: the title is hand-lettered in "Permanent Marker", 84px; labels in "Gochi Hand", 40px. Text never fades in: a left-to-right clip reveals it at about 14 characters per second, as if written.
Draw in the order a person would: outline, details, then hatching. Strokes travel at about 1,400px/s, so length sets duration (usually 0.2-0.6s), with easeInOutSine at each end and a 60-120ms pen lift between strokes. A flat-drawn marker in the same doodle style, tilted 25 degrees, rides the active stroke tip and lifts 12px between strokes.
Cheap versions use perfect vector shapes, a handwriting font faded on, and lines that sit dead still.
Banned: fades or scale-ins as entrances, perfect geometry, gradients, shadows, a fifth color, clip-art, photographic hands, emoji.
</direction>

<structure>
- 0-1.6s: the title is written in black; a red swoosh underlines it at 1.3-1.6s.
- 1.6-3.4s: a house with roof and downspout (black); a blue cloud; dashed rain streaks that shift down each boil frame.
- 3.4-5.2s: a blue arrow curls from the downspout into a shallow dip; green plants sprout in quick strokes.
- 5.2-7.0s: cutaway: ground line, hatched soil layers, wavy blue arrows sinking; "slows", "soaks" and "filters" written with small arrows.
- 7.0-8.4s: a red scribbled circle around the garden; "less runoff!" written in red.
- 8.4-9.0s: the marker slides off bottom-right.
- 9.0-10s: hold, still boiling.
Other lengths: keep the drawing speed constant and give extra time to holds, not slower strokes.
</structure>

<build>
One self-contained index.html (inline CSS and JS; Google Fonts via <link> are fine), a 1920x1080 (16:9) stage scaled to fit the window, built for 60fps. Draw in SVG; three.js isn't needed.
window.seek(t) (t in seconds) sets every visual from t alone, clamping past the end to the last frame. No CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames. All wobble and filter seeds come from a seeded PRNG keyed to the boil frame, never Math.random.
With no ?render in the URL, call seek from requestAnimationFrame so it plays in a browser; with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second (0-10s) and look at each. Fix overlaps, clipped or cramped text and anything off-style: every frame looking hand-drawn rather than vector-perfect, boil visible but not jittery, labels clear of drawings, the marker never covering text. Confirm the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline. The prompt specifies a self-contained HTML file with inline CSS and JS, designed for 60fps playback with seek-based animation.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt. Note the technical constraints and how they shape the output.
