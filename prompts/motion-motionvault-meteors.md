# MotionVault: Meteors

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L84) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/particle.ts#L84)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Meteors using React + plain Canvas 2D (no extra libraries). A canvas fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2) over a zinc-950 dark sky. Paint 40 tiny static stars (0.5-1.4px white dots, opacity 0.15-0.6) as a backdrop. Meteors spawn at staggered random intervals (every 300-900ms, max 8 alive) at a random x along the top (y slightly above the canvas) and travel diagonally about 35deg from vertical at 4-8 px/frame. Each meteor is a glowing 2px white head dot (shadowBlur 8) plus a ~120px tail drawn as a linear gradient stroke fading from rgba(255,255,255,0.6) to transparent opposite the travel direction. Roughly 1 in 5 meteors is larger and brighter (2.6px head, ~170px tail, higher speed). Remove meteors once fully offscreen. Clean up requestAnimationFrame and the ResizeObserver on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
