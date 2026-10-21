# MotionVault: Murmuration

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L211) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L211)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Murmuration using React + plain Canvas 2D (no extra libraries). A dark (zinc-950 #09090B) canvas fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Simulate a boids flock of 130 starlings: per frame each bird steers by the three classic rules with neighbor radius 60px — separation (push away from neighbors closer than 24px, weight 0.075), alignment (steer toward the average neighbor heading, weight 0.055), cohesion (barely-there steer toward the neighbor centroid, weight 0.0002 per px) — plus a very loose pull toward a wandering attractor (Lissajous orbit around the canvas center, ax=0.31*width, ay=0.22*height, wx=0.11, wy=0.073 rad/s, weight only 0.0005) and a per-bird random jitter (±0.03 per axis per frame) so the swarm morphs between ribbons and clouds instead of settling into a stable orbit ball. Clamp speed to 1.6-3.3 px/frame with smooth heading turn (limit delta-heading to ±0.14 rad/frame). Draw each bird as a tiny chevron (two 3.4px strokes meeting at a 70deg angle, slate-300 rgba(203,213,225,0.75), 1.1px) oriented along its velocity; wrap positions around edges with a 24px margin. Pointer as predator: birds within 120px of the cursor get a strong flee force (0.9 with linear falloff) so the flock splits around the pointer and swirls back together; reset the pointer offscreen on pointerleave. Pure rAF loop; clean up the loop, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
