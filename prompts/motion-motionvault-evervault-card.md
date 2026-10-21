# MotionVault: Encrypted Matrix

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L252) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L252)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called EvervaultCard using React + Tailwind CSS + Framer Motion, recreating the Aceternity Evervault effect. Render a white card (340×220px, rounded-xl, 1px zinc-200 border, overflow hidden, cursor-crosshair) filled with a matrix of random glyphs (A–Z, 2–9, #$%&@*+=<>/ — 46 cols × 14 rows, JetBrains Mono 10px, 14px line-height, 2px tracking, rendered as a whitespace-pre <pre>). Render the matrix twice: a dim base layer (zinc-300) that slowly re-rolls every 2.6s, and a lit layer (zinc-950, font-medium) that re-rolls every 140ms. Track the pointer with onPointerMove into useMotionValue x/y (never useState in the pointer path) and build a mask with useMotionTemplate: radial-gradient(130px circle at x y, black 25%, transparent 100%) applied as maskImage/WebkitMaskImage on the lit layer via a motion.pre — so a circular region around the cursor lights up with freshly scrambled dark glyphs like a scanning spotlight. On pointer leave set both MotionValues to −400 so the lit region slides off. Center a small frosted pill chip (white/85, backdrop-blur, hairline border, mono 10px uppercase "ENCRYPTED") as the only static content.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
