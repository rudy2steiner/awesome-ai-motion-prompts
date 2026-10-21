# MotionVault: Pinned Steps

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L42) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L42)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called PinnedSteps using React + Tailwind CSS + Framer Motion. Inside an internal scroll container (320px, overflow-y auto, overscroll-contain, thin scrollbar) place a 3.5×-tall track (1120px) with a sticky split panel. Left: a mock UI card (rounded-xl, border, soft shadow, window dots, big mono word DRAFT/BIND/SHIP, accent bar in muted sage/khaki/zinc) that morphs between three variants with a 300ms opacity+scale crossfade. Right: a masked column of three step descriptions (title + one line) that glides vertically in three steps via useTransform on useScroll({ container }) scrollYProgress with pauses at each stop. Derive the active index from scrollYProgress with useMotionValueEvent (threshold-only setState); the active step is zinc-950, inactive zinc-300, with 300ms color transitions. Add three indicator dots on the right edge (active: zinc-950, scale-125). Top progress hairline + fading "向下滚动" hint included.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
