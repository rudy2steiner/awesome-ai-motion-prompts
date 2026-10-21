# MotionVault: Image Trail

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L170) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L170)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ImageTrail using React + plain Canvas 2D (no extra libraries). A light canvas fills its container (absolute inset-0, cursor crosshair, DPR-aware sizing via ResizeObserver, clamp DPR to 1.75). On pointermove compute cursor speed (dist/dt in px/ms); only when speed exceeds ~0.9 px/ms AND distance from the last spawn exceeds 14px, stamp one ghost at the cursor: alternate circles and squares, size 9-23px, random rotation, mostly zinc greys (#A1A1AA/#71717A/#52525B/#D4D4D8) with a ~10% chance of amber #F59E0B. Each ghost lives 800ms: scale pops in over the first 110ms, then shrinks to 65% while alpha fades 0.9 to 0; draw squares via save/translate/rotate/fillRect. Cap the live list at 60 ghosts (drop oldest). Slow movement spawns nothing. Clean up requestAnimationFrame, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
