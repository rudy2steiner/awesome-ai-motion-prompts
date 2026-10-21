# MotionVault: Container Scroll

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L112) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L112)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Tilt3D using React + Tailwind CSS + Framer Motion. Use the internal-scroll-container pattern: a 320px overflow-y auto viewport (overscroll-contain, thin custom scrollbar, never page scroll) with a 680px track and a sticky full-viewport centered stage. Above the card, a title block (mono uppercase 'PRODUCT LAUNCH' caption + semibold Chinese title) drifts y 0 → -44 and fades opacity 1 → 0 over progress [0, 0.35]. Below it, wrap a 280px mock app screenshot card in a div with style perspective 900px; the card itself is a motion.div with transformStyle preserve-3d whose rotateX maps scrollYProgress [0.08, 0.6] → [24, 0] degrees, scale [0.88, 1] and y [24, 0] — it starts tilted back like a product-launch hero and flattens to a straight-on view as you scroll. The screenshot is pure CSS: a window chrome bar (zinc-50, three zinc-300 dots, a zinc-200 address pill), then a flex body — a 56px sidebar (zinc-50, stacked bars, one zinc-300 active) and a main pane with a zinc-800 title bar, two zinc-200 text bars and three small gradient thumbnails (zinc-100 → zinc-300). Rounded-xl, 1px zinc-200 border, soft shadow-xl. All useTransform ranges strictly increasing inside [0,1]; transform/opacity only. Top progress hairline + fading "向下滚动" hint included.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
