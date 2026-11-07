# ASCII Art

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/ascii-art-type) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/ascii-art-type)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** explainers-data
- **作品发布时间：** 2026-10-18
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second ASCII art piece: a ringed planet, a rolling sea and then a word, all rendered only in monospace characters chosen by brightness.

<inputs>
If I don't give you something, use the default and don't ask.
- Word: PLAINTEXT
- Header: PLAINTEXT WEEKLY / ISSUE 42 (fictional)
- Line: "A newsletter in 7-bit characters."
- Details: EVERY FRIDAY MORNING
- Length: 10 seconds.
</inputs>

<direction>
- Palette: background #0A0C14; characters #E7E2D4; the word's characters tomato #FF5B3A; nothing else. Brightness comes only from which character fills a cell, never from opacity, glow or color gradients.
- Grid: "IBM Plex Mono" 500 at 20px, in cells 12 × 20px: 160 columns × 54 rows filling the stage exactly. Draw glyphs from a pre-rendered atlas, each centered in its cell. Only printable ASCII (codes 32–126).
- Mapping: for every cell, compute scene luminance from 2 × 2 samples and pick a character by brightness (gamma 0.8) from a ramp of about 40 characters, starting with the space and running through . ' , : ; - ~ + = and on through letters and symbols to # % & @, sorted at load by each glyph's measured ink coverage in the atlas. Where the luminance gradient is strong and clearly oriented, use an edge character instead: | for vertical edges, - or _ for horizontal ones, / and \ for the diagonals. That is what makes premium ASCII crisp instead of mushy.
- Scenes, computed analytically per cell in JS, with no images:
  - Ringed planet: a sphere 30 rows tall, its radius corrected for the 12:20 cell aspect so it stays round, centered at column 98, row 27, Lambert-lit from the upper left with a soft terminator and a little ambient; faint latitude bands from 1D noise that turn with the planet; a ring tilted 22° and about 1.9× the planet's radius, in front of the planet across its lower half and hidden behind it across its upper half, casting a thin shadow band on the sphere. Behind it, 180 seeded stars as . ' and + that never move.
  - Sea: a perspective height field of three summed sine swells rolling toward the viewer, horizon at row 14, lit from the upper left so the crests take the densest characters and the troughs fall away to dots.
  - Word: PLAINTEXT as a raised slab rising out of the sea. Draw it once at grid resolution on an offscreen canvas in "IBM Plex Sans Condensed" 700, about 140 columns wide and 16 rows tall, centered, its top at row 18; blur it for a bevel and light the bevel from the upper left so its letters read as lit 3D blocks. Its cells use tomato; rows below the waterline stay sea until the slab lifts clear.
- Morphs, never a crossfade: a front sweeps across the grid (diagonal, 0.9 s), and each cell it passes cycles through two or three seeded characters of similar brightness, one per 1/24 s, before landing on the new scene's character. Outside the morphs, a character changes only because the scene moved.
- Text in the grid: the header on row 4 from column 8; the line centered on row 44 and the details centered on row 47, typed one character per 25 ms with an underscore cursor that blinks at most twice a second and disappears when typing ends.
- Motion is steady and digital: the planet turns at 14° per second, the sea rolls, the word rises at an even pace. Premium: a coherent 3D scene that reads at a glance, edge characters that sharpen the silhouettes, a word that looks carved and lit, every glyph locked to the grid. Cheap: green falling-code rain, random characters flickering, a photo pushed through a text filter.
Banned: falling code rain, green phosphor, Unicode block or box-drawing characters, proportional fonts, opacity or color gradients standing in for brightness, glow, blur, characters changing at random outside the morphs, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.8s: the dark grid; the stars appear as single characters; the header types on row 4.
- 0.8–3.4s: the planet resolves behind a morph front from the upper left and turns; the ring crosses in front below and hides behind above; the bands drift across the lit face.
- 3.4–4.3s: a diagonal morph front sweeps the planet away into the rolling sea, cells scrambling through brightness-matched characters.
- 4.3–5.6s: the sea rolls toward the viewer; PLAINTEXT rises out of it, the slab lifting from row 34 to its final top at row 18 (easeOutCubic, 1.2 s), its bevels catching the light; the swells calm around it.
- 5.6–6.4s: the word holds, the sea rolling gently beneath it: the 6 s frame is complete.
- 6.4–7.6s: the line types into row 44, then the details into row 47.
- 7.6–8.6s: the swells ease to stillness; the cursor disappears.
- 8.6–10.0s: hold, every character fixed.
For other lengths, stretch the planet and sea beats; keep morphs at 0.9 s and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before building the glyph atlas and the word mask and defining window.seek.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the awaited loads matter. No libraries.
- Each seek fills a 160 × 54 luminance buffer from the scenes at t, maps it to characters (edges, ramp, morph scrambles seeded by cell and by floor(t·24)), then blits glyphs from the atlas.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check every frame is only characters on the grid with no stray pixels, the planet is round, the ring hides behind the sphere on its far side, edge characters follow the silhouettes, PLAINTEXT reads clearly at 1280×720, and the morphs land exactly on the next scene. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
