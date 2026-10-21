# MotionVault: Draw Icons

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L30) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L30)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DrawIcons using React + Tailwind CSS + Framer Motion. It renders a row of 4 minimal line icons — mountain+sun, wave, leaf, star — each inside a 56px rounded-xl tile with a 1px zinc-200 hairline border on white. Each icon is a 24x24 viewBox SVG made of 1-2 strokes (e.g. mountain: 'M3 18 L9 8 L13 14 L16 10 L21 18' plus a small circle for the sun; wave: two stacked sine curves; leaf: a closed leaf outline plus a vein; star: a 5-point star polygon path), stroke #09090B, strokeWidth 1.5, round caps, no fill. On mouse enter of a tile, increment a runId in that tile's state and key the svg on it so all strokes remount and draw sequentially: each motion.path (or motion.circle) animates pathLength 0 to 1, 300ms each, staggered by 120ms. On mouse leave do nothing — the icon stays fully drawn; hovering again re-runs the draw. Tiles are independent (own state), centered in a light preview with 16px gaps.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
