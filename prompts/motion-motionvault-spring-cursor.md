# MotionVault: Spring Cursor

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L97) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L97)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called SpringCursor using React + Tailwind CSS + Framer Motion, running entirely on MotionValues (zero setState, zero re-renders). Inside a relative preview container (cursor-none, overflow-hidden), onPointerMove writes pointer coordinates (relative to the container rect) into mx/my MotionValues. Two followers: a 20px solid dot (h-5 w-5, rounded-full, bg-zinc-950) bound to useSpring(mx, { stiffness 500, damping 28 }) so it sticks tight to the pointer, and a 40px stroked ring (h-10 w-10, rounded-full, 1.5px zinc-950 border) bound to useSpring(mx, { stiffness 150, damping 15 }) so it trails lazily behind. Center each shape on the pointer with useTransform offsets (-10 / -20) instead of Tailwind translate classes. Derive the ring's ellipse stretch from useVelocity on the ring springs: scaleX = 1 + min(|vx| / 1600, 0.45), scaleY = 1 + min(|vy| / 1600, 0.45). A centered helper text ('移动鼠标，悬停这段文字试试', text-sm zinc-500) scales the ring 1.6x on hover: multiply the stretch by a hoverScale MotionValue driven by animate(hoverScale, 1.6 | 1, { type: 'spring', stiffness 300, damping 18 }) via computed useTransform. Fade both shapes in/out (opacity MotionValue) on pointer enter/leave, and initialize mx/my to the container center on mount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
