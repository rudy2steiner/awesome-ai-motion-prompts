# MotionVault: Rain Ripples

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L138) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L138)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called RainRipples using React + plain Canvas 2D (no extra libraries). A dark (zinc-950) canvas fills its container (absolute inset-0, cursor crosshair, DPR-aware sizing via ResizeObserver, clamp DPR to 2) with a faint horizon line (rgba(255,255,255,0.06)) at 70% height marking the water surface. Rain drops spawn at random x positions every 80-200ms and fall as short 6px white streaks (alpha 0.5, 11-15 px/frame); where each lands on the horizon, spawn an expanding ellipse ripple (radius 0 -> 46px, ry = 0.32 * radius for perspective, fading over 1.2s) plus a tiny 2-droplet splash. On click, a BIG drop (12px streak, brighter, accelerating to 14 px/frame) falls at the click x and lands at max(clickY, horizon + 6), producing 3 staggered concentric ripples (120ms apart, radius up to 64px) and a spray of 12 splash droplets in an upward fan with gravity 0.22. Quiet rainy-night mood, all strokes thin and white. Clean up requestAnimationFrame, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
