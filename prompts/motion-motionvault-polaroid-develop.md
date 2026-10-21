# MotionVault: Polaroid Develop

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L324) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/card.ts#L324)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called PolaroidDevelop using React + Tailwind CSS + Framer Motion — a polaroid camera card with a working shutter and shake-to-develop physics. Layout: a 196px white polaroid frame (rounded-md, p-2.5, pb-3, soft 16px/40px shadow, resting rotate -2deg) with a square photo area and a mono caption strip, a '按下快门' pill button below (Camera icon, active:scale-95). Clicking the shutter re-mounts the frame (key = shot count) so a fresh print slides up with spring (from y 34, opacity 0, rotate -5; stiffness 210, damping 20) and development begins: a MotionValue develop goes 0 → 1 over ~9s via useAnimationFrame (base rate 1/9 per second). Map develop to the photo's CSS filter — saturate 0.15→1, contrast 0.72→1, brightness 1.22→1, blur 1.5→0px, eased with smoothstep so color blooms late — while a milky #f5f0e6 veil overlay fades opacity 0.94→0 (steepest between 0 and 0.85). The scene is pure CSS (three cycling scenes 山野晨光/海边落日/城市入夜: layered linear-gradient sky, a glowing sun disc with colored box-shadow, and a clip-path polygon ridge/skyline silhouette). Shake detection: on pointermove over the frame, track horizontal direction reversals within 140ms; each reversal adds 0.35 to a boost ref (capped 2.2) that multiplies the development rate 6× and decays exponentially (~1.6/s); while boost > 0.25 show a '摇晃加速中' mono chip in the caption. Caption shows 显影中 N% (state synced via useMotionValueEvent, only on integer change) then the scene name; a 1px hairline progress bar under the caption scales X with develop. Button becomes 再拍一张 after the first print.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
