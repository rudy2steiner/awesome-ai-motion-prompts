# MotionVault: Text Pressure

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L237) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L237)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called TextPressure using React + Tailwind CSS + Framer Motion. It renders one large word ('PRESSURE', 48-60px, semibold, uppercase, system sans font, zinc-950) as inline-block per-character spans. Track the pointer with two useMotionValue numbers (x, y relative to the container, parked at -9999 on pointerleave) smoothed by useSpring (stiffness 260, damping 26, mass 0.6) — onPointerMove writes px.set/py.set, NO React state, zero re-renders. Each character measures its own untransformed center once on mount (getBoundingClientRect relative to the container, stored in a shared ref array) and derives its style with useTransform over [sx, sy]: proximity = max(0, 1 - distance / 180px), then fontVariationSettings string interpolates 'wght' 400→900, fontStretch 100%→125%, and scaleX 1→1.12 as a width fallback for non-variable fonts. Bind all three via the motion.span style prop (fontVariationSettings, fontStretch, scaleX) so weight and width swell elastically around the cursor and relax as it moves away. cursor-crosshair, select-none, transform + font-variation-settings only, light background, container aria-label.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
