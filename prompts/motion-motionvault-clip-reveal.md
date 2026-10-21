# MotionVault: Clip Reveal

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L82) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/scroll.ts#L82)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ClipReveal using React + Tailwind CSS + Framer Motion. Use the internal-scroll-container pattern: a 320px overflow-y auto viewport (overscroll-contain, thin custom scrollbar, page scroll untouched) with an 800px track and a sticky full-viewport panel on white. The panel holds a CSS-only "photograph" of a valley: a sage sky gradient (linear-gradient 180deg #e6ede4 → #f2efe2 → #faf9f4), a soft radial cream sun top-right, three full-width mountain-ridge layers drawn with clip-path polygons filled back-to-front #bccabc / #8ba08c / #49564c, and a white mist gradient at the bottom. Wrap the photo in an absolutely-positioned inset-0 motion.div whose clipPath is scrubbed via useTransform on useScroll({ container }) scrollYProgress from 'inset(45% 42% 45% 42% round 12px)' to 'inset(0% 0% 0% 0% round 12px)' over [0.08, 0.62] — it starts as a thin center strip and expands to full bleed. Inside the clip, scale the scene 1.18 → 1 over the same range for subtle parallax. Overlay a bottom-left caption (mono uppercase 'VALLEY · 山谷' in white/80, semibold white title '揭幕时刻', one white/70 line) that over progress [0.52, 0.8] fades 0→1, rises 16px→0 and sharpens filter 'blur(8px)'→'blur(0px)'. A small mono 'CLIP REVEAL' label top-left fades out over [0.05, 0.2]. All useTransform input ranges strictly increasing within [0,1]. Include the sticky top progress hairline and the fading "向下滚动" hint.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
