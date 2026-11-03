---
title: "Neural Network Explainer Animation Prompt for Claude"
author: "AI CSS Animations"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/neural-network-explainer"
license: "CC0"
collected: "2026-11-03"
---

# Neural Network Explainer Animation Prompt for Claude

**Author:** AI CSS Animations  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/neural-network-explainer](https://www.aicssanimations.com/directory/Motion-Prompts/neural-network-explainer)  
**License:** CC0

## Prompt

```
Make a 10-second 3D neural network explainer: a handwritten 7 rises out of a 28×28 pixel grid, activations flow forward through two hidden layers, and the output layer settles on 7.

<inputs>
- Digit: a handwritten 7, drawn in code.
- Network: 784 inputs (28×28) → 16 → 16 → 10 outputs.
- Output probabilities, summing to 100%: 0: 1%, 1: 3%, 2: 2%, 3: 1%, 4: 2%, 5: 0%, 6: 0%, 7: 88%, 8: 1%, 9: 2%.
- Title: "How a network reads a 7". Layer labels: "784 pixels", "16 neurons", "16 neurons", "10 digits".
- Caption: "88% sure it's a 7."
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Studio: background #DCE3EA; a ShadowMaterial floor at 22% opacity just below the network so everything sits in space; a hemisphere light (sky #FFFFFF, ground #B8C2CC, intensity 0.9) and one directional key from the upper left casting soft shadows (PCFSoftShadowMap, 2048 map). Matte materials only: MeshStandardMaterial, roughness 0.7, metalness 0. Colors: idle nodes #C3CCD6; activation ramps from #FFD9A8 to #FF7A1A; ink pixels #23303D; paper pixels #F4F6F8; links #3A4654; the winning output #FF5A1F.
The digit: two strokes, a slightly rising top bar and a long diagonal with a small hook at its foot, with seeded wobble. Rasterize them at 280×280 with a 22px round pen, center by mass in a 20×20 box and average down to 28×28, giving the soft gray edges of the classic handwritten-digit datasets. Those 784 values are the input.
Geometry, layers along x: the input is a 28×28 grid of square tiles (0.12 units, 0.015 gaps) standing in the y–z plane at x = −6; each tile is a box whose depth toward the network is 0.02 + 0.5 × intensity, colored from paper to ink by intensity, so the 7 stands out as a relief. Hidden layers are 4×4 grids of spheres (radius 0.18, spacing 0.75) at x = −1.5 and x = 2. The output is a column of 10 spheres (radius 0.22, spacing 0.62) at x = 5.5. Links are LineSegments with per-vertex color: from each lit pixel (intensity above 0.2) to all 16 first-layer nodes, then all 256 and all 160 between the later layers. Weights come from a seeded PRNG (normal, σ 0.5); a link rests at 6% + 10%·|w| opacity.
Activations: hidden layers come from a real forward pass with those weights (ReLU, then scaled 0–1 per layer for display); the output layer shows the given probabilities exactly. A node fills along the ramp, with emissive 0.25 × activation, as its pulses arrive.
Pulses: at each layer step, the 120 strongest contributions (|w × activation|) each carry a bright dash, 0.25 units long and in the ramp color, along their link over 0.6s, start times staggered by up to 0.25s.
Camera: a 32° PerspectiveCamera. It starts close on the input from the front left (position (−9.5, 1.2, 6.5), looking at (−6, 0, 0)), pulls back to a three-quarter view of the whole network ((−1, 3.2, 13) looking at (0.5, 0, 0)), and ends nearer the outputs ((3.5, 2.4, 10) looking at (3.5, 0, 0)). Moves take 1.4–2s on cubic-bezier(0.65, 0, 0.35, 1); total yaw stays under 40°.
Overlay, HTML on top in "Manrope": title 700, 56px, #16202B, top-left at x 96, baseline y 120; layer labels 600, 24px, #45525F, projected under each layer and clamped inside 96px margins; digit labels 0–9 (700, 26px) left of each output sphere and probability bars right of it (up to 180px, #FF5A1F for 7, #9AA6B2 for the rest) with values at 22px in tabular figures, all projected from 3D every frame; caption 700, 40px, bottom-left at x 96, baseline y 1000.
The real thing is a calm, legible machine: a digit you can read in the relief, links thin enough to see through, pulses that follow real weights to a clear winner. The cheap version is a neon brain, random sparks and a camera that never stops spinning.
Banned: brains, neon, bloom, particles off the links, sci-fi HUD details, camera spins over 40°, 3D text, probabilities that don't sum to 100%, emoji, anything flashing more than 3 times per second.
</direction>

<structure>
0.0–1.4s: close on the input grid; a virtual pen writes the 7, and tiles rise to their relief as it passes (top bar, then the diagonal) over 0.15s each; the title fades up.
1.4–2.6s: the camera pulls back to the three-quarter view; hidden and output nodes scale in layer by layer (0.25s each, 40ms apart); links fade to rest; layer labels fade in.
2.6–4.0s: input to hidden layer 1: pulses leave the lit pixels and the first hidden layer fills.
4.0–5.2s: hidden layer 1 to hidden layer 2.
5.2–6.4s: hidden layer 2 to the outputs: output nodes fill to their probabilities; node 7 swells to 1.35× and turns #FF5A1F.
6.4–7.8s: the camera glides toward the outputs; probability bars grow over 0.6s each on cubic-bezier(0.22, 1, 0.36, 1), 40ms apart, values counting up.
7.8–8.6s: links fade to 2% except the strongest chain into 7 (its top contributor in hidden layer 2, that node's top contributor in hidden layer 1, and that node's 12 strongest pixel links); the caption fades up.
8.6–10.0s: hold; the camera comes to rest by 9.0s and stays still.
Other lengths: scale the three forward-pass beats evenly; keep the hold at least 1s.
</structure>

<build>
One self-contained index.html, CSS and JS inline. Google Fonts via <link> are fine; no other libraries. Real 3D is needed here: three.js as an ES module pinned to three@0.160.0 through an import map on jsDelivr (https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js, addons under https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/), a WebGLRenderer with preserveDrawingBuffer: true and setPixelRatio(window.devicePixelRatio), and exactly one renderer.render at the end of every seek. Text is HTML on top. Await document.fonts.load() for every face before defining window.seek. The stage is 1920×1080 (16:9), scaled to fit the window. Design for 60fps. window.seek(t), t in seconds, must compute every visual from t alone: no CSS transitions or animations, no setTimeout or setInterval, no state carried between frames, and randomness only from a seeded PRNG. The rasterized digit, the weights and the forward pass are computed once at load; pulses, fills and the camera are pure functions of t. Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
</build>

<check>
Before showing me, step through one frame per second: screenshot each and look at it. Fix overlaps, clipped or cramped text, accidental edge collisions, and anything off-style or Banned. Check that the 7 reads clearly in the relief, labels and bars never overlap spheres or each other at any camera position, the bars match the given probabilities, shadows are soft and present, and nothing moves in the final second. Confirm seek(duration) and seek(duration + 1) match, so the final frame holds.
</check>
```
