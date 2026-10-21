# MotionVault: Rain Glass

[Source work](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L215) · [Author’s prompt / method](https://github.com/xiyu519/MotionVault/blob/master/src/data/effects/background.ts#L215)

- **Source account:** @xiyu519 / MotionVault contributors
- **Model:** Model-agnostic (React / Canvas / Framer Motion)
- **Category:** motion-studies
- **Prompt status:** Creator-published model-agnostic component prompt; preview component listed

Selected from MotionVault’s public effect catalogue through Chrome MCP. This is a creator-published AI component prompt with a named preview component in the same catalogue record, not an original model-run conversation or a claim that a specific model generated the displayed implementation. No generation model is identified. The source line anchor identifies this individual effect within the category file. The prompt is preserved as published and requires its stated React/Canvas/Framer Motion environment. Preview-component mapping and full prompt text were read; live playback, visual quality, physics accuracy and performance were not independently tested. Each distinct effect is counted once; variants or implementation subparts are not separate entries.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Create a React component called RainGlass using React + plain Canvas 2D (no extra libraries). A misty slate gradient base (linear from #1B2430 to #0F141C) fills its container (absolute inset-0, DPR-aware sizing via ResizeObserver, clamp DPR to 2); paint it ONCE on an offscreen fog layer blurred by overlaid soft white haze (alpha 0.05). Droplets condense continuously: every 60-140ms spawn a droplet (radius 0.8-2.6px) at a random position; each droplet grows slowly (+0.006 px/frame) and is drawn as a tiny refracting lens — a radial-gradient circle (light rim at top-left rgba(255,255,255,0.5), dark rim bottom-right, body nearly clear showing the fog) so drops read as beads on glass. When two droplets overlap, merge them (area adds, keep the larger's position). When a droplet exceeds 4.2px radius it starts to slide: it wicks downward at speed proportional to r^2 with a drunken horizontal wander (perlin-ish sine wobble), leaving a cleared trail — stamp the droplet's path onto the fog layer with destination-out (radius r*0.9, alpha 0.5) so the fog behind the trail is wiped clear and slowly re-mists (repaint fog haze at alpha 0.008 per frame). Sliding drops shrink as they lose water (trail sheds 12% of volume per 40px) and die at r < 1.6px or the bottom edge. Cap 220 droplets. Pure rAF loop; clean up the loop and ResizeObserver on unmount.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
