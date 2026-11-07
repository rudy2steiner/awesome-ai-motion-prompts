# Batik

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/batik-wax-resist) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/batik-wax-resist)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** motion-studies
- **作品发布时间：** 2026-10-19
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second batik film, seen from above: hot wax lines are drawn on cotton with a canting, the cloth goes through three dye baths with more wax laid between them, and the cracked wax is boiled away to reveal layered color.

<inputs>
If I don't give you something, use the default and don't ask.
- Studio: Rumah Batik Kembang Gede (fictional).
- Title: "Drawn in wax"
- Line: "Batik tulis: hot wax by hand, then yellow, indigo and soga brown, one bath at a time."
- Layer key: Ivory, waxed first · Yellow, bath 1 · Green, yellow under indigo · Brown, all three baths
- Design: an original long-tailed bird among five flowers and leaf sprays, a border of tumpal triangles, a ground of dots.
- Length: 10 seconds.
</inputs>

<direction>
- Look: a daylight time-lapse straight down on a cotton cloth stretched over a teak frame: wax lines glisten as they are drawn, the cloth changes color bath by bath, and each new color reaches only what the wax left open.
- Palette: studio floor #2A1E16 around the frame; frame teak #7A5232 with grain #5E3E25; cloth ivory #F3EBD8 with a fine plain weave; pencil #9C9488 at 40%; hot wax amber #E2A93C, translucent and glossy, cooling to matte #EAD9A2; yellow #E3B23C; indigo #2C4C8A; green #3F6B45, which is yellow under indigo; dark brown #2B2117, all three baths; crackle veins in the area's own color under the soga filter (#7A4A2A on ivory, #6E5222 on yellow, #2F3A26 on green); steam #FFFFFF at 12%; type #F3EBD8, secondary #D9C9A8, accent #E3B23C.
- How the colors interact: model each bath as a filter, color = ivory × every bath a pixel took, so green is literally yellow under indigo and the last bath turns every open area a deep brown that makes the earlier colors glow; ivory lines run through every stage; veins are the last bath seen through cracks, darkest across the light areas.
- The cloth: 1560 × 790 at x 180–1740, y 110–900 at 1.0×, inside the teak frame. The design is original and drawn freehand, not a copy of any named traditional pattern:
  - along the left edge, a border of nine tumpal triangles, each 130px wide, with a leaf inside;
  - in the center right, a crested long-tailed bird turning its head back: body 260px long, wings with three rows of feathers, a scale pattern on its breast, and five ribbon tail feathers sweeping 620px in an S, each ending in an eye spot;
  - five flowers 120–200px across, each with 8–12 layered petals and a dotted center, on curving stems with sprays of leaves (each leaf with a center vein and side veins);
  - a ground of cecek dots in staggered rows 22px apart filling every open space.
  Every outline is a wax line 4–6px wide that wobbles slightly and swells where the hand slowed; the isen fills (fine stripes in the petals, dotted leaf halves, scales on the bird) are wax too.
- Wax passes:
  1. the canting draws every outline, the isen fills and the ground dots (these stay ivory);
  2. a brush fills the flower centers, the bird's crest, the tail's eye spots and the tumpal leaves (these stay yellow);
  3. a brush fills every leaf, the bird's body and wings and the tail ribbons (these stay green).
  Whatever is still open after pass 3, the ground between the dots and the tumpal backgrounds, ends dark brown.
