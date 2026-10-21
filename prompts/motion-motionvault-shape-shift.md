# MotionVault: Shape Shift

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L48) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L48)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ShapeShift using React + Tailwind CSS + Framer Motion. A 28px square (h-7 w-7 bg-zinc-950) that runs a continuous morph cycle: animate rotate keyframes [0, 90, 180, 270, 360] together with borderRadius keyframes ['4px', '50%', '4px', '50%', '4px'] — square → circle → diamond → circle → square. Each quarter-cycle takes 1.6s (total duration 6.4s, times [0, 0.25, 0.5, 0.75, 1], easeInOut), repeating infinitely with smooth keyframes — the 'morphing loader' seen in premium dashboards. Transform/border-radius only. Respect prefers-reduced-motion by rendering the square static.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
