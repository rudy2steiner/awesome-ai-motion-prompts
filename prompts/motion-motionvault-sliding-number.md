# MotionVault: Sliding Number

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L77) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L77)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called SlidingNumber using React + Tailwind CSS + Framer Motion. A 4-digit counter in a mono font (font-mono, text-5xl, 48px, zinc-950) with leading-zero padding. Each digit is its own column: a 1em-tall window (overflow-hidden, width 0.62em) containing a vertical stack of digits 0-9 (each span exactly 1em tall, leading-none). To change a digit, animate the column's y to -digit em with Framer Motion (initial={false}) using a spring transition (type: 'spring', stiffness 300, damping 24) so the old digit slides up out and the new one slides up in, settling with a soft bounce. Stagger the digits by 40ms from the ones place outward (delay = (length - 1 - index) * 0.04) for an odometer-carry feel. Below the counter, two buttons: a dark '+1' (bg-zinc-950, white text) and an outlined '+10', both with active:scale-95 press feedback. Transform-only animation, centered on a light preview.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
