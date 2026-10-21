# MotionVault: Pixel Snow

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L159) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L159)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called PixelSnow using React + plain Canvas 2D (no extra libraries). A dark (zinc-950) canvas fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Spawn square pixel flakes (2, 3 or 4 px, fillRect, no arcs) with count scaling to container width (clamp(width/6, 40, 140)). Each flake falls at 0.35-1.2 px/frame, sways horizontally on a sine (amplitude 4-18px, period 2.4-6s, random phase), and has its own whiteness (lerp channel value 212-255) and alpha (0.35-0.95). Paint a soft bottom gradient (rgba(228,228,231,0) to 0.14 over the bottom ~14px) suggesting an accumulated snow layer; flakes fade out over the last 40px above that ground line, then respawn just above the top edge with fresh random parameters. Clean up requestAnimationFrame and the ResizeObserver on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
