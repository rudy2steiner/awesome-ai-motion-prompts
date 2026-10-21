# MotionVault: Wave Text

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L112) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L112)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React wave-text component: each letter of the string continuously
oscillates vertically (±8px) following a sine wave — phase offset per letter
index × 0.35, period 1.6s, plus a subtle scale 1→1.08 in sync. Implement
with requestAnimationFrame or Framer Motion animate loops. On hover, double
the wave speed, easing back on leave. Tailwind styling.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
