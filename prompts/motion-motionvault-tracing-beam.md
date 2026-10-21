# MotionVault: Tracing Beam

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L102) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L102)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called TracingBeam using React + Tailwind CSS + Framer Motion. Use the internal-scroll-container pattern: a 320px overflow-y auto viewport (overscroll-contain, thin custom scrollbar — page scroll never hijacked) holding a 900px article. The article (pl-16) has a mono uppercase caption, a semibold Chinese title, one intro line, then 4 sections, each with a small zinc-950 heading bar and 2–4 rounded placeholder text bars (h-2, zinc-200, varied widths) plus one bordered image placeholder block. Sticky beside it (pointer-events-none sticky top-0 h-0 wrapper, absolutely positioned at left-2 top-5) render a 40×280 rail: an SVG viewBox '0 0 40 280' with an S-curve path ('M 20 4 C 36 44, 4 76, 20 108 C 36 140, 4 172, 20 204 C 34 234, 8 254, 20 276') drawn twice — a zinc-200 track and a zinc-950 beam whose pathLength is bound directly to useScroll({ container }) scrollYProgress so the ink draws with scroll. Ride a glowing dot on the path head: a wrapper div with a blurred zinc-950/25 halo plus a 8px zinc-950 core, positioned by reading path.getTotalLength()/getPointAtLength(progress * len) inside useMotionValueEvent and writing the translate transform straight onto the element — zero re-renders. All useTransform input ranges strictly increasing within [0,1]. Include the sticky top progress hairline and the fading "向下滚动" hint.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
