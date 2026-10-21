# MotionVault: Holo Glare

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L129) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L129)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called HoloCard using React + Tailwind CSS + Framer Motion. Render a dark card (zinc-900, rounded-2xl, 1px zinc-800 border) centered inside a wrapper with CSS perspective 900px. Track the pointer over the card with onPointerMove, normalize to [0,1] on both axes into useMotionValue, and smooth with useSpring (stiffness 180, damping 22). Derive rotateX in [10deg, -10deg] and rotateY in [-10deg, 10deg] via useTransform, applied with transformStyle preserve-3d; on pointer leave, spring both axes back to 0.5. Layer a holographic glare: an absolutely positioned motion.div with mix-blend color-dodge whose backgroundImage is a soft spectrum linear-gradient at 115deg (transparent → pink/amber/mint/sky/violet at ~0.35 alpha → transparent), backgroundSize 250% 250%, and backgroundPosition counter-following the pointer via useTransform — never neon, always tasteful. Add a faint diagonal shine band: a rotated (20deg) motion.div with a white 12% linear-gradient streak whose translateX sweeps across the card with the pointer. Fade both glare layers in only while hovering (spring a hover MotionValue 0→1). Content stays minimal: small mono uppercase label, a short title, and a CSS-only orb (radial-gradient sphere with a 1px white/10 ring) floating at translateZ(30px).
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
