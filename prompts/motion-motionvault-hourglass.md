# MotionVault: Hourglass

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L118) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/loader.ts#L118)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Hourglass using React + Tailwind CSS + Framer Motion. Center a 40×45 SVG hourglass (viewBox '0 0 32 36'): an outline drawn with one zinc-950 1.6px path — top cap 'M 5 2 H 27', bottom cap 'M 5 34 H 27', and two apex-to-apex triangles 'M 6 2 L 26 2 L 16 18 Z' / 'M 6 34 L 26 34 L 16 18 Z' (fill none, round joins). Inside, two zinc-950 sand polygons: the upper sand 'M 8.5,4.5 23.5,4.5 16,16.5' with transformBox fill-box and transformOrigin '50% 100%' draining scaleY 1 → 0, and the lower sand '8.5,31.5 23.5,31.5 16,19.5' with the same origin filling scaleY 0 → 1 — both over 1.05s with 0.45s delay, easeIn. A cycle counter state advances every 1.6s via setInterval in useEffect gated by an IntersectionObserver in-view flag; the whole SVG sits in a motion.div animating rotate to cycle * 180deg with a spring (stiffness 160, damping 15 — visible settle wobble), and the sand polygons are keyed by the cycle so they reset while the flip hides the swap. Loop forever. Respect prefers-reduced-motion by rendering a half-full static hourglass. Mono uppercase 'hourglass' caption (11px, zinc-400) below.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
