# MotionVault: Draw Check

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L50) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L50)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DrawCheck using React + Tailwind CSS + Framer Motion. It renders a 64x64 SVG (viewBox 64) inside a rounded-full button. Sequence on mount: 1) a circle outline (radius 27, 2.5px zinc-950 stroke, round cap, rotated -90deg) draws itself via pathLength 0 to 1 over 0.6s ease-in-out; 2) a check mark path 'M 21 33 L 28.5 40.5 L 44 24' (3px zinc-950, round caps/joins) draws via pathLength 0 to 1 over 0.35s at 0.6s delay; 3) at ~0.95s the wrapping motion.g pops with a slight overshoot — scale keyframes [1, 1.12, 1] over 0.35s, transform origin 50% 50% — while a same-radius circle filled #16A34A fades to opacity 0.08 as a subtle success tint. Clicking the button increments a runId in state and keys the svg on it so the whole sequence replays. Light background, animate pathLength/opacity/transform only.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
