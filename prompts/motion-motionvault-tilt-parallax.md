# MotionVault: Tilt Parallax

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L160) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L160)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called TiltParallaxCard using React + Tailwind CSS + Framer Motion. Render a white card (288×192px, rounded-2xl, 1px zinc-200 border, soft shadow, overflow hidden) centered in a wrapper with CSS perspective 900px. Track the pointer with onPointerMove, normalize to [-1,1] on both axes into useMotionValue, smooth with useSpring (stiffness 160, damping 20), and derive rotateX/rotateY in ±8deg via useTransform, applied with transformStyle preserve-3d; spring back to 0 on pointer leave. Inside, translate three layers at different depths, all bound to the same springs with no setState in the pointer path: a background layer (two soft blurred gradient blobs, indigo-200/60 and rose-200/60) moving at 0.3× (±9px, translateZ 0), a mid content card (white/85 backdrop-blur inner panel with skeleton lines) at 0.6× (±18px, translateZ 30px), and a foreground badge + title (black pill chip with mono uppercase text plus a semibold title) at 1.0× (±30px, translateZ 60px). Finish with a soft glare sweep: an absolutely positioned motion.div whose radial-gradient highlight (white 0.85 fading to transparent at 55%) follows the pointer via useTransform, sitting at translateZ 80px.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
