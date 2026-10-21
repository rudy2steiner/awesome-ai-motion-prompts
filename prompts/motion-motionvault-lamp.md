# MotionVault: Lamp

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L151) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L151)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called Lamp using React + Tailwind CSS + Framer Motion (Aceternity Lamp effect, inverted to a restrained monochrome). On a zinc-950 stage, place a thin horizontal light line at ~24% from the top: a 1px-tall div (62% width, max 340px) with background linear-gradient(90deg, transparent, rgba(255,255,255,0.9), transparent), expanding with scaleX 0.2 to 1, plus a small bright blurred core (3px, 64px wide, white, blur 2px, box-shadow 0 0 12px 2px rgba(255,255,255,0.6)) at its center. From the line, a conic light cone unfolds downward: a div (width 80%, height 60% of the stage, transform-origin top) with background conic-gradient(from 165deg at 50% 0%, transparent 0deg, rgba(244,244,245,0.16) 13deg, rgba(244,244,245,0.30) 15deg, rgba(244,244,245,0.16) 17deg, transparent 30deg), blurred 10px, animating scaleY 0.15 to 1 with opacity over 0.7s, ease [0.16,1,0.3,1]; add a wide soft radial halo (blur 24px, white at 26% alpha) behind the line. Below, the word 'LAMPLIGHT' in light-weight zinc-100 with 0.45em letter-spacing and a soft white text-shadow floats up (y 16 to 0, opacity 0 to 1, 0.35s delay) after the cone opens. Clicking the stage toggles the lamp off and on, reversing every animation; keyboard accessible (Enter/Space). Compose per-element centering through Framer Motion style x: '-50%' instead of Tailwind translate classes so transforms never conflict.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
