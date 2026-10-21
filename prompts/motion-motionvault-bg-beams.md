# MotionVault: Background Beams

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L162) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L162)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called BackgroundBeams using React + Tailwind CSS + inline SVG with declarative SMIL (Aceternity Background Beams, restrained monochrome). A full-bleed SVG (viewBox 0 0 800 500, preserveAspectRatio "none", absolute inset-0) over a white base holds 5 gently S-curved paths dropping from the top edge to the bottom (e.g. M 90 -10 C 150 130, 40 300, 110 510), stroked 1px in zinc-200 (#E4E4E7) with vector-effect non-scaling-stroke. Along each path travels a short bright pulse — a 2.6px zinc-400 dot wrapped in a 9px rgba(161,161,170,0.12) halo — driven by animateMotion with an mpath reference, looping on staggered durations 4.2-6.9s with negative begin offsets so the phases never align. Pair each animateMotion with an opacity animate (values 0;1;1;0, keyTimes 0;0.12;0.85;1, same dur/begin) so pulses fade in at the top and out at the bottom. No JS, no rAF, no timers. Overlay a centered mock heading (zinc-900 title + mono caption, pointer-events-none) for readability.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
