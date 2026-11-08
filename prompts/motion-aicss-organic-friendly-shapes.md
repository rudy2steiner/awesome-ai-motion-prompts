# Organic Friendly Shapes

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/organic-friendly-shapes](https://www.aicssanimations.com/directory/Motion-Prompts/organic-friendly-shapes)
- **Collected:** 2026-11-08

## Prompt

```
<inputs>
- BRAND (lowercase wordmark). Default: "sunnook".
- TAGLINE. Default: "Little rituals for calmer days."
- ICON: optional SVG; default is the drawn mark below.
- COLORS. Default: the palette below.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Pebble-soft blobs breathe, gather and become an app icon; the wordmark lands on a gentle spring. It should feel like an exhale.
- Palette: background cream #FBF4EA; blobs peach #FFB8A1, butter #FFD98E, sage #B7D6B0, lilac #CDBDF2, sky #ABD3EC; ink #2E2A35, never pure black. Blobs use mix-blend-mode multiply so overlaps make a soft third tint.
- Type: wordmark in Fredoka 600, 132px, letter-spacing −0.01em, ink; tagline in Nunito 600, 30px, #6B6474.
- Blobs: SVG paths rebuilt every seek. 9 radial control points each; radius = base × (1 + 0.07·sin(1.3t + φ1) + 0.04·sin(2.1t + φ2)), phases seeded per point, joined with a closed Catmull-Rom spline as cubic Béziers. Sizes 260–520px.
- Depth: one static soft shadow filter (dy 18px, blur 36px, rgba(120,72,50,0.13)). Grain: a static feTurbulence layer (baseFrequency 0.85, 2 octaves, fixed seed) at 6% opacity, soft-light, over everything.
- Motion: entrances use an analytic damped spring, x(τ) = 1 − e^(−ζωτ)·cos(ω_d·τ), ζ 0.62, ω 2π·1.5 (overshoot under 10%). Drifts use easeInOutSine over 4–6s. Peak speed under 300px/s.
- Icon: a 300px squircle (superellipse, n = 5) in peach holding a butter circle with a smile drawn as one 10px round-capped ink stroke.
- Premium: wide margins (type at least 160px from edges), blobs that feel weighted, one thing in focus at a time. Cheap: confetti, hard shadows, everything bouncing at once.
Banned: neon, pure #000 or #FFF, hard-edged shadows, overshoot above 12%, fast spins, emoji, full-frame gradient mesh, more than five fills, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.4s: peach, sage and lilac blobs rise from below frame on springs staggered 0, 0.2, 0.4s.
- 1.4–3.6s: they drift and breathe; two overlap into a tinted lens; a small butter blob floats up through the gap.
- 3.6–5.2s: peach moves to center and morphs into the squircle (radii eased toward its outline, 1.2s easeInOutCubic) while the others shrink into it; the smile draws on at 4.8s.
- 5.2–7.0s: icon springs 280px left as wordmark letters rise 24px, 55ms stagger, each on the spring.
- 7.0–8.4s: tagline rises 14px and fades in (700ms, easeOutCubic); two small blobs settle into the far corners.
- 8.4–10.0s: hold with slow breathing only (scale ±1.5%).
Stretch the drift beat for longer cuts; keep spring timings fixed.
</structure>

<build>
- One self-contained index.html, 1920×1080 (16:9) stage, designed for 60fps.
- window.seek(t), t in seconds, computes every visual from t: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames (anything cumulative is solved analytically from t or re-simulated from 0 at a fixed step), randomness only from a seeded PRNG.
- No ?render in the URL: drive seek from requestAnimationFrame. With ?render: don't start that loop. Define seek once fonts and assets load.
- Google Fonts via <link> are fine.
- Engine: inline SVG; path data, transforms and opacity are set from seek.
</build>

<check>
Before showing me, screenshot one frame per second (t = 0…10) and look at each. Fix overlaps, clipped or cramped text, and anything that reads as a cheap demo. The icon and wordmark should balance optically as a pair, the tagline needs room, blobs must never kink, and the grain should be felt, not seen. Confirm the final frame holds as a composed end card.
</check>
```