- Tools: the canting, a copper bowl 26px across with a curved spout on a bamboo handle running out of frame to the lower right, casting a 10px shadow; a brush with a bamboo handle and a wax-dark tip. Both travel between strokes on easeInOutSine and draw at a steady speed. New wax is amber and glossy, with a moving specular streak, and cools to matte pale over 0.4 s behind the tool.
- Baths: each bath is a wet front that crosses the cloth from top to bottom over 0.4 s; behind it the dye's color rises in every open area with a wet sheen (12% specular) that dries off over 0.6 s; on wax, the dye beads into small drops that roll off and fade.
- Crackle: after pass 3 the cloth is crumpled and smoothed again: soft crumple shading rises and relaxes over 0.3 s, and a network of fine cracks (seeded and Voronoi-like, 1px, denser across large waxed areas) opens through every waxed area. The last bath seeps into them as veins.
- Lorod: hot water lifts the wax from the center outward in a ring that grows over 0.9 s; behind it the wax's gloss and pale tint vanish and the colors underneath come up crisp, with a few wisps of steam rising and fading.
- Camera: straight down. It opens at 2.0× on the bird's head as the canting starts, eases out to 1.0× by 1.6 s, drifts 20px through the middle, and from 6.6 s eases to 0.92× with the cloth centered at (960, 470), so the frame edges, the key and the type fit around it.
- Layer key (HTML, from 6.6 s): right-aligned to x 1800 on baseline 1000, four entries, each a 26px swatch in its final color and its label in Plus Jakarta Sans 500, 20px, secondary, rising in 0.15 s apart.
- Type (HTML over the canvas): kicker "RUMAH BATIK KEMBANG GEDE" in Plus Jakarta Sans 700, 20px, tracked 0.16em, accent, on baseline 890; title Plus Jakarta Sans 800, 60px, #F3EBD8, on baseline 950; line Plus Jakarta Sans 500, 24px, secondary, on baseline 1000; all from x 120, on the dark floor below the cloth. Text rises 12px as it fades in over 0.6 s on cubic-bezier(0.22, 1, 0.36, 1).
- Premium: a true resist order (each color kept only where wax went on before the next bath), green made from yellow under indigo, glistening wax that cools matte, crackle veins and a crisp reveal. Cheap: a pattern fading in through colored filters, vector lines, colors that appear without a bath.
Banned: colors appearing without a bath, vector-crisp lines, wax or dye drawn as smooth gradients, neon colors, glitter, hands or people, wayang figures, national emblems or religious motifs, copies of named traditional patterns, glow, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.3s: close on the pencil drawing of the bird's head; the canting arrives.
- 0.3–1.9s: the canting draws the outlines and isen fills in hot wax as the camera eases out; the ground dots stipple in, rows at a time.
- 1.9–2.4s: bath 1: yellow rises behind the wet front.
- 2.4–3.0s: the brush waxes the flower centers, the crest, the eye spots and the tumpal leaves.
- 3.0–3.5s: bath 2: indigo turns every open yellow area green.
- 3.5–4.1s: the brush waxes the leaves, the bird and its tail.
- 4.1–4.4s: crumple: cracks run through all the wax.
- 4.4–4.9s: bath 3: soga brown darkens the ground and seeps into the cracks.
- 4.9–5.8s: lorod: the wax lifts away from the center out and the colors come up crisp.
- 5.8–6.6s: the finished cloth, still (the 6.0 s frame: no wax left, every color and vein visible).
- 6.6–7.6s: the camera eases out; the layer key builds swatch by swatch.
- 7.6–8.4s: the kicker, title and line rise in.
- 8.4–10.0s: hold.
For other lengths, stretch the waxing passes; keep the order and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas: one WebGL canvas (preserveDrawingBuffer: true, drawn once per seek), its backing store sized from CSS size × devicePixelRatio, whose fragment shader computes each pixel's color from prebuilt textures (the three wax masks with their arrival times, the crack network, the weave) and the closed-form bath, crumple and lorod fronts; the frame, the tools and the steam on a 2D canvas above it. Text is HTML over the canvas.
- Wax arrival times follow the tools' paths and are computed once at load; a pixel's color is the stack of baths that reached it before wax did, so any frame is direct.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check every stage obeys the resist (each waxed area keeps the color it had when it was waxed), green appears only where yellow met indigo, veins appear only in cracked wax after bath 3, wax appears only where a tool has passed, lines wobble and swell like hand-drawn wax at 1280×720, the bird and flowers read clearly, the 6.0 s frame is the finished cloth with no wax, and the type stays on the floor clear of the cloth. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
