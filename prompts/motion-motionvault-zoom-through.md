# MotionVault: Zoom Through

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L52) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L52)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ZoomThrough using React + Tailwind CSS + Framer Motion. Use the internal-scroll-container pattern (320px overflow-y auto viewport, overscroll-contain, thin scrollbar, never page scroll) with a ~3× track (1000px) and a sticky centered stage on a zinc-50 background. Stack 4 white cards (230px wide, rounded-xl, border, soft shadow, big mono number 01–04 + Chinese title + one line) absolutely centered with fixed z-index (front card highest). For card i, map useScroll({ container }) scrollYProgress with useTransform: scale [ (i-1)/4, i/4, (i+1)/4 ] → [0.7, 1, 2.8] and opacity [(i-0.55)/4, i/4, (i+0.55)/4, (i+0.95)/4] → [0, 1, 1, 0], so each card grows from the depths, flies past the camera and fades, revealing the next; the last card stops at scale 1 and stays. Smooth scrub, transform/opacity only. Include the top progress hairline and fading "向下滚动" hint.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
