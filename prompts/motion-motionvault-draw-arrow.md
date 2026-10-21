# MotionVault: Draw Arrow

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L140) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L140)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DrawArrow using React + Tailwind CSS + Framer Motion. It renders a 320x180 viewBox SVG containing a hand-drawn-feel guide arrow. The main curve is a slightly wobbly path from top-left winding to bottom-right: 'M 44 42 C 46 96 96 58 146 88 C 196 118 220 84 262 124', stroke #09090B (zinc-950), strokeWidth 3, round caps/joins, no fill. The arrowhead is a separate path of two short barbs at the tip: 'M 246 122 L 262 124 L 254 108', same stroke styling. Loop both on a 2.7s infinite repeat using pathLength keyframes: the curve animates [0, 1, 1, 0] with times [0, 0.44, 0.81, 1] and per-segment eases [easeInOut, linear, easeInOut] — 1.2s draw, 1s hold, 0.5s backward erase; the head animates [0, 0, 1, 1, 0] with times [0, 0.34, 0.44, 0.8, 1] so it flicks in during the last beat of the draw and erases with the tip. Center the svg (max-width ~360px) on a light background, animate pathLength only, container aria-label.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
