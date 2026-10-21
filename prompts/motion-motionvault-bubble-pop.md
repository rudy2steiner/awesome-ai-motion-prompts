# MotionVault: Bubble Pop

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L128) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L128)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called BubblePop using React + plain Canvas 2D (no extra libraries). A light (zinc-50) canvas fills its container (absolute inset-0, cursor pointer, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Iridescent bubbles (thin-stroke circles, radius 12-40px) float upward from below the bottom edge at 0.35-1.0 px/frame with a horizontal sine sway (10px amplitude). Each bubble wobbles subtly (drawn as an ellipse whose rx/ry oscillate ±5% in antiphase), has a translucent white body (rgba(255,255,255,0.22)), a 1.2px rim in zinc-400 with occasional sky-400 or rose-400 pastel tints, and a small white highlight arc at the upper-left. Keep 8-14 bubbles alive, respawning from the bottom; bubbles that drift off the top are removed. On click, any bubble under the cursor pops: it is removed, 8-10 tiny droplet particles (1.4-2.6px, matching tint) burst outward with gravity, and a quick ring expands from 0.5x to 1.6x the bubble radius while fading over 300ms. Clean up requestAnimationFrame, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
