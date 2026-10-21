# MotionVault: Matrix Rain

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L109) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L109)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called MatrixRain using React + plain Canvas 2D (no extra libraries) over a zinc-950 base. An elegant, RESTRAINED matrix rain: columns of tiny 10px monospace glyphs (half-width katakana + digits, 14px column width, 12px row height). Each frame, fill the canvas with translucent black rgba(9,9,11,0.08) so old glyphs fade into trails. Active columns advance their head at only 1.5-3 rows per second (delta-time based), drawing the head glyph in soft white at 80% opacity and the glyph one row behind in zinc-500; only ~60% of columns are ever active, and finished columns respawn at a random negative offset with a fresh random speed. Draw a glyph only when the head crosses into a new row so the fall stays slow and crisp — a whisper of the matrix, not a seizure. Canvas fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2); clean up the rAF loop and observer on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
