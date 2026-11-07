# Clifford Attractor

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/clifford-attractor) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/clifford-attractor)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** 3d-simulations
- **作品发布时间：** 2026-10-19
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second film of the Clifford attractor as a long exposure: millions of points of one simple map build a glowing density image in copper on verdigris, then the four parameters morph and the figure folds and re-knots into new shapes.

<inputs>
If I don't give you something, use the default and don't ask.
- Studio: Pellworth Generative (fictional).
- Title: "Four numbers"
- Line: "The Clifford map, 4,194,304 points a frame"
- Closing caption: "Nudge one number and the whole figure refolds."
- Map: xₙ₊₁ = sin(a·yₙ) + c·cos(a·xₙ), yₙ₊₁ = sin(b·xₙ) + d·cos(b·yₙ).
- Keyframes (a, b, c, d): P₀ = (1.77, −1.49, 1.58, −0.91), P₁ = (1.81, −1.68, −0.85, −1.38), P₂ = (1.12, −1.13, 1.92, −1.09).
- Length: 10 seconds.
</inputs>

<direction>
- Palette, copper on verdigris: ground #0C2B27 with a soft radial lift to #123A34 behind the figure; density ramp on the tone-mapped value v: 0 the ground, 0.35 verdigris #1F5C52, 0.6 copper #C46A3A, 0.85 pale gold #F0C07E, 1.0 bone #FFF5E2, interpolated linearly. Faint regions glow green, dense filaments burn copper and gold: complements meeting in the mid-tones. Type #E7D3B8, secondary #9DB8B0, accent copper.
- The exposure, rebuilt fresh every frame so any frame can be drawn directly: 16,384 orbits from fixed seeded starting points in [−1, 1]², each iterated 32 steps unplotted, then 256 plotted steps: 4,194,304 points. Accumulate hit counts h per backing-store pixel, then tone-map v = ln(1 + h) ÷ ln(1 + h_ref), with h_ref = h₉₉.₅ × max(1, 4,194,304 ÷ N(t)), h₉₉.₅ the 99.5th percentile of the non-empty pixels and N(t) the points drawn this frame, so a short exposure looks short and a long one never blows out.
- Framing: the figure lies inside |x| ≤ 1 + |c|, |y| ≤ 1 + |d|; scale it by min(430 ÷ (1 + |d|), 590 ÷ (1 + |c|)) stage pixels per unit, centered at (1220, 540), y up. Because the parameters move continuously, so does the framing.
- The morph: straight lines in parameter space, P₀ → P₁ over 1.8–4.6 s and P₁ → P₂ over 4.6–7.6 s, each eased by smootherstep (6u⁵ − 15u⁴ + 10u³), so each shape holds briefly at its keyframe; P₀ before, P₂ after.
- Collapse guard (verified necessary): along these lines the map crosses narrow periodic windows where an orbit collapses onto a handful of dots, or nearly so, which would flash for a frame: for example near f = 0.215–0.222, 0.444–0.449 and 0.902–0.909 on P₀ → P₁, and 0.029–0.031, 0.071–0.074 and 0.313–0.320 on P₁ → P₂. At load, scan each segment at 4,000 evenly spaced f with 12,000 iterations on a 128 × 128 grid over its bounding box, mark f as collapsed where fewer than 15% of the cells are hit, widen every marked run by 0.002 on each side, and build a monotone remap of f that jumps over the runs (about 7–8% of each segment; the widest run is about 0.014, roughly one frame of motion, so the jumps are invisible). With it, every frame hits at least about 20% of the grid when measured with 40,000 iterations.
- Exposure over time: the plotted steps per orbit ramp from 0 to 256 over 0.2–1.8 s, so the first figure arrives as scattered sparks that gather into filaments; over 8.2–8.8 s they rise to 1,024 (16.8 million points) for a deeper, finer final image.
- Readouts, left column x 120–560: the map in Bellefair 400, 34px, two lines at (120, 420); a, b, c and d from (120, 560) at 46px intervals in Victor Mono 400, 26px, tabular, three decimals, each with a 160px track from −2 to 2 and a copper dot at its value; "Points this frame" with its count in Victor Mono 400, 22px, secondary, at (120, 790).
- Type: the kicker in Victor Mono 500, 20px, tracked 0.18em, uppercase, copper, at (120, 96); the title in Bellefair 400, 108px, #E7D3B8, at (120, 220); the line in Bellefair 400, 30px, secondary, beneath; the closing caption in Bellefair 400, 32px, #E7D3B8, at (120, 960).
- Easing: text rises 12px as it fades in over 0.6 s on cubic-bezier(0.22, 1, 0.36, 1); readout digits change continuously with the parameters.
- Premium: millions of points building a soft, filament-rich density with deep shadows and hot copper cores, a morph that stays chaotic in every frame, crisp at 1280×720. Cheap: a few thousand dots, rainbow coloring, frames that collapse to dots, bloom smearing everything.
Banned: rainbow or hue-cycling color, bloom or blur, frames where the figure collapses to a few dots, visible point grain at the end, colors beyond the palette, camera shake, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.2s: the verdigris ground; the kicker and title rise in.
- 0.2–1.8s: the exposure builds at P₀: copper sparks scatter, then filaments gather into the first figure; the map and readouts rise in at 0.8 s.
- 1.8–4.6s: the morph to P₁: ribbons fold through each other and re-knot as c swings through zero; the readout dots slide along their tracks.
- 4.6–7.6s: the morph to P₂. The 6.0 s frame: a complete figure midway between P₁ and P₂, sharp and fully exposed.
- 7.6–8.8s: the figure settles at P₂; from 8.2 s the exposure deepens fourfold and the filaments sharpen; the closing caption rises in.
- 8.8–10.0s: hold, completely still.
For other lengths, stretch the two morphs equally; keep the build-up and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas: one WebGL2 canvas (preserveDrawingBuffer: true), its backing store sized from CSS size × devicePixelRatio. Iterate the 16,384 orbits with transform feedback, one pass per step, drawing each step's points as 1px points with additive blending into an R32F accumulation texture (EXT_color_buffer_float and EXT_float_blend); read it back once per frame for h₉₉.₅; then one full-screen pass tone-maps and colors it. If EXT_float_blend is missing, accumulate the same points on the CPU instead. Type is HTML; the readout tracks are a 2D canvas.
- The collapse scan and remap are computed once at load (keep load under 5 s); the parameters, framing and point count are closed-form functions of t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Also log, for every frame from 1.8 to 7.6 s, the share of the bounding-box grid the figure covers; with 40,000 iterations no frame may drop below 15%. Check the first second reads as sparks gathering into filaments rather than noise, filaments stay crisp, the brightest cores reach gold and bone without clipping into flat blobs, the figure stays inside its frame and clear of the text column, and the final frame is smooth with no visible grain. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
