---
title: "Snow Globe Animation Prompt for Claude | AI CSS Animations"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/snow-globe"
license: "CC0"
collected: "2026-11-03"
---

# Snow Globe Animation Prompt for Claude | AI CSS Animations

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/snow-globe](https://www.aicssanimations.com/directory/Motion-Prompts/snow-globe)  
**License:** CC0

## Prompt

```
Make a 10-second tabletop film of a glass snow globe with a tiny village inside: it rocks, the snow swirls up in a vortex, then drifts down and settles on the roofs.

<inputs>
If I don't give you something, use the default and don't ask.
- Title: "Holmcrest"
- Line: "Winter Market · 6–22 December" (fictional)
- Plaque on the base: HOLMCREST
- Village: five houses, a chapel with a clock steeple, seven fir trees, a lamp post, and a frozen pond with a footbridge.
- Length: 10 seconds.
</inputs>

<direction>
- Look: a product shot at blue hour: cool daylight from a big window on the left, a warm lamp from the right, the globe on a pale oak table, the background soft and out of focus.
- Palette: backdrop #3A4E6E at the top to #6E819C behind the globe; oak #C8A27A with grain; walnut base #4A2F22, satin; brass plaque #C9A45C; water tint #EAF4FF; snow #FFFFFF with blue shadows #C5D3E3; plaster walls cream #EFE3CC, brick red #A8473A and sage #8FA58A; slate roofs #4C5664 under snow #F4F6F8; timber #5B3B2A; lit windows #FFC870; firs #2F5A45; pond ice #B8CFE0; title #F2F4F8, line #C4CEDC.
- The globe: a sphere of radius 1.0 set in a collar on a turned walnut base (LatheGeometry: foot radius 1.05, a cove, a bead and a fillet, 0.55 tall), with the brass plaque engraved HOLMCREST on its front. Model the glass and water as one transmissive sphere (MeshPhysicalMaterial: transmission 1, ior 1.2, thickness 1.0, roughness 0.02, attenuation #EAF4FF at distance 6), so the village shows clearly, slightly magnified, and the table edge behind bends through it. Over it, a shell at radius 1.004 carries the reflections: transparent, roughness 0, a strong clearcoat and Fresnel, showing the window as a crisp rounded rectangle at upper left and a warm highlight on the right edge.
- The village on a snow mound (a dome of radius 0.75 filling the lower half): five houses (box bodies with rounded edges, pitched roofs with overhanging eaves, chimneys, doors, and two to four lit windows each with mullions), a chapel with a steeple and a clock face, seven firs (stacked cones with snow loads on each tier), a lamp post with a small warm PointLight, and a frozen pond with a little arched footbridge. Houses stand 0.12–0.18 tall. Window light falls warm on the snow around them.
- Light: build an environment once with PMREMGenerator.fromScene from a small room: a big cool window panel (#DCE8FF, intensity 4) on the left, a warm lamp panel (#FFC88A) on the right, a dim floor. Key: a cool DirectionalLight from the upper left (intensity 2.2, soft shadows, PCFSoftShadowMap, 2048 map) for the base's soft contact shadow; a warm SpotLight low from the right; HemisphereLight fill at 0.6. ACESFilmic, exposure 1.1. A soft, bright spot of focused light lies on the table on the far side of the globe from the key, as a water-filled sphere throws (an additive elliptical decal at 25%). Everything is clearly lit from the first frame.
- Snow: 3,000 flakes (flat and irregular, 0.006–0.014 across) as an InstancedMesh, white with a little emissive so they never go grey, each tumbling at 0.3–1.2 turns a second so it catches the light. Simulate once at load at a fixed 1/120 s step from t = −2 s: each flake's velocity relaxes toward the water's velocity with a 0.15 s time constant while it sinks at 0.05 units/s; after the rocking, the water swirls about the vertical axis (6 rad/s, decaying as e^(−t ÷ 1.6 s)) and rolls up the middle and down the walls, which decays faster; flakes stay inside radius 0.97, and any flake that touches the mound, a roof or a fir (simple dome, box and cone tests) stops and stays. At the start most flakes rest on the mound and roofs.
- The rocking: the globe tips and rocks on its base three times at 2.2 Hz (tilt ±9°, slide ±0.12), as if nudged by an off-screen hand; the water lags behind the glass, lifting the settled snow into the swirl.
- Camera: fov 30, a three-quarter view 12° above, the globe centered at (1180, 520) and about 640px across, orbiting 10° and pushing in 4% across the piece on easeInOutSine.
- Type (HTML over the canvas): title in Gilda Display 400, 96px, #F2F4F8, baseline at (120, 500) on the backdrop left of the globe; line in Nunito Sans 600, 24px, uppercase, tracked 0.14em, #C4CEDC, beneath. Each rises 12px as it fades in over 1.0 s on cubic-bezier(0.22, 1, 0.36, 1).
- Premium: glass you believe (a window reflection, a bright rim, the table bending behind it, a focused spot of light), a village with eaves, chimneys and lit mullioned windows, flakes that tumble and glint and settle as the swirl dies. Cheap: a grey see-through ball over a flat house icon, with white dots falling straight down.
Banned: rainbow glitter, hands or people, holiday characters, text inside the globe, snow outside the globe, flakes passing through roofs, glass with no reflections, bloom halos, rocking more than 3 times per second, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: the globe at rest, snow lying on the mound and roofs, windows lit; the camera begins its orbit.
- 1.2–2.6s: the globe rocks three times on its base; the snow lifts off and the water starts to swirl.
- 2.6–3.8s: a blizzard under glass: flakes whirl around the steeple, glinting as they tumble.
- 3.8–5.2s: the swirl slows; the title and line rise in.
- 5.2–7.6s: the flakes drift down through the lamplight and settle on roofs, firs and the mound.
- 7.6–8.8s: the last of the swirl dies; the camera eases to rest.
- 8.8–10.0s: hold: a few late flakes still drifting down.
For other lengths, stretch the settling; keep the rocking at 2.2 Hz and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- The transmissive sphere uses three.js's built-in transmission pass, which already includes the village and flakes behind the glass. Flake states are read from the precomputed arrays; the rocking, orbit and swirl are closed-form functions of t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the glass shows the window reflection, a bright rim and the table bending behind it in every frame, the village is clearly visible through the glass, no flake leaves the sphere or sinks into a roof, the rocking stays at 2.2 Hz, and the title sits clear of the globe. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
