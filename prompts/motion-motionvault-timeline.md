# MotionVault: Scroll Timeline

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L62) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L62)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** explainers-data
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Timeline using React + Tailwind CSS + Framer Motion. Render an internal scroll container (320px, overflow-y auto, overscroll-contain, thin custom scrollbar — page scroll never hijacked) holding an 880px-tall relative column. Down the center: a 1px zinc-200 hairline, and a zinc-950 fill line whose scaleY (origin-top) is bound directly to useScroll({ container }) scrollYProgress so the ink grows top→bottom with scroll. Place 5 milestone nodes (2021–2025: mono year, semibold Chinese title, one-line description) at 8%/29%/50%/71%/92% of the track, alternating left/right of the line (cards w-[calc(50%-22px)], small white bordered cards with soft shadow). Each node is a micro-component mapping progress around its threshold: card opacity 0→1 and scale 0.8→1 over [at-0.07, at] (transform-origin toward the line), and a centered dot on the line that scales 0.5→1 and fills from white to #09090b over [at-0.04, at]. Top progress hairline + fading "向下滚动" hint. Transform/opacity only.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
