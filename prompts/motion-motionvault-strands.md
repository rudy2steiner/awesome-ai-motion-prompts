# MotionVault: Strands

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L130) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/svg.ts#L130)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Strands using React + Tailwind CSS (no Framer Motion needed — drive it with requestAnimationFrame). It renders a 320x180 viewBox SVG with 6 horizontal cubic-bezier strands. Strand i sits at baseY = 44 + i*18 and its path is 'M 6 baseY C 92 c1 228 c2 314 baseY' where the control points ride phase-offset sine waves: c1 = baseY + 13 * sin(t*1.25 + i*0.75), c2 = baseY + 13 * sin(t*1.25 + i*0.75 + PI*0.66). Keep an array of path refs; each rAF frame recompute every strand's d and write it via setAttribute directly (round to 2 decimals, zero React state, 60fps). Strand index 2 is the lead — stroke #09090B strokeWidth 1.6 full opacity; the other five are #A1A1AA (zinc-400) at 1px and 0.75 opacity. All round line caps, no fill. Gate the loop with an IntersectionObserver-based useInView hook so it only runs while visible; cancelAnimationFrame on cleanup. Center the svg (max-width ~380px) on a light background, container aria-label.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
