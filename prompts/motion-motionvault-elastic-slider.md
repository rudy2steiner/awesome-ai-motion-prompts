# MotionVault: Elastic Slider

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L87) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L87)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ElasticSlider using React + Tailwind CSS + Framer Motion. A horizontal slider inside a light preview: a 4px rounded-full zinc-200 track (flex-1), a zinc-950 fill bar, a 24px white knob (rounded-full, subtle border + shadow-sm, cursor-grab), and a mono numeric readout (0-100) on the right. Drive the knob with a MotionValue x bound to drag (drag='x', dragConstraints { left: 0, right: trackWidth - 24 } measured via ResizeObserver, dragElastic 0, dragMomentum false). The fill does NOT track x directly — it follows useSpring(x, { stiffness: 140, damping: 22, mass: 0.8 }) so it lags elastically behind the knob, rendered as percentage width via useTransform. While dragging, the knob stretches in the drag direction (scaleX 1.3, scaleY 0.85, 150ms easeOut); on drag end it jelly-bounces back with keyframes scaleX [1.3, 1] / scaleY [0.85, 1] on a spring (stiffness 500, damping 12). Pointer-down on the track springs the knob to that position (animate(x, target, { type: 'spring', stiffness 400, damping 30 })) with the same squash keyframes. Render the readout by passing a rounded useTransform MotionValue directly as a motion.span child — zero per-frame setState.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
