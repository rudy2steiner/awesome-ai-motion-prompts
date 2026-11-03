---
title: "Fireworks Finale Animation Prompt for Claude | AI CSS Animations"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/fireworks-finale"
license: "CC0"
collected: "2026-11-03"
---

# Fireworks Finale Animation Prompt for Claude | AI CSS Animations

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/fireworks-finale](https://www.aicssanimations.com/directory/Motion-Prompts/fireworks-finale)  
**License:** CC0

## Prompt

```
Make a 10-second fireworks finale over a harbor skyline: ballistic shells, named burst types, trails, drifting smoke and rippling reflections on the water.

<inputs>
If I don't give you something, use the default and don't ask.
- Event: Lowmere Harbour Midsummer Fireworks (fictional).
- Title: "Midsummer"
- Line: "Lowmere Harbour · Saturday · 22:30"
- Length: 10 seconds.
</inputs>

<direction>
- Palette: sky #0B1030 at the top to #1C1F45 at the horizon, with a faint warm city glow #3A2A48 just above the rooftops; skyline silhouette #080A16 with sparse warm windows #FFC879 (2 × 3px, on about 6% of facades); water #05070F. Star colors from real chemistry: strontium red #FF3A3A, barium green #74FF86, copper blue #5B82FF, sodium gold #FFC15A, charcoal willow #E7A24A, titanium white #FFF4E2, violet #C46BFF. Smoke #6E6A80, lit by the bursts' colors.
- Skyline: a seeded silhouette between y 760 and 880 built from mixed blocks with a few landmarks: a clock tower, a stepped spire, a gasholder frame and a three-arch bridge running to the right edge. The waterline sits at y 880; the water fills 880–1080.
- Physics, all closed-form so seek(t) needs no stored state: height measured upward, gravity g = 600 px/s², and linear drag k for everything: x(t) = x₀ + (v₀ₓ/k)(1 − e^(−kt)), h(t) = h₀ + ((v₀ᵧ + g/k)/k)(1 − e^(−kt)) − (g/k)t. Shells (k = 0.2) rise from three barges on the water in 1.1–1.4 s with a dim gold comet tail and burst at their apex. Stars use k = 2.6 for peonies, rings and chrysanthemums, 1.6 for palm comets and 4.2 for willows, which hang and slide down slowly; burst speeds of 450–750 px/s open a peony to about 220px radius. Burst velocities are 3D (a seeded sphere, or a tilted ring) projected to the screen, so bursts read as spheres with denser rims, not flat circles. Trails are polylines through the same star at t, t − 0.04 … t − 0.24 s, fading along their length and longer for willows.
- Burst types: peony (bright stars that change color at 70% of their life), chrysanthemum (each star sheds a fine trail of sparks), willow (gold, long drooping trails, 3.5 s life), ring (a tilted 3D circle), palm (6–8 thick comets with branching tails). Every star burns out at its own seeded lifetime (±20%), so edges die raggedly.
- Light and smoke: each burst lifts the sky with a soft radial glow (at most 10% added brightness, rising over 0.15 s and decaying over 0.9 s) and leaves a smoke puff that expands, drifts right at 14px/s and stays faintly lit in its burst's color while it burns. Building faces toward a burst pick up a 6% tint.
- Reflection: render the sky layer to an offscreen canvas and draw it flipped onto the water, squashed to 85% height and sliced into 3px rows, each shifted sideways by sin(y·0.09 + t·1.6) × (2 + 6·depth) px, at 45% brightness with a dark blue tint toward the bottom.
- Pacing and safety: never more than three burst moments in any one second (bursts at the same instant count once); from 6 s on, keep burst centers out of the upper-left area where the title will sit. Stars and glows use "lighter" compositing.
- Type: title in Bodoni Moda 600 italic, 104px, #FFF1D6, baseline at (120, 190); line in Work Sans 500, 24px, uppercase, tracked 0.24em, #C9C2D9, beneath.
- Premium: shells that really fly and slow in the air, stars that droop and burn out at different times, smoke that catches the light, rippling reflections. Cheap: circles of dots that grow at constant speed and vanish together.
Banned: stamped sprite bursts, star shapes or sparkle emoji, strobing glitter or crackle, full-sky flashes, perfectly flat circles, straight-line motion, more than three burst moments in any second, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: a calm harbor; windows glow, the water ripples, and the first shell climbs from the left barge.
- 1.0–3.0s: the opening: a red peony (1.1 s), a white chrysanthemum (1.8 s), a green ring (2.5 s); their reflections bloom on the water and the first smoke appears.
- 3.0–5.6s: the build: palms and peonies, one every 0.5 s, alternating barges and colors; smoke layers drift and glow.
- 5.6–7.4s: the finale: five gold willows 0.4 s apart across the center and right, their trails drooping into a curtain over the skyline, with two white palms bursting at the same moments as the second and fourth willows.
- 7.4–8.6s: the willow trails fall and burn out; the smoke glows faintly as it drifts; the title and line fade in over 0.9 s in the clear upper-left sky.
- 8.6–10.0s: hold: only the smoke drifts and the water ripples.
For other lengths, add or remove build shells at the same spacing; keep the finale and at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size × devicePixelRatio. Canvas won't fetch fonts itself, so the awaited loads matter.
- Every shell, star, trail and smoke puff is a closed-form function of t and its seeded launch data, so nothing is stepped and any frame can be drawn directly.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Count burst moments in every one-second window (three at most), check each trajectory curves under gravity and slows with drag, the title stays clear of trails and dense smoke, and each reflection sits under its burst. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
