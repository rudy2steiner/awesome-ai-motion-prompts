---
title: "Lorenz Attractor Animation Prompt for Claude | AI CSS Animations"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/lorenz-attractor"
license: "CC0"
collected: "2026-11-03"
---

# Lorenz Attractor Animation Prompt for Claude | AI CSS Animations

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/lorenz-attractor](https://www.aicssanimations.com/directory/Motion-Prompts/lorenz-attractor)  
**License:** CC0

## Prompt

```
Make a 10-second 3D film of the Lorenz attractor drawn in two inks on paper: one exact path traces the butterfly, then a cloud of 1,200 starting points released almost together tears apart across both wings while the camera orbits.

<inputs>
If I don't give you something, use the default and don't ask.
- Series: "Field Notes on Chaos · No. 3", from the Ashgrove Institute (fictional).
- Title: "A small difference"
- Line: "1,200 starts within 0.1 of one point, on the Lorenz system"
- Closing caption: "Same equations, starts 0.1 apart: six time units later, both wings."
- System: ẋ = σ(y − x), ẏ = x(ρ − z) − y, ż = xy − βz, with σ = 10, ρ = 28, β = 8/3.
- Length: 10 seconds.
</inputs>

<direction>
- Palette, two inks and graphite on paper: paper #EFE8DA with faint seeded fibers (±2%) and a soft vignette to #E6DDCB; graphite #3A3733 for the first path, axes and marks; indigo ink #2B3C8F and vermilion ink #E0452B for the cloud, with plum #6B3A7E as the midpoint of the ramp between them; type #26231F, secondary #7A736A.
- The ink look: every stroke is multiplied onto the paper, never alpha-blended to grey: CustomBlending with blendSrc DstColorFactor and blendDst ZeroFactor, each fragment writing mix(vec3(1.0), ink, coverage). Overlapping strokes darken like real ink, indigo over vermilion goes deep plum-black, and order doesn't matter, so nothing is sorted and depthTest is off for strokes. Depth reads through ink density: coverage × (0.55 + 0.45·nearness), nearness from 0 at the far side of the attractor to 1 at the near side. The paper is a full-screen quad drawn first.
- Integration, exact: RK4 at a fixed step of 0.002 time units, everything precomputed at load, positions stored every 0.01 units. Lorenz time τ(t) runs at 1.2 units per second from t = 0.6 s and eases to a freeze over 8.0–8.8 s (the closed-form integral of a speed that falls on a half-cosine), ending near τ = 9.36.
- The first path: starts at (0.143500, −2.284607, 23.466987) at τ = 0 and runs to τ = 2.6, switching wings at about τ = 0.14, 1.15 and 1.70, so it draws the whole butterfly. A 1.6px graphite line grows from its start with a 5px head dot; after the release it stays as a 22% graphite guide.
- The cloud: at τ = 2.6 (t ≈ 2.77 s), 1,200 points seeded uniformly in a ball of radius 0.1 around the path's position there, (−7.6283, −11.6829, 18.7017). From these exact values its RMS radius goes 0.08 at release, about 0.7 at +1.5 units, about 5 at +2.5 as it stretches past the origin, refolds to about 0.8 by +3.0, then about 9 at +4.5 and 8–19 from +5.0 on, split almost exactly half and half between the wings: a tight bead, a ribbon, then a cloud over both wings. Color: rank each point by its coordinate along the cloud's first principal axis at τ = 4.1 (1.5 units after release) and map the rank through indigo → plum → vermilion, so the stretched ribbon runs indigo at one end to vermilion at the other and the inks interleave as it folds.
- Strokes: each cloud point draws its trail over the last 0.25 time units (Catmull–Rom through the stored samples) as a screen-space ribbon 2.2px wide at the head tapering to 0 at the tail, coverage 0.55 at the head fading to 0, plus a 3px head dot at full coverage. Build all 1,200 ribbons in one BufferGeometry, offsetting each vertex sideways in screen space in the vertex shader from its neighbors (previous and next sample), so widths stay true at any distance.
- Graphite marks: three axes from the origin (x and y from −25 to 25, z from 0 to 50) as 1px lines with ticks every 10 units and small x, y, z labels; the fixed points C⁺ and C⁻ at (±6√2, ±6√2, 27) ≈ (±8.49, ±8.49, 27) as 12px circled crosses; the origin, the third fixed point, as a 7px open circle.
- Camera: PerspectiveCamera, fov 30, up +z, target (0, 0, 25), distance 118. It opens on the −y side (azimuth −90°, elevation 6°), the classic butterfly view with x across and z up, then orbits to azimuth −25° and elevation 24° over 2.8–8.6 s on easeInOutSine. Use setViewOffset so the target sits at x 1180 on the stage; the attractor fills about 70% of the frame height.
- Type, HTML over the canvas: the kicker in Sometype Mono 500, 20px, tracked 0.14em, uppercase, vermilion, at (120, 96); the title in Literata 600 (opsz 72), 72px, #26231F, at (120, 170), two lines at most; the line in Literata 400 italic, 26px, secondary, beneath. The equations at (120, 470) in Literata 400 italic, 30px, one per line, with the constants beneath in Sometype Mono 400, 20px. From (120, 690) two readouts in Sometype Mono 500, 26px, tabular figures: "τ" and "Cloud spread" (RMS radius, two significant figures). Under them a 380 × 120px chart: log₁₀ of the cloud's RMS radius from 0.01 to 100 against time since release, drawn live as a 2px vermilion line, beside a dashed graphite reference of slope 0.906 per unit (the system's largest Lyapunov exponent) labeled "e^0.906τ" in Sometype Mono 400, 20px. Labels C⁺ and C⁻ in Sometype Mono 400, 20px, projected from 3D each seek. The closing caption in Literata 500, 26px, at (120, 1000).
- Easing: text rises 12px as it fades in over 0.6 s on cubic-bezier(0.22, 1, 0.36, 1). Camera on easeInOutSine; nothing bounces.
- Premium: two inks that overprint like a print, one exact solution drawn to scale, a cloud that visibly holds together and then tears apart exactly as the equations say, a calm orbiting camera. Cheap: neon particle trails with bloom in a black void, a pre-baked butterfly curve with random sparkles.
Banned: black or dark backgrounds, glow or bloom, additive blending, colors beyond the palette, motion not from the equations, motion blur, camera shake, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.6s: paper; the axes and fixed-point marks draw in over 0.4 s; the kicker, title and line rise in.
- 0.6–2.8s: the first path draws the butterfly from its start, crossing between the wings three times; the equations rise in at 1.0 s.
- 2.8s: release: the 1,200 points appear at the path's head as one dark bead; the path fades to its 22% guide; the readouts and chart rise in.
- 2.8–4.6s: the bead travels as one thick bundled stroke; about 1.5 units after release it starts to stretch.
- 4.6–6.6s: it smears into a long ribbon, indigo at one end and vermilion at the other, wrapping both wings while the chart climbs along the reference slope; the camera has turned far enough to show the wings' depth. The 6.0 s frame: the two-ink ribbon across both wings over the faint guide.
- 6.6–8.0s: the ribbon folds again and again until the inks interleave across both wings.
- 8.0–8.8s: time eases to a freeze; the closing caption rises in.
- 8.8–10.0s: hold, completely still.
For other lengths, change the Lorenz-time rate and keep the release at τ = 2.6 and the cloud's 6.8 units; keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every shape and texture is generated in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Anything cumulative is solved analytically from t or precomputed once at load at a fixed step. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face before defining window.seek.
- Engine: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (`three` and `three/addons/`). WebGLRenderer with antialias, preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio); render once at the end of every seek. Text is HTML over the canvas; the chart is a 2D canvas.
- The path and all 1,200 cloud points are integrated once at load into Float32Arrays (about 940 samples each); seek(t) maps t to τ in closed form and only reads and interpolates them.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Also log the cloud's RMS radius at 0.5 and 4.5 units after release (about 0.07 and 9) and the share of points with x < 0 at the end (about 0.5). Check the strokes darken where they cross instead of turning grey, far strokes are lighter than near ones, the first frame is the classic butterfly view, labels C⁺ and C⁻ sit on their marks, and the chart and type stay clear of the attractor. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
