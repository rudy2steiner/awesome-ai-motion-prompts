# MotionVault: Morphing Text

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L257) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L257)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called MorphingText using React + Tailwind CSS + Framer Motion. It cycles between two bold words ('灵感' ⇄ '动效', 64px, font-bold, tracking -0.02em, zinc-950) every 1.8s on a setInterval gated by an IntersectionObserver (pause off-screen, clean up on unmount). Both words are absolutely centered inside a fixed-size relative wrapper (e.g. 260x104px flex center) so their different widths never cause layout shift. Wrap the keyed motion.span in AnimatePresence initial={false} and cross-dissolve: incoming word animates from { opacity: 0, scale: 1.18, filter: 'blur(12px)' } to { opacity: 1, scale: 1, filter: 'blur(0px)' }, outgoing to { opacity: 0, scale: 0.85, filter: 'blur(12px)' } — duration 1.1s, ease [0.16, 1, 0.3, 1], so the dissolve finishes well inside the 1.8s cycle for a seamless, never-idle loop. whitespace-nowrap, will-change-transform, wrapper carries an aria-label of the current word; light background.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
