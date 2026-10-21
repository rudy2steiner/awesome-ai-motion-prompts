# MotionVault: Uplink

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L108) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L108)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Uplink using React + Tailwind CSS + Framer Motion. Center a column in the preview: on top a small lucide ArrowUp icon (h-3.5 w-3.5, strokeWidth 2.5, zinc-950) that each cycle slides y 4 → -7 while fading opacity 0 → 1 → 0 (1.4s, easeOut, times [0, 0.55, 1], infinite). Below it, a row of five signal-strength bars (w-1.5 rounded-full, items-end, 6px gap) with ascending heights 10/16/22/28/34px. Over a 1.4s infinite cycle each bar animates backgroundColor keyframes zinc-200 → zinc-950 → zinc-950 → zinc-200 (times [0, 0.18, 0.78, 1], easeInOut) with a 110ms stagger per bar (delay = i * 0.11) so they light up in sequence from weak to strong then all extinguish together. Gate all animations behind an IntersectionObserver in-view flag (render bars at zinc-200 and the arrow static when off-screen) and respect prefers-reduced-motion. Add a mono uppercase 'uplink' caption (11px, zinc-400) below.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
