# Calligraphy Signature

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/calligraphy-signature) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/calligraphy-signature)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** motion-studies
- **作品发布时间：** 2026-10-18
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second close-up of a pointed pen writing a copperplate signature: ink swells on every downstroke, thins to hairlines on the upstrokes and pools where the pen pauses.

<inputs>
If I don't give you something, use the default and don't ask.
- Signature: Eloise Hart
- Line beneath: "Wedding stationery, written by hand"
- Small caps line: ELOISE HART STUDIO · EST. 2011 (fictional)
- Length: 10 seconds.
</inputs>

<direction>
- Palette: cream cotton laid paper #F4EDDF; wet ink #232838, blue-black with a glossy highlight, drying to iron-gall brown-black #261C16; desk walnut #3A2A1F, seen only beyond the sheet's deckled edges; nib steel #9EA3A8 with a brass flange #B08D57 on a black holder #151312; printed lines #4B3C31.
- Paper: the sheet fills x 140–1780, y 90–990, with deckled edges, laid lines (1px, 3% darker, every 7px horizontally), chain lines (every 120px vertically, 4%) and fine fibers, generated once at load, lit by a warm lamp from the upper left that falls off 12% toward the lower right. The pen and holder cast a soft shadow on the sheet.
- Copperplate, built properly: slant 55° from the baseline; baseline y 600; x-height 96px; ascenders and capitals reach 270px above the baseline, descenders 150px below; the signature spans about x 400 to 1520. Author it as centerline cubic Béziers in writing order, letter by letter on that slant grid: a capital E with an entry hairline, a small top loop and a shaded spine and bottom oval; l with a tall hairline loop and a shaded stem; o as a slanted oval shaded on its left side; i; s with a shaded body; e with a hairline loop; a capital H with two shaded stems and a looped hairline crossbar; a, r and t joined by hairline connectors. The i's dot, the t's cross and a long underline swash come last, as real signers add them. Every main downstroke is parallel to the slant, ovals are consistent, and downstrokes are evenly spaced.
- Pen physics: width w = 1.4px + 17px × p, where pressure p rises only on downstrokes, ramping in over the first 20% of a stroke and out over the last 25% (a swelled shade); upstrokes and connectors stay hairlines. The pen moves at 260px/s through shades and 800px/s through hairlines (scale both together if a beat needs it, keeping that ratio); between strokes it lifts and travels on a shallow arc at 1200px/s while its shadow slides 26px away and softens. Draw the nib at the writing point, angled to the slant, its two tines visibly spreading in proportion to w.
- Ink: stamp overlapping discs along each stroke into an ink layer, with slight density variation and a 1px darker rim along the edges of shades, where ink gathers as it dries. Where the pen stops (stroke ends, the i's dot, the end of the t's cross), a pool forms: a darker, slightly wider bead that keeps its wet highlight longest. Wet ink carries a thin glossy highlight along heavy shades that fades over 1.2 s after the pen passes, as the color shifts from wet to dry.
- Camera: a slow push from 1.0 to 1.06 that follows the pen loosely in x with a 0.4 s lag and ends framed on the whole signature, centered.
- Type: the line beneath in "Libre Caslon Text" italic, 34px, #4B3C31, centered on baseline y 830; the small caps line in Libre Caslon Text 400, 22px, uppercase, tracked 0.3em, centered on y 880.
- Premium: true copperplate construction, shades only on downstrokes, hairlines so fine they nearly vanish, ink that pools and dries. Cheap: a script font revealed by a left-to-right wipe, a uniform-width line, sparkles.
Banned: script fonts for the signature, uniform-width strokes, wipes or clip reveals, ink splatter, glitter, wax seals, roses, blur transitions, fast cuts, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.6s: paper under the lamp; the pen descends into frame from the upper right, its shadow sharpening as the nib nears the paper.
- 0.6–1.8s: the capital E: entry hairline, top loop, a shaded spine swelling and thinning, the bottom oval ending in a small pool.
- 1.8–3.4s: "loise" in one connected run, hairline up and shade down; the i is left undotted.
- 3.4–3.7s: the pen lifts and travels to the H.
- 3.7–5.0s: the H's two shaded stems and looped crossbar, then "art" joined; the t's stem stays uncrossed.
- 5.0–5.4s: the pen dots the i, leaving a round pool, and crosses the t with a hairline that ends in a tiny bead.
- 5.4–5.9s: the swash: a long underline from beneath the E to past the t, with one shaded swell near its middle, ending in a hairline.
- 5.9–6.4s: the pen lifts away to the upper right, its shadow softening; the complete signature reads, its last strokes still wet.
- 6.4–7.6s: the last wet highlights dry off; the line beneath and the small caps line fade up 0.3 s apart, rising 6px.
- 7.6–10.0s: hold, completely still.
For other lengths, scale the pen speeds and keep every stroke in order; keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the awaited loads matter. No libraries.
- At load, sample every stroke at 1px steps with its width, pressure and arrival time from the speed rules, and render the paper once; seek(t) draws the ink deposited up to t (with drying from each sample's age), then the pen and its shadow at their positions for t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check shades fall only on downstrokes, every downstroke shares the 55° slant, hairlines stay visible at 1280×720, the i is dotted and the t crossed, pools appear only where the pen stopped, the 6 s frame shows the whole signature with the pen clear of it, and the letters read as Eloise Hart. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
