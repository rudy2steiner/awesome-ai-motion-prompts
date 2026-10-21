# MotionVault: Stroke Hover

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L110) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L110)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called StrokeHoverText using React + Tailwind CSS + Framer Motion. It renders a 320x140 viewBox SVG with the word 'STROKE' (62px, Inter 700, letter-spacing 0.06em, centered via x=160 textAnchor middle) stacked in three layers. Layer 1 (resting state): the glyph as a pale outline — fill none, 1px stroke #D4D4D8 (zinc-300). Layer 2 (highlight sweep): the same text stroked 2.2px with a low-saturation horizontal linearGradient (transparent zinc-400 → #71717A → #18181B → zinc-400 transparent), wrapped in a <g> carrying an SVG mask whose only content is a 110px-wide motion.rect filled with a soft horizontal white-to-transparent gradient; on hover, increment a runId in state and key the mask rect on it so it remounts and sweeps x from -120 to 330 over 1.15s easeInOut — a soft-edged light band travelling across the strokes. Layer 3 (fill flash): the same text filled #18181B, keyed on runId, animating opacity keyframes [0, 0.9, 0.12] with times [0, 0.55, 1] over the same 1.15s so the fill briefly lights up mid-sweep then settles to a faint tint. Trigger on the wrapper's onMouseEnter (cursor-pointer, select-none), light background, use component-unique gradient/mask ids, container aria-label.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
