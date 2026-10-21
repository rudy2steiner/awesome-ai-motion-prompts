# MotionVault: Path Morph

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L60) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L60)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called PathMorph using React + Tailwind CSS + Framer Motion. It renders a 200x200 SVG with a single filled motion.path (fill #09090B at 90% opacity). Craft TWO compatible 'd' strings with the exact same command structure — 8 anchors every 45deg around center (100,100) connected by 8 cubic C segments, closed with Z: a blob (radii alternating 68/58/48/58 with generous tangential control points ~0.42*r) and a 4-point star (radii alternating 70/38 with short control points ~0.16*r producing curved points). Because the structures match, Framer Motion can tween the 'd' attribute directly: toggle a boolean in state every 1.5s (1.2s morph + 0.3s hold, full loop 3s) via setInterval and animate d to the current shape's string with duration 1.2s, ease-in-out; clean up the interval on unmount. Below the shape show a tiny mono uppercase label (text-xs zinc-400) that crossfades between 'BLOB' and 'STAR' with AnimatePresence mode='wait' (y 4px drift, 200ms) so the label always names the current shape. Light background.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
