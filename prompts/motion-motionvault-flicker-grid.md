# MotionVault: Flicker Grid

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L79) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L79)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called FlickerGrid using React + plain Canvas 2D (no extra libraries) over a white base. Draw a grid of small squares (16px cells, 2px gap) in zinc-900 (#18181B) whose resting opacity is 0.04. Continuously pick random cells and fade each one up to a peak opacity of 0.25-0.5 and back with a smooth sine in/out over a random 1-3s duration, keeping roughly 6% of all cells animating at any time — a calm digital rain of tiles, not flashy. Apply a subtle radial falloff so cells near the center are livelier (full intensity) than the edges (~35%). The canvas fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2). Pure rAF loop at 60fps; clean up the loop and observer on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
