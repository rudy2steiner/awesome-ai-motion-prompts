# Anaglyph 3D

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/anaglyph-3d-title) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/anaglyph-3d-title)

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
Make a 10-second red-cyan anaglyph title sequence in the manner of a vintage 3-D comic: a night farm, a swarm of moths, a block-letter title and a giant moth come toward the viewer, every element printed twice in red and cyan at the offset its depth calls for.

<inputs>
If I don't give you something, use the default and don't ask.
- Opening card: "PUT ON YOUR 3-D GLASSES NOW!"
- Presenter: "VISTAROMA PICTURES PRESENTS" (fictional)
- Title: "INVASION OF THE" over "MOON MOTHS"
- Tagline: "They came for the porch lights!"
- Burst: "IN 3-D!"
- Length: 10 seconds.
</inputs>

<direction>
- Look: a 1950s 3-D comic printed in two inks on cheap newsprint. Everything exists twice, a cyan copy and a red copy, offset by its depth, with bold brush inking and dot tones. Through red-cyan glasses (red over the left eye) it stands off the page; without them it still reads as a handsome two-ink comic title.
- Paper and inks: newsprint #F2E8D2 with seeded fibers, a few foxing spots and one faint fold; cyan ink #1FB0D8; red ink #E8343F. Both print with multiply, so where they overlap they make a near-black navy #1C2435, and anything on the page plane reads as clean dark ink. Only the two inks and the paper appear.
- The stereo rule, exact: every element is a flat card at a depth d, measured as screen disparity in px (d = 0 on the page, d > 0 toward the viewer, d < 0 behind the page). The left-eye view prints in cyan with the card shifted +d/2 in x; the right-eye view prints in red, shifted −d/2. So a card in front of the page shows its cyan copy to the right of its red copy, and a card behind it the reverse. A card also scales with depth, scale = 1 + d/230, so it grows as it comes forward. Keep d within −24 to +60; type stays within −8 to +24 so it reads without glasses. The camera truck moves each card by −truck × scale, so near cards slide farther than far ones.
- Printing: draw the left-eye scene and the right-eye scene separately, each on its own opaque white offscreen canvas in black ink, cards back to front at their own offsets, with each card's paper areas filled white so they hide what's behind them. Turn each into its ink by filling the ink color over it with 'screen' compositing (black becomes the ink, white stays white), then multiply both onto the paper. Mid-tones are dot tones, never flat tints: dots on a 7px screen, angled 15° in the left-eye drawing and 75° in the right-eye drawing, so where tones overlap they moiré into small rosettes like old comic printing. Solid blacks are solid in both.
- Inking: bold brush lines 3–8px that taper at their ends (each drawn as a filled shape from a centerline and a width profile), solid black shadows, and dot tones for the moon, the sky and the wing patterns.
- The cards, their places and depths (positions are where they sit in the final frame, after the truck):
  - sky: stars as small four-point crosses and dots, and a huge full moon (radius 220) at (1440, 300) with its maria and craters in dot tone, all at d −20;
  - distant hills: a silhouette ridge with dot-tone haze at d −12;
  - the farm on the near hill, d −4 to 0: a clapboard farmhouse at x 180–460, y 760–960 with a porch and a hanging porch lamp at (440, 820) whose glow is drawn as tapered ink spokes, a water tower, a barn further right on the ridge and a picket fence;
  - foreground, d +8: a mailbox on a post at the lower right (x 1700–1780, y 880–1010) and grass tufts along the bottom;
  - small moths: 14 moths 40–70px across, wings in dot tone with an eyespot each, at d −20 as they leave the moon and d −2 to +6 as they circle the lamp, staying within x 160–560, y 770–950, below the title;
  - "VISTAROMA PICTURES PRESENTS" at d 0, centered at y 960, like a comic's credit line;
  - "INVASION OF THE" at d +8, centered at y 470;
  - "MOON MOTHS" across y 560–760: block letters whose front faces sit at d +22, each with an extruded side face of six stacked slices stepping back to d +10 and 3px down-right per slice; the front face solid, the side faces in dot tone, a thick ink outline round each letter;
  - the tagline at d +4, centered at y 870;
  - the hero moth, 620px across at its closest, hovering at the upper left centered at (500, 255) and never touching the title: forewings and hindwings as separate shapes with scalloped edges, dot-tone bands, an eyespot of concentric rings on each hindwing, a furry body in short hatch strokes and two feathery comb antennae;
  - the "IN 3-D!" burst: a 16-point starburst 320px across at (1500, 270), its fill paper, an ink outline and a solid ink drop shadow, the words inside in two lines.
