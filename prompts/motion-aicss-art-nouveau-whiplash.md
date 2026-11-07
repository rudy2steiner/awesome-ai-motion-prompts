# Art Nouveau

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/art-nouveau-whiplash) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/art-nouveau-whiplash)

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
Make a 10-second Art Nouveau poster in the manner of an 1890s Paris lithograph: whiplash stems grow into a floral frame around a haloed iris and a hand-lettered title.

<inputs>
Title: The Iris Show. Venue: Wrenmoor Glasshouses. Dates: 3–18 May. Line: "Come in from the rain." Flower: the bearded iris. Duration: 10s. If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Palette, as flat lithographic inks: paper #F0E6CD, sage #A4B394, deep sage #61765A, olive #3F4A31, gold ink #C39A48 with a lighter gold #DDBE78 for inner rims, iris violet #8E7AA0, deep violet #5F4E73, pale lilac #C7B9CF, outline brown #3B2F24. No black, no white.
Lithograph texture: a seeded crayon-tooth grain at 5% multiplied over everything, and each color sits 1–2px off its outlines (a fixed seeded offset per ink), so slivers of paper show along a few edges, as on a stone printed one ink at a time.
Line is the style. Every contour is an outline-brown line whose weight swells and thins, never a uniform stroke: about 7px through the long runs of the stems, 2px at tips and in small details, swelling to 10px on the outside of tight curls. Draw each line as a filled shape: sample its centerline (cubic Béziers joined with matching tangents, so there are no kinks) and offset it by half the width profile w(s) on each side.
Composition, symmetrical about x 960 in structure but not in detail:
- the frame: a 4px outline-brown rule inset 70px with 28px rounded corners, and a 2px gold rule 10px inside it;
- the halo, centered at (960, 430): an outer gold ring 16px wide at radius 320 with a lighter gold inner rim, a band of 48 small paper-colored circles outlined in brown between radius 282 and 304, then a sage disc holding 36 lancet-shaped rays in alternating sage and deep sage, all within radius 270;
- the hero iris in front of the halo: a stem rising from y 770, two sword leaves crossing behind the bloom, and a bloom 360px tall centered at (960, 380): three upright standards in pale lilac with violet veins, three falls curving down and out in violet with deep violet veins and a gold beard, every petal edge ruffled by a low-amplitude sine;
- two whiplash stems, one from each bottom corner of the frame: each rises up its side in a long S, snaps inward into a tight spiral of two turns (thinning to a hairline at its center) at about (300, 220) and (1620, 220), and carries three long leaves and two smaller irises on side shoots; the left and right stems differ in leaf placement and spiral direction;
- a title panel, 1240×150 centered at (960, 845), with half-round ends, sage fill and the outline rule, overlapping the base of the hero stem.
Type: "Federant" 400 for the title, uppercase, each letter placed individually so the line fills 1120px of the panel and stretched vertically 1.12× like drawn lettering, in outline brown; the T and the W end in drawn whiplash swash tails (tapered paths) that curl into the panel's ends. "Marcellus SC" 400, 30px, tracked 0.18em, outline brown, for one line beneath the panel at baseline 962: Wrenmoor Glasshouses · 3–18 May · Come in from the rain.
Motion is growth. Lines extend along their length from root to tip, slowing as they enter a curl, on cubic-bezier(0.3, 0, 0.1, 1) over 1.6–2.2s, the tapered tip always leading. Leaves unfurl from their base along their axis (scale 0 → 1 with 12° of rotation settling to rest) over 0.6s, starting as the stem tip passes. Petals open from a closed bud on cubic-bezier(0.25, 0.8, 0.25, 1) over 0.9s. Rings draw clockwise from 12 o'clock. Nothing bounces, and nothing but the frame rules moves in a straight line.
The real thing is one unbroken line with living weight, flat litho color held inside it, and ornament obeying a symmetrical frame; the cheap version is clip-art vines and a script font on parchment.
Banned: script or brush fonts, parchment or photo textures, gradients, drop shadows, glow, uniform-weight strokes, roses or hearts, Art Deco motifs (sunbursts, chevrons, stepped frames), pure white or black, a human figure, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–0.6s: bare paper; the frame rules draw from the bottom center outward along both sides and meet at the top center.
0.6–2.6s: the two whiplash stems grow from the bottom corners up the sides and snap into their spirals; their leaves unfurl behind the tips.
1.4–3.2s: the halo: the gold ring draws clockwise over 0.9s, the 48 circles appear around it 15ms apart, and the 36 rays fan open from vertical.
2.8–4.4s: the hero iris: its stem rises, the sword leaves unfurl, and the bud opens, falls dropping out and down as the standards lift.
3.6–4.8s: the four side buds open into small irises, 0.3s apart.
4.4–5.4s: the title panel draws outward from its center and its sage fill floods in behind the line; the title letters ink in from the center letter outward, 50ms apart, each rising 8px.
5.4–5.9s: the swash tails draw and the line beneath sets letter by letter.
5.9–7.4s: small gold seed beads run along both stems from root to spiral; the halo's rays turn 4° and come to rest; the leaves sway once (±1.5°) and settle.
7.4–10.0s: hold, completely still.
For other durations, scale every timestamp proportionally.
</structure>

<build>
One self-contained index.html, CSS and JS inline. Google Fonts via <link> are fine; no other libraries (no three.js: this style is flat). Draw in inline SVG: each tapered line is a filled path built once at load from its sampled centerline and revealed by a mask whose thick stroked centerline animates stroke-dashoffset, with the tip's taper applied at the reveal point. Generate the crayon grain once at load into a canvas laid over the SVG with mix-blend-mode: multiply. Await document.fonts.load() for each face, then define window.seek. The stage is 1920×1080 (16:9), scaled to fit the window. Design for 60fps. window.seek(t), t in seconds, must compute every visual from t alone: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, and randomness only from a seeded PRNG. Anything cumulative is precomputed once at load at a fixed step or solved analytically from t, so any frame can be drawn directly. Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text, accidental edge collisions, and anything off-style or Banned. Check every stem reads as one continuous line that swells and thins with no kinks at segment joins, the growing tip stays tapered (never a blunt cap), the iris reads as an iris (three standards up, three bearded falls down), the structure is symmetrical while the plants differ, and the title reads cleanly on its panel. Confirm seek(duration) and seek(duration + 1) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
