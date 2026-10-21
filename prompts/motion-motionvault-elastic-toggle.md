# MotionVault: Elastic Toggle

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L67) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L67)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ElasticToggle using React + Tailwind CSS + Framer Motion + the Sun and Moon icons from lucide-react. A toggle switch (role='switch'): a 56×32 rounded-full track that tweens its background zinc-200 ⇄ zinc-950 over 250ms, with a 24px white knob (rounded-full, shadow-sm). The knob slides x 0 → 24 on a spring (stiffness 500, damping 28). While sliding the knob STRETCHES: nest the visible knob inside the sliding wrapper and drive it with useAnimationControls on every toggle — scaleX keyframes [1, 1.4, 1] and scaleY [1, 0.78, 1] over 450ms (times [0, 0.45, 1], easeOut) so it becomes a horizontal ellipse mid-travel then squashes back. Bonus: tiny 12px sun/moon icons crossfade inside the knob (opacity + scale + ±90° rotate, 200ms) — sun when off, moon when on. Transform/opacity only, centered on a light preview.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
