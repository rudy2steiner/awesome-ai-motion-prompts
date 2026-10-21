# MotionVault: Jelly Checkbox

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L37) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L37)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called JellyCheckbox using React + Tailwind CSS + Framer Motion. A vertical row of 3 custom checkboxes (labels like '接收通知' / '记住登录状态' / '自动同步数据'), each a button with role='checkbox' holding a 22px box (rounded-md, 1px zinc-400 border, white bg) plus a label span. On check: the box squishes with keyframed scale [1, 0.8, 1.1, 1] on a spring (stiffness 500, damping 12) while its background and border tween to zinc-950; inside, a white SVG check path (M1 5.5 L4.5 8.5 L11 1.5, stroke-width 2, round caps) pops in with a tiny overshoot — scale keyframes [0.4, 1.2, 1] over 300ms. The label gets a strike-through: an absolutely positioned 1px line (bg-zinc-400, origin-left) animating scaleX 0 → 1 over 250ms easeOut. On uncheck everything reverses calmly (200ms easeOut, no wobble). Transform/opacity only.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
