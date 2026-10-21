# MotionVault: Orbit

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L58) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L58)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called OrbitLoader using React + Tailwind CSS + Framer Motion. Two 8px zinc-950 dots orbit a center point in opposite directions (radius 18px, one revolution per 1.2s, linear infinite). Implement each orbiter as a zero-size motion.div at the center that rotates 0 → 360deg (the second 0 → -360deg, phase-offset by 180deg so they start opposite each other). Inside each rotator, render the main dot plus 6 ghost dots as a comet trail: each ghost sits 14deg further behind along the path with decreasing size (6.5 → 2.5px) and opacity (0.45 → 0.06), so the trail fades as the whole group spins. Add a tiny 4px zinc-300 dot at the center as the anchor point. Transform only. Respect prefers-reduced-motion by rendering two static dots.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
