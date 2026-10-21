# MotionVault: Click Spark

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L149) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L149)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ClickSpark using React + plain Canvas 2D (no extra libraries). A light (zinc-50) canvas fills its container (absolute inset-0, cursor pointer, DPR-aware sizing via ResizeObserver, clamp DPR to 2). On click, burst 8-12 spark streaks from the click point: directions evenly spread over 360deg with random jitter, initial speed 2.2-5.6 px/frame with a slight upward bias. Each spark is drawn as a short round-capped line segment (7-14px long, 1.2-2.1px wide) trailing behind its velocity vector. Colors are mostly zinc-950 #09090B with some zinc-500 #71717A, and roughly 1 in 4 sparks is amber #F59E0B. Sparks feel gravity 0.16 px/frame^2, air drag 0.985, live 480-800ms, fade linearly while their streak length shrinks to zero. Multiple rapid clicks must stack bursts. Show a centered hint text "点击任意位置" (12px zinc-400, pointer-events none). Clean up requestAnimationFrame, ResizeObserver and listeners on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
