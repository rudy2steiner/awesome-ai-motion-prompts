---
title: "Hyperspace Jump Animation Prompt for Claude | AI CSS Animations"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/hyperspace-jump"
license: "CC0"
collected: "2026-11-03"
---

# Hyperspace Jump Animation Prompt for Claude | AI CSS Animations

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/hyperspace-jump](https://www.aicssanimations.com/directory/Motion-Prompts/hyperspace-jump)  
**License:** CC0

## Prompt

```
Make a 10-second hyperspace jump: a still starfield stretches into streaks, becomes a tunnel of light, then drops out above an alien planet.

<inputs>
If I don't give you something, use the default and don't ask.
- Planet: Orvane IV (fictional).
- Title: "Orvane IV"
- Subline: "Arrival, 41 light-years out"
- Length: 10 seconds.
</inputs>

<direction>
- Palette: space #02030A; stars #DCE8FF with a few #FFE2C4 and #A9C8FF; streak heads #FFFFFF fading to tails #4E9BFF; tunnel #1E3BFF, #6FD3FF and #8A5CFF; planet ocean #1C6A86, deep ocean #0F3A55, land ochre #C49856 and #8E6A3E, clouds #F2F4F2, atmosphere rim #7FD0FF, night-side city lights #FFC27A; title #EAF2FF, subline #8FA6C6.
- Stars: 7,000 seeded stars in a hollow cylinder (radius 6–80 units, 600 units long) around the flight axis, drawn as LineSegments with a custom shader: each star is a segment from its position back along the axis by v(t) × 0.05 s of travel, so at rest it is a dot and at speed a streak, every streak converging on one vanishing point at frame center. Brightness follows size; far stars are dimmer. Distance travelled is the closed-form integral of v(t) and star z wraps modulo the cylinder length, so any frame is direct to compute.
- Speed v(t): cruise 0.5 units/s; a brief pull-back before the jump (v dips to −0.3 for 0.3 s, the field drawing inward); exponential acceleration to 900 units/s over 1.4 s; hold; then a hard but eased drop to 0.4 units/s over 0.5 s (easeOutExpo). The jump and the drop-out are the only fast moments.
- Tunnel: at full speed, a long open cylinder (radius 3, camera inside) with an additive ShaderMaterial of streaming fBm along its length and fine lengthwise filaments, colored through the three tunnel hues by angle and rolling 20° across the beat. It grows out of the streaks and collapses back into them, and never adds more than 70% to frame brightness.
- Planet: not visible before the drop-out; after it, a sphere of radius 60 below and ahead whose limb arcs across the lower 55% of the frame, lit by a sun out of frame upper right. One ShaderMaterial computes it from 3D noise on the surface normal: oceans and ochre continents, a separate slowly turning cloud shell, a terminator across the left third with warm city lights on the night side, and a back-face atmosphere shell with a Fresnel rim in #7FD0FF. A small gray moon (radius 2.5, cratered by noise) hangs at upper left.
- Post: EffectComposer with UnrealBloomPass (strength 0.55, radius 0.4, threshold 0.6) so only streak heads and the rim bloom, then OutputPass. ACESFilmic.
- Camera: fov 60 at cruise, widening to 75 at full speed, settling to 50 on arrival; after the drop-out it pitches down 5° and drifts forward slowly.
- Type (HTML over the canvas): title in Michroma 400, 64px, uppercase, tracked 0.32em, #EAF2FF, centered with its baseline at y 260 in the dark sky above the planet; subline Barlow 400, 24px, tracked 0.2em, #8FA6C6, beneath.
- Safety is part of the brief: the drop-out is not a white flash. Average frame brightness never changes by more than 20% within any 0.33 s, and nothing flickers.
- Premium: one vanishing point, streak length that truly follows speed, a planet that looks lit by a real sun. Cheap: a zoom-blur filter on a star photo, a white flash cut.
Banned: white or full-frame flashes, camera shake, lens flares, spaceships, cockpits or HUDs, rainbow streaks, streaks that miss the vanishing point, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.4s: a still, deep starfield drifting toward the camera at cruise speed.
- 1.4–1.7s: the pull-back: the field eases inward.
- 1.7–3.1s: the jump: stars stretch into streaks that lengthen and turn blue-white, all racing out from the center.
- 3.1–5.4s: the streaks merge into the tunnel, which streams and rolls; the field of view widens.
- 5.4–5.9s: drop-out: the tunnel collapses and the streaks shrink back to points as the speed falls away.
- 5.9–7.8s: the planet is revealed below with its limb and terminator, clouds turning slowly; the camera pitches down and drifts.
- 7.8–8.6s: the title, then the subline, rise 12px as they fade in.
- 8.6–10.0s: hold; only the clouds drift.
For other lengths, stretch the tunnel beat; keep the drop-out at 0.5 s and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- Call composer.render() once per seek in place of renderer.render(). Star positions, tunnel flow and cloud rotation are closed-form functions of t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check every streak frame shares one vanishing point, log the average luminance of each frame from 5.0 to 6.5 s to confirm there is no flash, the planet's lit side faces the off-screen sun, and the title sits over clear sky. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
