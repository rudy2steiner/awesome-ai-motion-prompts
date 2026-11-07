# Felt Stop-Motion

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/felt-stop-motion) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/felt-stop-motion)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** characters-stories
- **作品发布时间：** 2026-10-16
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second felt stop-motion opening for a children's show: a hand-stitched felt hillside comes together on twos, the sun rises, and a small felt rabbit hops out under the title.

<inputs>
- Show title: "Bobbin Knoll" (a fictional children's show).
- Subtitle: "Stories stitched by hand".
- Details tag: "Weekdays at 4".
- Character: Moss, a small felt rabbit.
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Set: a tabletop felt diorama shot straight on, in layers from back to front: a sky backing #8CC3E6; far hills #7FB86A; a middle hill #5FA650; a near hill #4C9A47 with a round 120px burrow door (#3B2A20 felt, a wooden button knob) at (1240, 790); a foreground strip of grass tufts #3E8A3C with three felt flowers (petals #F5A3C0, centers #FFD24A). Sun: a 220px #FFC83D disc with twelve rounded rays cut from #FFB02E. Two scalloped clouds in #F8F4EC. Embroidery threads: cream #FFF6E0, rust #C2562E, navy #2E3A63, pink #F48FB1.
Felt is the soul. Each color gets a fiber texture generated once at load: about 4,000 short curved hairs (4–12px long, 0.6px wide, ±8% lightness) over the base color. Each piece is clipped to its shape and gets a fuzzy edge (a 1.5px soft edge plus a stray fiber poking 2–5px outward every 6px or so), pillowing (a 12px inner shade at 15% along the edge, so the felt reads 3mm thick) and a soft shadow on the layer below, rgba(40, 30, 20, 0.25), its offset and blur growing with depth from 4px/8px at the back to 10px/16px at the front.
Stitches: running stitches (10px stitches, 7px gaps, 3px thread) in a contrasting thread around the clouds, sun and hills, and blanket stitch around the burrow door. Each stitch is a capsule with a lighter center line for the twist and a small dark dimple at each end where it enters the felt. Buttons are shiny two-hole discs with a radial highlight, sewn on with a thread cross.
Moss: about 200px tall sitting, with a cream felt body and head (#F4EDE0), long ears with pink inner pieces (#F7B6C2), a black button eye, a pink felt nose, a two-stitch navy mouth and a pom-pom tail of loose fibers. Head, ears, body, front paw and hind leg are separate felt pieces joined by visible stitches, so they pivot.
Motion on twos: every animated value uses tq = floor(t·12)/12, so the picture changes 12 times a second. Each step gives every piece a tiny replacement jitter (±0.5px, ±0.25°) seeded by (piece, step), and the set's light varies ±1% per step. Moves use easeInOutQuad with held extremes; a hop is four drawings (crouch with squash 0.9, launch with stretch 1.1, airborne, land with squash 0.92). Clouds drift 18px/s; only the sun's rays turn, 10°/s.
Camera: locked off like a tabletop rig, with a slight depth of field: the sky and far hills blurred 2px, the near hill and Moss sharp.
Type: the title is cut from rust-orange felt (#E8743B). Render "Bobbin Knoll" in Sniglet 800 at 130px, fill the glyphs with that felt's texture and fuzzy edge, and run a cream running stitch just inside each letter's outline (a dashed stroke along the glyph outline, clipped to the letter). It sits on a cream felt banner (#FFF6E0, about 760×250px, pinked zigzag edges) hanging from two navy threads at the upper left, x 160–920, y 120–370. The subtitle is printed on the banner under the title in Sniglet 400, 34px, navy. The details sit on a small pink felt tag (Sniglet 400, 28px, navy) stitched to the near hill at the lower left.
Premium: thick, fuzzy felt with real fiber, contrasting hand stitches with tiny dimples, warm soft shadows, and stepped motion with a little boil. Cheap: flat vector shapes under a noise filter, smooth tweens, perfect edges.
Banned: smooth unstepped motion, motion blur, hard vector edges, glossy highlights except on buttons, gradients except shadows and pillowing, outlines (stitches are not outlines), existing characters, emoji, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: the far, middle and near hills are placed one at a time from above, each arriving lifted (a large soft shadow) and settling as its shadow tightens.
- 1.2–2.4s: the sun rises from behind the far hills in steps, its rays turning; the clouds slide in from the edges.
- 2.4–3.6s: three flowers pop up in the foreground, each in three drawings (bud, half, open).
- 3.6–5.0s: the burrow door swings open on its left edge (scaleX 1 → 0.2 in steps); Moss's ears peek out, then the head; a blink (a felt eyelid covers the button for two steps).
- 5.0–6.6s: Moss hops out twice to the left and lands at x 1000 on the near hill; the tail fluff bounces.
- 6.6–8.0s: the banner drops in on its threads, swings ±4° and settles in decaying steps.
- 8.0–8.6s: Moss waves a paw twice (a four-drawing cycle); the details tag is placed.
- 8.6–10.0s: hold: the clouds stop, the jitter halves, everything else is still.
Other lengths: scale proportionally but keep 12 steps per second.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative (growth, simulation, particles) is precomputed once at load at a fixed step or solved analytically, so seek can jump to any time. Past the end, hold the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link>; await document.fonts.load() for each face before assigning window.seek.
- Engine: Canvas 2D. Fiber textures, stitch sprites and the blurred back layers are built once at load from a seeded PRNG; seek composes the frame from them.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that the 12-per-second stepping is visible, fuzzy edges and stitches survive at 1280×720, shadows are soft and warm, the title reads clearly, Moss sits on the hill (not floating) after each hop, and nothing looks like paper or flat vector. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
