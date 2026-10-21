# MotionVault: Line Shadow

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L297) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L297)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called LineShadowText using React + Tailwind CSS + Framer Motion. It renders 'SHADOW' at 72px, font-bold, tracking -0.02em, zinc-950, each glyph in a relative inline-block. Under every glyph render a fan of 12 hairline vertical lines (w-px, bg-zinc-950, flex row with 3px gap, absolutely positioned just below the baseline, centered on the glyph) wrapped in a mask-image linear-gradient(to bottom, black 35%, transparent 96%) so the fan fades out at its foot. Line heights vary from 34px at the edges to 56px in the middle of each fan (light-falloff profile). Every line is a motion.span with origin-top animating scaleY [0.25, 1, 0.25] and opacity [0.12, 0.65, 0.12] — duration 2.4s, ease-in-out, repeat Infinity, delay = charIndex * 0.16s + lineIndex * 0.06s — so the shadow grows downward and breathes in staggered waves, a print-plate illusion. transform (scaleY) and opacity only, will-change-transform, aria-label on the word, glyphs aria-hidden, light background.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
