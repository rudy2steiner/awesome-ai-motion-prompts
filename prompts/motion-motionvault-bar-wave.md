# MotionVault: Bar Wave

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L38) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L38)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called BarWave using React + Tailwind CSS + Framer Motion. Five vertical bars in a row (w-1 rounded-full bg-zinc-800, 6px gap, transformOrigin center) with heights peaking in the middle: 24, 32, 40, 32, 24px. Each bar animates scaleY keyframes [0.3, 1, 0.3] over 900ms with easeInOut, repeating infinitely, staggered by 100ms per bar (delay = index * 0.1) so the wave ripples left to right like an equalizer. Transform only. Respect prefers-reduced-motion by rendering the bars static.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
