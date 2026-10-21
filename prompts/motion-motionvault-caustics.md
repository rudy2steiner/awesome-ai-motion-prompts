# MotionVault: Caustics

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L182) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L182)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Caustics using React + plain Canvas 2D (no extra libraries). A deep water-blue canvas (#0B1B2A) fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Simulate swimming-pool light caustics with a jittered Voronoi approach: scatter a grid of seed points (spacing 64px, each jittered ±22px, drifting slowly on individual sine orbits of 8-14px amplitude, periods 5-11s). Each frame, on a coarse render buffer (scale 0.25, ImageData), compute for each pixel the distances to the two nearest seeds (F1, F2) by checking only the 3x3 neighboring cells; intensity = clamp01(1 - (F2 - F1) / 26) ^ 2.6 — bright thin webs where seeds are equidistant. Map intensity to a pale aqua (140, 220, 210) tint added over the base, plus a faint vertical light gradient (deeper = darker). Upscale the buffer with drawImage (smoothing on) so edges stay soft. Slow, hypnotic, never flashy: cap intensity at 0.5 alpha. Pure rAF loop; clean up the loop and ResizeObserver on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
