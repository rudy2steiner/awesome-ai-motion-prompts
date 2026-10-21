# MotionVault: Orbit Text

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L247) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/text.ts#L247)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called OrbitText using React + Tailwind CSS. It typesets the phrase 'MOTION VAULT · INSPIRATION · ' around a circle WITHOUT SVG textPath: split into characters and absolutely position each at left-1/2 top-1/2 of a 216x216px relative wrapper with transform 'translate(-50%, -50%) rotate(i * (360 / len) deg) translateY(-88px)' (monospace 13px, font-medium, uppercase, zinc-950, space chars rendered as-is since the fixed angular step keeps spacing). Rotate the whole ring continuously at 360deg per 12s with a requestAnimationFrame loop (gated by IntersectionObserver, cancelAnimationFrame on cleanup) writing style.transform = rotate(angle) directly to a ref'd wrapper — no state. Track a target direction in a ref (+1 normally, -1 while hovered via onMouseEnter/onMouseLeave) and exponentially lerp the current direction each frame (factor ~dt * 4, dt clamped to 50ms) so the spin reverses like a turntable changing direction, never a hard cut. Place a small 8px rounded-full zinc-950 dot (logo mark, pointer-events-none) in the exact center. will-change-transform on the ring, cursor-pointer, light background, aria-label on the container.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
