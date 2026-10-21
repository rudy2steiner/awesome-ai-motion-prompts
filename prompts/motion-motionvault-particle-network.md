# MotionVault: Particle Network

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L24) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L24)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ParticleNetwork using React + plain Canvas 2D (no extra libraries). A canvas fills its container (absolute inset-0, cursor crosshair, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Spawn nodes proportional to area (count = clamp(width*height/9000, 28, 70)) with small random velocities. Each frame: clear, update positions with velocity damping (0.995) and edge bounce, then draw hairline connections (rgba(9,9,11,0.12), 1px) between nodes closer than 110px with alpha fading by distance, and fill 1.6px dots (rgba(9,9,11,0.55)) at each node. Pointer interaction: nodes within 140px of the cursor receive a small attraction force toward it (acceleration 0.02 along the normalized direction); when the pointer leaves, reset it offscreen. Clean up requestAnimationFrame, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
