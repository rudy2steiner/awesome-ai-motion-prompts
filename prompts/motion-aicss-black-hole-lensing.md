---
title: "Black Hole Animation Prompt for Claude | AI CSS Animations"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/black-hole-lensing"
license: "CC0"
collected: "2026-11-03"
---

# Black Hole Animation Prompt for Claude | AI CSS Animations

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/black-hole-lensing](https://www.aicssanimations.com/directory/Motion-Prompts/black-hole-lensing)  
**License:** CC0

## Prompt

```
Make a 10-second ray-traced film of a black hole: a glowing accretion disk bent by gravitational lensing, with its photon ring, a Doppler-bright approaching side and lensed stars, as the camera orbits slowly.

<inputs>
If I don't give you something, use the default and don't ask.
- Object: Tessaly X-7 (fictional), a non-rotating black hole of 9 million solar masses.
- Title: "Light, bent"
- Line: "Every pixel is a ray of light traced through curved space."
- Labels: "Shadow" · "Photon ring" · "Far side of the disk, lensed over the top" · "Approaching side: Doppler-bright" · "Receding side: dimmer and redder"
- Scale note: "Shadow: 5.2 horizon radii across"
- Length: 10 seconds.
</inputs>

<direction>
- Look: an honest relativistic render lit only by the disk: a thin hot disk around a dark shadow, its far side bent up over the top and down under the bottom, a razor-thin photon ring, one side blazing and the other dim, against a lensed field of stars in deep blue-green space.
- Palette: space #04121A with a faint dust band #0D3440 and mauve wisps #3A2440; disk emission mapped through one ramp by observed temperature: madder #5C0F2E → rose #D8436A → apricot #FFB27A → cream #FFF1DC → ice #DDF2FF at the hottest, on the approaching side; stars #E6F0FF with a few #FFD9B0; title #EEF4F6, secondary #8FB3BA, label leaders #8FB3BA. The warm ramp against blue-green space is the whole palette: no other hues.
- Physics, in units where the horizon radius r_s = 1, for a Schwarzschild black hole. For each pixel, march the photon backward from the camera with the null-geodesic shortcut x'' = −1.5·h²·x ÷ |x|⁵, with h = |x × v| conserved; adaptive steps (0.06·r, at least 0.02, at most 1.0), up to 400. Stop when r < 1 (the ray falls in: black) or when r > 60 and moving outward (it escapes: sample the sky in its final direction).
- The disk lies in the plane y = 0 from r = 3, the innermost stable orbit, to r = 12. At every crossing of that plane (locate it by interpolating between steps), add the disk's emission and absorb by its opacity (0.85 inside r = 8, fading to 0 at 12), so the lensed far side shows over the top and a thin secondary image wraps under the shadow. Emission: temperature T(r) ∝ r^(−3/4)·(1 − √(3/r))^(1/4); the observed shift g = √(1 − 1/r) ÷ (γ·(1 − β·cosα)), with orbital speed β = √(0.5 ÷ (r − 1)), γ = 1/√(1 − β²) and α the angle between the gas's motion and the direction toward the camera; intensity ∝ g⁴·T⁴·density, color from the ramp at g·T. Texture: density = 0.55 + 0.45·fBm(6·log r, φ − Ω(r)·t) with Kepler shear Ω(r) ∝ r^(−3/2) (the inner edge turning once every 3.2 s), giving fine spiral streaks that wind tighter inside, plus 7 seeded hot clumps (Gaussian blobs 0.3–0.6 across at r 4–9) riding their orbits, each appearing twice through lensing. Choose the spin so the approaching side is on the left.
- The photon ring is never drawn by hand: it comes from rays that loop near r = 1.5 and cross the disk several times. Use enough small steps there that it is a continuous, thin bright ring hugging the shadow's edge at an apparent radius of √27/2 ≈ 2.6.
- Sky: a procedural star field sampled by final direction (three magnitudes, seeded on a cube-sphere hash, crisp points), a faint dust band and nebula wisps, so lensing visibly stretches and doubles stars near the shadow and smears a faint Einstein ring at the right radius. No star ever appears inside the shadow.
- Render: one full-screen ShaderMaterial quad at full resolution, then EffectComposer with UnrealBloomPass (strength 0.5, radius 0.35, threshold 0.72) so only the hot approaching side, the ring and the clumps glow, then OutputPass. ACESFilmic, exposure set so the disk is bright and the dim side still clearly visible.
- Camera: distance 34, fov 30, orbiting slowly: inclination from 4° above the disk plane at the start (the disk a bright band across most of the frame, its far side arched over the shadow) to 14° by 8.6 s, yawing 24° on easeInOutSine and dollying in to 32; the shadow centered at (1180, 600), about 320px across. The far-side arch stays clear of the title: keep everything left of x 840 and above y 330 over dark sky.
- Labels (HTML): Inconsolata 500, 22px, #EEF4F6, on 1px leaders ending in 5px dots, anchored to real features each seek: the shadow's edge and the photon ring at their apparent radii, the top of the far-side arch found by tracing a column of 200 rays up the shadow's center line on the CPU with the same integrator, and the approaching and receding sides at the disk's projected left and right; at most three at once.
- Type: kicker "TESSALY X-7 · 9 MILLION SOLAR MASSES" in Inconsolata 500, 20px, tracked 0.16em, secondary; title Noto Serif Display 300 italic, 104px, #EEF4F6, top-left at (120, 110); line Inconsolata 400, 24px, secondary, beneath; the scale note at bottom left (120, 990) in Inconsolata 500, 22px, above a 1px bar exactly as long as the shadow's diameter on screen. Text rises 12px as it fades in over 0.6 s on cubic-bezier(0.22, 1, 0.36, 1).
- Premium: every shape comes from tracing rays: the arch over the top, the thin ring, the bright side, stars stretched near the edge. Cheap: an orange donut with a black circle on it, a glow ring drawn on by hand, a disk the same on both sides.
Banned: a symmetric disk, a hand-drawn ring, stars inside the shadow, lens flares, jets, spaceships, planets, rainbow colors, any flash, camera shake, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.2s: nearly edge-on: the bright disk crosses the frame, its far side arched over the shadow and a thin image under it, already turning; the kicker rises in.
- 1.2–3.4s: the camera begins to rise and orbit; the hot clumps stream around, each seen twice; the title and line rise in at 1.6 s.
- 3.4–6.0s: "Shadow" and "Photon ring" attach at 3.6 s, then "Far side of the disk, lensed over the top" at 4.4 s. At 6.0 s the camera is at about 10°, three labels on, nothing mid-fade.
- 6.0–7.6s: those labels clear; "Approaching side: Doppler-bright" and "Receding side: dimmer and redder" attach at 6.4 s.
- 7.6–8.6s: the camera settles at 14°; the scale note and its bar rise in.
- 8.6–10.0s: hold: the camera still, only the disk turning.
For other lengths, stretch the orbit; keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas.
- Camera orbit, disk rotation and clump phases are closed-form functions of t passed to the shader as uniforms; the shader traces every pixel fresh each seek, so any frame is direct. Call composer.render() once per seek in place of renderer.render().
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check the far side arches over and under the shadow in every frame, the photon ring is thin and continuous, the left side is clearly brighter and bluer than the right, stars near the shadow stretch into arcs and none sit inside it, the inner disk visibly shears faster than the outer, the frame is bright from the first second, each label sits on its feature, and the title stays over dark sky. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
