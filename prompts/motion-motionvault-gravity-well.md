# MotionVault: Gravity Well

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L117) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L117)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called GravityWell using React + plain Canvas 2D (no extra libraries). A dark canvas fills its container (absolute inset-0, cursor crosshair, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Spawn 150 small white particles (1-2.4px, alpha 0.35-0.85) drifting slowly (0.15-0.45 px/frame) and wrapping around edges. While the pointer is inside, it acts as a gravity well: particles within 200px receive a mild attraction toward the cursor (acceleration ~0.045 with distance falloff) plus a stronger tangential push (~0.14 perpendicular to the radial direction) so they are captured into ORBITS instead of collapsing; add an outward push inside 34px, global velocity damping 0.985 and a 4 px/frame speed cap for stability. Draw a faint 200px reach circle and a 6px core ring at the cursor. On click, the well becomes a repulsor for 400ms: particles within 260px are blasted outward (force 3.2 with falloff), an expanding flash ring (10 -> 120px, fading over 400ms) marks the pulse, then calm orbiting resumes. Reset the pointer offscreen on pointerleave. Clean up requestAnimationFrame, ResizeObserver and all listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
