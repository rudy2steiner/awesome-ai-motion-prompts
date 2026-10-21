# MotionVault: Day Night Cycle

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L130) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L130)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called DayNight using React + Tailwind CSS with scoped CSS keyframes (inline <style> tag, 16s linear infinite cycle). Stack four absolutely positioned sky layers and crossfade them with opacity keyframes: dawn (soft peach linear-gradient #FCE9D8 → #F5AE8B, visible 0-25%), noon (pale sky #D9ECF9 → #F1F8FD, 25-50%), dusk (warm violet #B99BD6 → #F0A184, 50-75%), night (deep zinc-950 #09090B → #17171B, 75-100%) with ~8% crossfade overlaps so colors interpolate smoothly. Add a stars layer (tiny 1-1.5px white radial-gradient dots scattered over the upper half) that fades in only during night. A small sun disc (24px, radial #FDE9C8 → #F9B45C with a warm box-shadow glow) sits at the top of a full-size arm whose transform-origin is 50% 150% — rotating the arm from -78deg to 78deg sweeps the sun across the sky in an arc, fading in/out near the horizons during the dawn→dusk half; a smaller moon (20px, #FAFAFA → #D4D4D8) does the same during the night quarter. Transform-only animation. Place mock content (small heading + outline button) on top with mix-blend-difference and white text so the foreground automatically reads dark on light skies and light on the night sky.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
