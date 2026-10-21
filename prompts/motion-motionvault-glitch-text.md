# MotionVault: Glitch Text

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L186) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L186)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called GlitchText using React + Tailwind CSS with a component-scoped <style> block. It renders one word ('GLITCH', monospace, 40px, medium, uppercase, tracking 0.08em, zinc-950) as three stacked layers: the base glyph plus two absolutely-positioned aria-hidden copies (inset-0) colored rose #F43F5E and sky #38BDF8, both at opacity 0 at rest. On hover a state class enables a 600ms burst that runs exactly once per hover (CSS animations, 1 iteration, default fill so everything reverts clean afterward): the rose copy shifts -3px (jittering to -6px), the sky copy +3px (to +6px), both at 0.6 opacity; each copy's visibility is chopped into 3-4 horizontal clip-path inset() slices that jump discretely using animation-timing-function steps(1, end) across 5 keyframes (e.g. inset(8% 0 72% 0) → inset(58% 0 12% 0) → inset(24% 0 52% 0) → inset(78% 0 4% 0)), and the base glyph gets a subtle ±2px translate jitter on the same steps() timing. At 100% every layer returns to opacity 0 / translate 0 so off-burst text is perfectly clean. Re-hovering replays the burst. Transform and opacity only, will-change-transform, light background.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
