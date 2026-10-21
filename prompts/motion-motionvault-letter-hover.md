# MotionVault: Letter Hover Bounce

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L146) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L146)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called LetterHover using React + Tailwind CSS + Framer Motion. It renders a word (e.g. 'MotionVault', 32px, font-semibold, zinc-950) with each letter as an inline-block motion.span so transforms work. Track the hovered letter index in state (onMouseEnter per letter, reset to null on container onMouseLeave). The hovered letter springs to scale 1.4, y -8px, and a slight rotate of ±6deg alternating by letter index parity; letters exactly one position away get 15% of that same displacement (scale ~1.06, y ~-1.2px, rotate ~±0.9deg) for a rubber-band pull, and all other letters stay at rest. Use a spring transition with stiffness 500 and damping 15 on every letter so both the jump and the return bounce feel physical. Cursor pointer on the container, will-change-transform on letters, animate transform only for 60fps.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
