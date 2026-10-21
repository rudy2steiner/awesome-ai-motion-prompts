# MotionVault: Beam Path

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L80) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L80)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called BeamPath using React + Tailwind CSS. It renders a 300x160 viewBox SVG containing a dim S-curve rail with a hairpin feel: path 'M 24 120 C 90 120 90 40 150 40 C 210 40 210 120 276 120', stroke #E4E4E7 (zinc-200), strokeWidth 1.5, round line cap, no fill, plus two small terminal dots (r 2.5, zinc-300) at both ends. A bright head dot (r 3.5, fill #09090B zinc-950) travels the rail in a 2.4s seamless loop, trailed by 3 ghost dots (r 3 / 2.5 / 2, opacity 0.32 / 0.18 / 0.09) sitting 16 / 32 / 48 path-units behind the head. Drive the motion with requestAnimationFrame: keep a ref to the rail path, call getTotalLength() once, and each frame compute t = ((now - start) % 2400) / 2400, then position every dot with path.getPointAtLength wrapped modulo the total length so the trail never jumps at the seam — write cx/cy via setAttribute directly on ref'd circles (no React state, 60fps). Gate the loop with an IntersectionObserver so it pauses off-screen and cancelAnimationFrame on cleanup. Center the svg (max-width ~360px) on a light background, monochrome zinc only, container aria-label.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