- Motion: cards move in depth on easeOutCubic when coming forward and easeInOutSine when drifting, their scale and cyan-red separation changing together with d. Nothing changes depth faster than 80px of d per second except the burst's slam (0.2 s). The hero moth's wings beat at 2.2 Hz (each wing foreshortens and rotates about the body from a closed-form angle), easing to a spread pose by 8.2 s; the small moths loop around the lamp on seeded closed-form paths, wings beating at 5 Hz; the lamp's spokes turn slowly; a camera truck of 120px to the right runs across the whole piece on easeInOutSine.
- Type: the opening card in Bangers 400, 84px; the presenter in Alfa Slab One 400, 40px, tracked 0.08em; "INVASION OF THE" in Bowlby One 400, 64px; "MOON MOTHS" in Bowlby One 400, 200px; the tagline in Bangers 400, 56px; the burst's words in Bowlby One 400, 64px.
- Premium: every element printed twice with an offset that follows its depth exactly, inks and dot tones that look printed, depth that changes in motion, and a title that reads cleanly with or without glasses. Cheap: an RGB-split glitch filter, the same offset on everything, a third color, flat tints instead of dots.
Banned: RGB-split or chromatic-aberration filters, glitch effects, one uniform offset, colors beyond the two inks and the paper, gradients, glow, photo textures, disparities outside −24 to +60px, real films, studios or characters, gore, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: the newsprint; the opening card prints on the page plane (d 0, so it reads as clean dark ink): a pair of cardboard 3-D glasses drawn in ink above the words; the glasses bob once.
- 1.2–2.4s: the card sinks behind the page (d 0 to −24), shrinking away, as the night prints in behind it: the moon and stars, the hills, the farm and its lamp, the foreground; the truck is under way.
- 2.4–3.8s: the small moths spiral out of the moon toward the porch lamp, growing as they come, and start to circle it; the presenter line prints at the foot of the page.
- 3.8–5.4s: "INVASION OF THE" rises from behind the hill to d +8 (3.9 s); MOON MOTHS flies up letter by letter, 0.1 s apart from 4.2 s, each letter from d −12 to its front at d +22, settling with a 1.04 to 1 scale.
- 5.4–6.0s: the tagline prints at d +4. The 6.0 s frame is complete: the night farm, the circling moths and the whole title.
- 6.0–7.6s: the hero moth flies out of the moon toward us, growing from d −20 to +56 with its wings beating, and comes to hover at the upper left.
- 7.6–8.4s: the burst slams forward from d 0 to +36 at the upper right and wobbles ±2° once.
- 8.4–10.0s: hold: the hero moth rests with its wings spread; only the small moths circle the lamp.
For other lengths, stretch the moth swarm and the hero moth's approach; keep the title's timing and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the awaited loads matter.
- Every card's depth, position, scale and wing angle is a closed-form function of t; each frame redraws both eye canvases from scratch, inks them and multiplies them onto the paper, which is generated once at load. Build the dot-tone patterns and the paper texture once at load.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Pick three cards at different depths in several frames and confirm the cyan copy sits exactly d px to the right of the red one (to the left for cards behind the page) and page-plane items line up exactly; check MOON MOTHS and the tagline read at a glance without glasses, only the two inks and the paper appear, dot tones show as dots with rosettes where they overlap, the hero moth reads as a moth and never covers the title, and no disparity leaves −24 to +60px. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
