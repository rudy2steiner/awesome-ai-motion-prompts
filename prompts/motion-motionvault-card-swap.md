# MotionVault: Card Swap

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L180) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L180)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called CardSwap using React + Tailwind CSS + Framer Motion. Render three stacked cards (320×128px, rounded-xl, 1px zinc-200 border, subtle gradient faces with a small accent bar, mono uppercase label, title, and two skeleton lines) absolutely positioned in a fixed wrapper. Drive the cycle with a reordered id array in state: every 3 seconds a setInterval (only running while the component is in view via IntersectionObserver) moves the front id to the back. Each card is a motion.div keyed by id with initial={false}, animating to its slot values — front: y 0, scale 1, opacity 1, zIndex 30; middle: y 14, scale 0.95, opacity 0.85, zIndex 20; back: y 28, scale 0.9, opacity 0.7, zIndex 10. Track the previous order in a ref; the card moving from front to back animates with keyframes instead — y [0, 60, 28], scale [1, 0.97, 0.9], opacity [1, 0.55, 0.7], zIndex [30, 30, 10] over 700ms with times [0, 0.45, 1] — so it drops down 60px and fades slightly before sliding behind the stack, while the other cards step forward with a 500ms ease [0.16,1,0.3,1] tween.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
