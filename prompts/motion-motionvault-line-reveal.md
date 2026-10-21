# MotionVault: Line Reveal

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L136) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L136)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called LineReveal using React + Tailwind CSS + Framer Motion. It renders a 3-4 line paragraph (15px, zinc-700, generous ~2x line-height) where every line is wrapped in its own overflow-hidden block-level mask. Each line's inner span animates with whileInView from { y: '100%', opacity: 0 } to { y: '0%', opacity: 1 } — duration 500ms, ease-out, with a 120ms stagger via per-line delay. Use viewport={{ once: true, amount: 0.6 }} so the reveal triggers crisply the first time the paragraph scrolls into view and never replays. The mask keeps each line fully hidden until its turn, producing an editorial, gallery-quality reveal. Animate transform and opacity only; keep the text selectable.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
