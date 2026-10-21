# MotionVault: Wobble Input

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L57) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/spring.ts#L57)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called WobbleInput using React + Tailwind CSS + Framer Motion. A login-ish row: a password input (h-10 w-52, rounded-lg, 1px zinc-300 border, placeholder '输入密码') next to a dark '登录' button (bg-zinc-950, white text). Clicking 登录 with any input runs the classic error shake on the whole row via useAnimationControls: x keyframes [0, -10, 10, -6, 6, -2, 0] over 400ms easeInOut. Simultaneously the input border flashes rose-500 for 800ms (state + setTimeout clearing it, transition-colors duration-300), and a small hint '密码错误，再试一次' (12px, text-rose-500) slides down below the row inside an overflow-hidden container (y -8 → 0, opacity 0 → 1, spring stiffness 400 damping 22, wrapped in AnimatePresence). Focusing the input again resets everything — border back to zinc-300, hint exits.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
