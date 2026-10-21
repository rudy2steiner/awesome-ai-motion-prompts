# MotionVault: Border Trail

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L100) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L100)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called BorderTrail using React + Tailwind CSS + Framer Motion. It renders a 296x168px card: an absolutely-positioned SVG (viewBox 296x168) draws a rounded rect (x 1, y 1, width 294, height 166, rx 16) three times. First rect is the static base — white fill, 1px stroke #E4E4E7 (zinc-200). Second is the travelling bright arc: motion.rect with no fill, 1.5px stroke #09090B (zinc-950), round line cap, and the pathLength normalization trick — pathLength={100}, strokeDasharray '9 91', then animate strokeDashoffset from 0 to -100 over 3.2s with ease linear and repeat Infinity so a short bright segment orbits the border seamlessly. Third is a fainter companion arc half a lap behind: same rect, 1px stroke #A1A1AA (zinc-400), strokeDasharray '5 95', strokeDashoffset animating from -50 to -150 on the same 3.2s linear infinite timeline. Centered inside the card, static content: 'BORDER TRAIL' (14px mono, font-medium, uppercase, tracking 0.24em, zinc-950) over a small sub-caption 'STROKE-DASHOFFSET LOOP' (11px mono, uppercase, tracking 0.18em, zinc-400). Light background, animate stroke-dashoffset only, container aria-label.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
