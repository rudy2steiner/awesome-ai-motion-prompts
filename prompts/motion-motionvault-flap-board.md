# MotionVault: Flap Board

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L216) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L216)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called FlapBoard using React + Tailwind CSS + Framer Motion. It mimics a Vestaboard / airport departure board cycling through three 8-column words ('DEPARTED' → 'ARRIVALS' → 'BOARDING') every 4s on a setInterval gated by an IntersectionObserver (pause off-screen, clean up on unmount). Each of the 8 columns is a dark tile (44x64px, bg zinc-900, rounded-md, inset white/8 top highlight + soft black drop shadow) holding a white monospace 26px glyph, with a 1px black/70 horizontal hinge line across the tile's vertical center and a faint white gradient shading on the upper half. On every word change each tile replays a vertical flap tween with Framer Motion — scaleY keyframes [1, 0, 1], duration 360ms, times [0, 0.5, 1], ease-in-out, remounted via a key containing the cycle tick + column index — with a 60ms delay per column for a left-to-right ripple. Mid-flip the glyph swaps: a setTimeout at ~42% of the tween shows one random glyph from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ#%&/', then at ~58% it lands on the target character, timed to the same per-column stagger. Above the board render a tiny caption 'FLIGHT BOARD · GATE 07' (11px mono, uppercase, tracking 0.22em, zinc-500). Dark zinc-950 preview background, animate transform/opacity only, aria-label announces the current word.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
