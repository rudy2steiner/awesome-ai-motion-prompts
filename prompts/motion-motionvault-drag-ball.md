# MotionVault: Drag Ball

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L127) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L127)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DragBall using React + Tailwind CSS + Framer Motion, running entirely on MotionValues (zero setState). Inside a relative overflow-hidden preview, center a dashed zinc-300 origin ring (44px) and a draggable 36px ball (rounded-full, bg-zinc-950, cursor-grab, active:cursor-grabbing, touch-none). Position is driven by x/y MotionValues: the ball is a motion.div with drag, dragConstraints bound to the preview container ref, dragElastic 0.12, dragMomentum false, style={{ x, y }}. Velocity squash: take vx/vy from useVelocity(x/y) and derive three useTransforms — stretch = 1 + min(mag/1400, 0.5) for scaleX, squash = 1 - min(mag/5200, 0.18) for scaleY, angle = atan2(vy, vx) in degrees (only above a small 60px/s threshold) — applied to an INNER motion.span wrapping the visible ball so drag transform and squash transform never fight. Three ghost trails render behind the ball: memo-less children binding useSpring(x/y) with progressively lazier springs (stiffness 200/150/110, damping 20/18/18) at opacity 0.22/0.13/0.07. On drag end, fly home with animate(x, 0, { type: 'spring', stiffness: 180, damping: 12 }) and the same for y — a visible overshoot past the origin before settling. Light background, transform/opacity only.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
