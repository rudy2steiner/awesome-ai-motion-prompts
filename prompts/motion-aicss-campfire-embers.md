# Campfire

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/campfire-embers) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/campfire-embers)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** 3d-simulations
- **作品发布时间：** 2026-10-18
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second campfire at night: flames lick up from charred, glowing logs, embers rise and wink out, and the firelight moves on the forest around it.

<inputs>
If I don't give you something, use the default and don't ask.
- Title: "Ember Hours"
- Line: "Stories told by the fire · Episode 9"
- Fire: a split-log teepee over a bed of coals in a ring of stones; one log settles at 5.2 s.
- Length: 10 seconds.
</inputs>

<direction>
- Palette: canopy gaps #0D1424 with a few faint stars; deep forest #0A0C0B; moonlight on the far side of things #2C3A55; bark under firelight #8A4A26 falling to #3A1E12; leaf litter #2B1A10 lit to #7A4422; stones #5B5550 lit #B07A55; char #1B1512; coals #FF5A1E with hot seams #FFB347; flame ramp by temperature: core #FFF3C4, yellow #FFC24A, orange #FF7A1A, red #D6361B, then smoke #2A2420; a hint of blue #3A6BFF at the very roots of the flames; embers #FFD27A cooling to #FF4E1A; title #F6E7D2, line #C9A98A.
- Camera: seated at the fire, eye height about 1 m, looking slightly down; the coal bed at (1040, 780), the stone ring an ellipse 560 × 160px around it, the ground falling away into the dark.
- Fire construction: four split logs lean into a teepee over the coals and two whole logs lie on the ground beside it, 18–26 cm thick. Each log shows ridged bark (#3E2A1E with lit ridges), pale split faces where it hasn't burned yet, end grain with growth rings on the cut ends, and charred sections cracked into alligator char: a Voronoi network of 14–30px cells whose 1.5–3px seams glow coal-orange, each cell breathing on its own slow sine (0.3–0.7 Hz). The coal bed is about 40 lumps (20–60px) with grey ash skins on top and hot gaps between. Eleven rounded stones, soot-dark on their inner faces, lit warm on top.
- Flames, in a WebGL fragment shader over a 560 × 600px region rising from the coals: a temperature field T = envelope × (1.1 − height) + (domain-warped fBm − 0.5) × 0.9, the fBm (4 octaves) scrolling upward at about two flame heights a second, the envelope a teardrop leaning with the breeze and split into 3–5 tongues by a horizontal noise. Map T through the ramp with soft edges (smoothstep width 0.08) and add it over the scene. Tongues stretch, pinch off into flamelets that shrink and vanish near the top, and the whole flame puffs about twice a second, the rhythm of a real fire this size. Above it, heat shimmer offsets the background by at most 3px, and thin smoke rises, lit orange underneath, drifting right and thinning out by y 150.
- Firelight: build the forest, ground, stones and logs once at load as an albedo layer plus a mask of how much each pixel faces the fire. Each frame multiplies them by the firelight I(t) × 1 ÷ (1 + (d ÷ 420px)²), with I(t) = 1 + 0.05 sin(2π·0.9t) + 0.04 sin(2π·1.4t + 1) + 0.03 sin(2π·1.9t + 2), plus a 10% swell at the log settle that decays over 0.8 s. The light's center wanders ±10px with the flames. Add a 12% cool moonlight term so the far sides of trunks read as blue silhouettes, not black.
- Forest: three layers of conifer trunks: near trunks cropped by the frame edges (120–220px wide, deep vertical bark furrows lit warm on the fire side), thinner mid trunks, and far trunks that are almost silhouettes; low ferns by the stones; a canopy of dark needles across the top with gaps showing deep blue sky and a few stars. The light dies into darkness about 1,100px from the fire.
- Embers: about 600 over the piece, plus a burst of 24 when the log settles. Each leaves the coal bed at 220–480px/s upward, held up by buoyancy that drag slowly bleeds off, is carried right and swirled by a seeded curl-noise breeze, shrinks from 3.5px to 1.5px, cools from #FFD27A to #FF4E1A, and winks out over 0.1 s at its own lifetime (0.8–3.0 s), a few drifting out of the top of the frame. Draw each as a hot core, a short streak along its velocity and a small additive glow. Precompute them once at load at a fixed 1/60 s step from t = −3 s; the breeze keeps them out of the title zone (x 100–860, y 80–300).
- The log settle at 5.2 s: one teepee log slips 6px and turns 2°, the fountain of sparks lifts, and the flames flare 15% for 0.6 s.
- Type (HTML over the canvas): title in Fraunces (opsz 144, weight 600, SOFT 100), 112px, #F6E7D2, baseline at (120, 220) over the dark canopy; line in Public Sans 500, 24px, uppercase, tracked 0.18em, #C9A98A, beneath. Each rises 12px as it fades in over 1.0 s on cubic-bezier(0.22, 1, 0.36, 1).
- Premium: a white-hot core, tongues that tear into flamelets, glowing seams in cracked char, embers that cool and die at different heights, light that falls off into the trees. Cheap: an orange gradient blob, particles shot out of a cone, the whole frame flickering.
Banned: cartoon flame outlines, emoji, marshmallows, tents or people, light on the surroundings swinging faster than 2 Hz, full-frame flicker, lens flares, smoke over the title, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: the fire already burning (everything started at t = −3 s): flames puffing, embers rising, the near trunks warm and the forest dark beyond.
- 1.0–3.2s: a light breeze leans the flames 6° to the right and carries the embers with it; the camera begins a 4% push-in toward the fire on easeInOutSine.
- 3.2–4.6s: the title rises in, then the line 0.3 s later; smoke wisps climb toward the canopy.
- 4.6–5.2s: a steady burn, the seams in the char breathing.
- 5.2–6.6s: the log settles: a fountain of sparks climbs high into the dark, and the light swells on the trunks and decays.
- 6.6–8.6s: the breeze drops; the flames stand up straight; the embers return to a calm rate; the push-in ends.
- 8.6–10.0s: hold the composition: camera and type still, only the fire, embers and smoke moving.
For other lengths, stretch 1.0–4.6s and 6.6–8.6s; keep the log settle and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas: one WebGL canvas (preserveDrawingBuffer: true, drawn once per seek) that composites the prebuilt albedo and firelight-mask textures and draws the flames, shimmer and smoke in fragment shaders, with a 2D canvas above it for the embers in 'lighter' compositing; backing stores sized from CSS size × devicePixelRatio. Text is HTML over the canvas.
- The forest, logs, stones and char network are drawn once at load into offscreen canvases; the flame field and firelight are closed-form functions of t; embers are read from the precomputed arrays.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the flames have a near-white core at their roots and break into separate flamelets at the top, the char seams glow, embers die out at different heights, the trunks read in every frame, and the title zone stays clear of embers and smoke. Sample a trunk's average brightness at 30 fps and confirm no swing over 5% happens more than twice in any second. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
