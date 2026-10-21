# MotionVault: Fireworks

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L95) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L95)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Fireworks using React + plain Canvas 2D (no extra libraries). A dark canvas fills its container (absolute inset-0, cursor crosshair, DPR-aware sizing via ResizeObserver, clamp DPR to 2). On click, launch a rocket from the bottom edge that rises to the click point (speed ~8-10 px/frame upward, slight horizontal sine wobble of 3px amplitude, short 8-dot fading trail, glowing white head). On arrival it explodes into 60-90 radial sparks using 2-3 harmonious hues per burst picked from a muted palette (amber #F59E0B/#FBBF24/#FDE68A, rose #F43F5E/#FB7185/#FDA4AF, sky #0EA5E9/#38BDF8/#7DD3FC). Sparks have random radial velocities (1-5 px/frame), gravity 0.04, drag 0.96, and fade over ~1.5s while their radius shrinks to 30%. If no launch happens for 2.5s, auto-launch one rocket at a random position. Multiple simultaneous bursts must be supported. Clean up requestAnimationFrame, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
