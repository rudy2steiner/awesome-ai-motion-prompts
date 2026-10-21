# MotionVault: Spring Modal

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L27) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L27)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called SpringModal using React + Tailwind CSS + Framer Motion. A button '打开弹窗' opens a modal rendered inside a relative preview container (absolute positioning, NOT fixed — the backdrop covers the preview only). The backdrop fades in (opacity 0 → 1, 200ms, bg-zinc-950/20) and closes on click. The modal card (w-[280px], rounded-2xl, white bg, zinc-200 border, title + body text + a full-width dark action button + an ✕ close button) enters with an overshoot spring: initial scale 0.6 / y 40 / opacity 0 animating to scale 1 / y 0 / opacity 1 with type 'spring', stiffness 260, damping 17 — a visible bounce past the target. The card is draggable vertically (drag='y', dragConstraints bound to the preview container ref, dragElastic top 0.05 / bottom 0.4, cursor-grab); on drag end, if the y offset exceeds 100px dismiss it — the exit is a quick drop-down (y 120, opacity 0, 220ms easeIn). Wrap everything in AnimatePresence.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
