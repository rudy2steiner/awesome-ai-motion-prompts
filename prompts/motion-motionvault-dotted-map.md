# MotionVault: Dotted Map

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L120) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L120)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** explainers-data
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DottedMap using React + Tailwind CSS + Framer Motion. It renders a 320x180 viewBox SVG. Dot grid: circles every 10px — precompute in useMemo which dots are 'land' using 3-4 overlapping ellipses (e.g. centers (78,66) rx46 ry32, (150,112) rx30 ry34, (226,62) rx42 ry27, (258,118) rx24 ry19) plus a subtle sine wobble on the radius threshold (1 + 0.12 * sin(x*0.21 + y*0.13)) for organic coastlines; land dots r1.7 fill #3F3F46, ocean dots r1 fill #E4E4E7. Four city dots at (70,58) (148,108) (228,58) (258,112): each is a 3px zinc-950 dot with a 1.2px white core plus a memoized infinite pulse ring (motion.circle, r 3 → 11, opacity 0.5 → 0, 1.6s easeOut repeat Infinity, staggered 0.4s). Three dashed arcs connect the cities — quadratic paths bowed upward ('M 70 58 Q 145 6 228 58', 'M 148 108 Q 196 60 258 112', 'M 70 58 Q 104 116 148 108'), stroke #09090B 1.2px round cap, strokeDasharray '1 6', animating strokeDashoffset 0 → -56 over 2.2s linear repeat Infinity (0.35s stagger) so dashes flow along the arcs. Light background, monochrome zinc only, container aria-label.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
