# MotionVault: Chase Ring

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L128) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L128)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called ChaseRing using React + Tailwind CSS + Framer Motion. Center a 56px SVG (viewBox '0 0 64 64') with a faint full-circle track (r 26, stroke zinc-100, width 3). On the same ring render two gapped arcs (circumference ≈ 163.4): the LONG arc is a zinc-950 round-cap circle with an animated strokeDasharray breathing between '120 43.4' and '70 93.4' and back (2.4s easeInOut infinite), wrapped in a motion.g (transformBox fill-box, origin center) rotating 0 → 360deg over 1.2s linear infinite, clockwise. The SHORT arc is a zinc-400 round-cap circle with a fixed dasharray '34 129.4' and dashoffset -60, inside another motion.g rotating 0 → -360deg over 0.9s linear infinite — counter-clockwise, slightly faster, so it forever chases the long arc while the long arc's gap breathes. Gate all animations behind an IntersectionObserver in-view flag (render statically when off-screen) and respect prefers-reduced-motion. Mono uppercase 'chase ring' caption (11px, zinc-400) below.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
