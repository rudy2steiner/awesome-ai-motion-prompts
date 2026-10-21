# MotionVault: Keycap

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L190) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L190)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called KeycapCard using React + Tailwind CSS + Framer Motion. Render a big mechanical keycap (128×128px) centered on the preview: a darker zinc-300 side/bottom layer (rounded-2xl, same size, translated 8px down so it peeks out as an extruded lip) behind a zinc-100 top face (rounded-2xl, 1px zinc-200 border) carrying a big mono letter 'K'. The top face holds an inset dished surface (an inner rounded-xl zinc-50 panel with shadow-[inset_0_3px_10px_rgba(0,0,0,0.10)] for a subtle concave key dish). Drive the press with a useMotionValue y smoothed by useSpring (stiffness 500, damping 25): on pointerdown set y to 8 so the top face physically translates down 8px and covers the side lip (the extrusion visually shrinks to zero); on pointerup / pointerleave / pointercancel set y back to 0. Derive the drop shadow from the same spring via useTransform — a soft 14px blur shadow at rest collapsing to a tight 2px contact shadow when fully depressed — for a satisfying click feel. Add a tiny mono counter below ('×N') that increments per press. Transform and opacity only, no setState in pointermove.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
