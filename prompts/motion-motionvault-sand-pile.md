# MotionVault: Sand Pile

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L233) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L233)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called SandPile using React + plain Canvas 2D (no extra libraries). A light (zinc-50 #FAFAFA) canvas fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Run a falling-sand cellular automaton on a coarse grid (cell 5px, stored in a Uint8Array, updated bottom-up each tick): a grain falls straight down if the cell below is empty, else slides down-left or down-right (random order) if empty, else rests — piles grow natural ~34-degree angle-of-repose slopes. Three fixed spouts near the top (at 25% / 50% / 75% width) each emit a thin stream (spawn a grain with 60% probability per tick in a 2-cell-wide nozzle). Render grains as filled rects in warm sand tones (amber-200 #FDE68A / amber-300 #FCD34D / amber-400 #FBBF24 picked per grain) over a faint zinc-100 ground shadow. Pointer: while the pointer is down (or moving with buttons pressed), pour a stream from the cursor (3-cell-wide nozzle, 90% per tick); on a single click without drag, excavate — clear grains in a 5-cell radius so slopes collapse and re-settle. Cap live grains at ~5200 (stop spouts when full); every 14s quietly dissolve the bottom row to make room. Pure rAF loop (tick the automaton every other frame for a calm pace); clean up the loop, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
