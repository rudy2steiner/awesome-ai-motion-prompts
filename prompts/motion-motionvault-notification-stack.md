# MotionVault: Notification Stack

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L49) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/layout.ts#L49)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called NotificationStack using React + Tailwind CSS + Framer Motion that mimics the iOS notification stack. Render 3 notification cards (300px wide, 64px tall, white, rounded-2xl, 1px zinc-200 border, soft shadow 0 8px 24px -10px rgba(0,0,0,0.12)) absolutely positioned at the top of a relative 300px × 230px wrapper. Each card shows a 28px muted-pastel avatar dot, a 12.5px medium title (zinc-800), a short zinc-100 text bar, and a mono 10px zinc-400 timestamp on the right ("现在" / "5 分钟前" / "1 小时前"). Collapsed state: card i sits at translateY i*9px and scale 1 - i*0.05 with transform-origin top center, so only two hairline edges peek out behind the front card, and a small dark badge (zinc-950 circle, white mono "3") sits at the front card's top-right corner. On wrapper hover toggle a boolean in useState and animate every card with a spring (stiffness 300, damping 24) to translateY i*74px at scale 1, staggered 60ms per card (reverse the stagger to 40ms when collapsing); the badge fades and scales out in 200ms. On mouse leave the stack springs back into the pile. Transform and opacity only for a smooth 60fps feel.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
