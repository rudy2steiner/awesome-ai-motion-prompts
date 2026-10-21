# MotionVault: Like Burst

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/button.ts#L132) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/button.ts#L132)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** interactive
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React LikeButton component (Twitter-style) using React + Tailwind CSS + Framer Motion + the Heart icon from lucide-react. A ghost circular button (h-12 w-12, rounded-full, hover bg-rose-50) with a heart icon and a like count sitting next to it. On like: the heart fills rose #F43F5E and pops in with an elastic spring (remount with scale 0, spring stiffness ~420 / damping ~11 so it overshoots to ~1.3 before settling), a 2px rose ring expands outward from the button's edge (scale 1 → 1.9 while fading, 550ms ease-out), and 7 tiny particles — a mix of 4px dots and mini filled hearts in rose shades (#F43F5E, #FB7185, #FDA4AF) — spew radially (even 360°/7 spread with slight angle jitter, 26–44px travel, shrinking and fading over 650ms ease-out). On unlike: the heart unfills with a calm 150ms shrink, no ring or particles. The count increments/decrements with a tiny y-slide: wrap it in AnimatePresence (popLayout) so the new number slides in from below on +1 and from above on -1 (180ms). Center on a light preview.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
