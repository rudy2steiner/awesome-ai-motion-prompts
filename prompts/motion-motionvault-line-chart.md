# MotionVault: Line Chart Grow

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L70) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L70)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** explainers-data
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called LineChartGrow using React + Tailwind CSS + Framer Motion. It renders a minimal line chart in a 320x180 viewBox. Three faint horizontal grid lines (1px zinc-200) fade in first, then the two axes (1px zinc-400 lines: x-axis y=145 from x=40 to 292, y-axis x=40 from y=145 to 20) draw in via pathLength 0 to 1 over 200ms. Then a 5-point polyline through (60,118) (108,82) (156,96) (204,58) (252,36) grows left to right: motion.path pathLength 0 to 1, 1.8s ease-out, 2px zinc-950 stroke, round caps/joins, starting at 0.2s delay. Five data dots (r 3.5, white fill, 2px zinc-950 stroke) pop in with a spring (stiffness 500, damping 18) from scale 0, each delayed by its x fraction of the 1.8s line duration ((x-60)/192 * 1.8 + 0.2s) so they appear exactly as the line reaches them. The last dot gets a soft pulse ring: an isolated React.memo micro-component rendering a motion.circle whose r and opacity animate (r 5 to 16, opacity 0.45 to 0) on a 1.4s infinite repeat. After the line completes, a faint area under the line (same polyline closed down to y=145, filled with a vertical linearGradient from zinc-950 at 8% opacity to transparent) fades in over 0.8s. Light background, monochrome zinc only.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
