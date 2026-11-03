---
title: "Spiral Galaxy Animation Prompt for Claude | AI CSS Animations"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/spiral-galaxy"
license: "CC0"
collected: "2026-11-03"
---

# Spiral Galaxy Animation Prompt for Claude | AI CSS Animations

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/spiral-galaxy](https://www.aicssanimations.com/directory/Motion-Prompts/spiral-galaxy)  
**License:** CC0

## Prompt

```
Make a 10-second film of a spiral galaxy taking shape: a turning disk of stars gathers into two dusty arms around a bright core while the camera rises to look down on it.

<inputs>
If I don't give you something, use the default and don't ask.
- Galaxy: the Vesper Wheel (fictional).
- Title: "The Vesper Wheel"
- Line: "Two arms · 210 billion stars · 104,000 light-years across"
- Clock: +0 to +240 million years.
- Length: 10 seconds.
</inputs>

<direction>
- Palette: space #04040A with a faint violet haze #120C22 behind the disk; core #FFF1D6 into #FFC977; bulge and old disk stars #FFD9A6 and #F5C08A; young arm stars #A9C6FF and #D8E5FF; star-forming knots #FF6EA3 with #FF9BC0 halos; dust #2B160C; title #EEE8FF, secondary #A49CC0.
- Arms from orbits (kinematic density waves): every disk star moves on its own ellipse around the center. With disk radius R = 10 units and semi-major axis a: eccentricity e(a) rises from 0 in the core to 0.32 at 0.45R and eases to 0.18 at the rim; the ellipse is turned by φ(a) = φp + κ·a/R with κ = 3.1 rad; the star's angle along it is θ = θ0 + Ω(a)·T with Ω(a) = Ω0/(a + 0.8), so inner stars orbit faster; position x = a·cos θ·cos φ − b·sin θ·sin φ, y = a·cos θ·sin φ + b·sin θ·cos φ, with b = a·√(1 − e²). Where neighboring ellipses crowd, density rises into two arms on its own; pick the sign of κ so they trail, their outer ends curving back against the rotation. The pattern turns slowly as a whole (φp at a fixed pattern speed) while stars stream through it.
- Forming: e and κ ramp from 0 (a plain turning disk with no arms) to full on easeInOutSine over 1.0–5.0 s while the disk's thickness falls from 0.35R to 0.05R, so the arms condense out of an even glow.
- Populations (seeded, about 170,000 points):
  - 110,000 disk stars, a drawn from an exponential profile (scale length 0.3R), 1–2.4px, warm in the inner disk and neutral toward the rim;
  - 22,000 young blue stars, 160 pink knots of 20–40 points each with one soft halo sprite, and 26,000 dust points, all placed along the arms in the pattern's own frame and turning with it. Find the arm crests once at load from a polar density histogram of the disk stars at full ramp (the two density peaks at each radius), then put blue stars on the crests, knots strung just outside them, and dust in thin filaments on their inner (concave) edges, offset about 0.03R toward the center; they fade in with the arms over 1.6–5.0 s;
  - 18,000 bulge stars in an oblate ellipsoid (0.12R) plus a core sprite (a radial falloff, 160px across at the final framing);
  - in front of everything, 900 sharp field stars across the frame (1–2.5px, slight color variety) and six tiny distant galaxies (soft elliptical smudges 6–14px).
- Rendering: Points with a ShaderMaterial: round Gaussian sprites, size attenuation, AdditiveBlending, depthWrite false; dust drawn afterwards with NormalBlending at 22–40% opacity and 3–7px, so lanes darken the light behind them. EffectComposer with UnrealBloomPass (strength 0.5, radius 0.5, threshold 0.7) so only the core and knots glow, then OutputPass; ACESFilmic. Set exposure so the disk is bright from the first frame: from 1 s on the galaxy spans at least 60% of the frame width and the arms read clearly against space.
- Time: T(t) is galactic time, the closed-form integral of a rate that runs steady and eases to a quarter over the last 1.4 s; it drives every angle, and the clock shows it, reaching +240 Myr at 10 s. Choose Ω0 so stars at 0.3R complete about 0.8 of an orbit across the piece and stars at the rim about 0.25; the pattern turns about 23°.
- Camera: fov 40; it starts 14° above the disk plane and close, the disk a bright lens with the bulge standing above it, and rises to 52° above the plane over 1.0–7.6 s on easeInOutSine while yawing 30° and pulling back, ending with the galaxy centered at (1160, 560) and spanning about 65% of the frame width.
- Type (HTML over the canvas): title in Instrument Serif 400, 88px, #EEE8FF, at (120, 150); line in Azeret Mono 400, 22px, tracked 0.06em, #A49CC0, beneath; the clock "+0 Myr" → "+240 Myr" in Azeret Mono 400, 24px, tabular, at the bottom left (120, 980); three labels in Azeret Mono 400, 20px, on 1px #A49CC0 hairline leaders ending in 4px dots on real features: "core", "dust lane", "star-forming knot", each anchor projected from 3D every seek.
- Easing: camera and ramps on easeInOutSine; text rises 12px as it fades in over 0.6 s on cubic-bezier(0.22, 1, 0.36, 1).
- Premium: arms that come from orbits (stars streaming through a slowly turning pattern), dust that blocks light, a warm core and blue arms, a camera that rises calmly. Cheap: a 2D spiral of dots spinning like a pinwheel, uniform white stars, a lens-flare core.
Banned: the whole disk rotating rigidly at one speed, lens flares, rainbow colors, spaceships or planets, twinkling faster than 1 Hz, dim or near-black frames, hard-edged sprites, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.0s: a broad, puffy disk of warm stars turns slowly, seen from low above its plane; the core glows; the field stars are still.
- 1.0–3.4s: the disk flattens; as the ellipses stretch and twist, two arms gather out of the glow and dust begins to thread along their inner edges.
- 3.4–6.0s: the camera rises and yaws; the arms sharpen; blue stars and pink knots light along them; inner stars visibly overtake outer ones; the title and line rise in at 4.4 s.
- 6.0–7.6s: the camera settles at 52°; the clock passes +200 Myr.
- 7.6–8.6s: the three labels attach, 0.2 s apart.
- 8.6–10.0s: hold; the rotation slows to a quarter and the clock stops at +240 Myr.
For other lengths, stretch the forming beat; keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- Star positions are computed in the vertex shader from per-star attributes (a, θ0, population, height, color) and uniforms (T, the forming ramp, the pattern angle), so each seek only sets uniforms; call composer.render() once per seek in place of renderer.render().
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check two arms read clearly from 3.4 s on, dust lanes sit on the arms' inner edges and darken what is behind them, inner stars move faster than outer ones while the pattern turns slowly, the galaxy is bright and large from the first second, each label points at its feature, and the title sits over dark sky clear of the disk. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
