# MotionVault: Pixel Trail

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L190) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L190)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called PixelTrail using React + plain Canvas 2D (no extra libraries). A light canvas fills its container (absolute inset-0, cursor crosshair, DPR-aware sizing via ResizeObserver, clamp DPR to 1.75). The pointer stamps an 8px grid: on pointermove snap the cursor to cell (floor(x/8), floor(y/8)) and record it in a Map keyed "cx,cy" with a birth time; skip re-stamping a cell that is less than half-way through its life. Each cell draws as a 7x7px square (0.5px inset hairline gap) fading from 0.9 alpha to 0 over 1200ms, then is deleted — continuous movement leaves a dashed snake of pixels. Colors: mostly zinc-800 #27272A with some zinc-700/zinc-600, ~8% amber #F59E0B. Cap the map at 240 cells (evict oldest). Clean up requestAnimationFrame, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
