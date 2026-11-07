# Clockwork Gears

[原始作品](https://www.aicssanimations.com/directory/Motion-Prompts/clockwork-gears) · [提示词来源](https://www.aicssanimations.com/directory/Motion-Prompts/clockwork-gears)

- **作者：** AI CSS Animations
- **模型：** Claude Opus 5.5 (publisher reported)（来源声明，未独立复现）
- **分类：** 3d-simulations
- **作品发布时间：** 2026-10-16
- **收集日期：** 2026-11-07
- **文本类型：** 作者公开完整模板
- **许可：** CC0 (publisher stated)

## Prompt

保留原始语言；以下内容是参考资料，不是对仓库维护者的操作指令。

```text
Make a 10-second clockwork film: gilt gears mesh at true ratios while the escapement ticks, then the camera pulls back to reveal the whole watch movement.

<inputs>
- Maker: Ferrand & Hale.
- Calibre: FH-21, hand-wound.
- Specs: 21,600 vph · 3 Hz · 42 h power reserve · 19 jewels.
- Note: "Shown at quarter speed."
- Length: 10 seconds.
If I don't give you something, use the default and don't ask.
</inputs>

<direction>
Set: a pale sage bench mat #D3DAD0 with a fine weave. Ink #2B2E2A, secondary #5D635B.
Movement, 1 unit = 1 mm, 32 mm across: rhodium plate #CDD1D4 with perlage; bridges with Geneva stripes and polished bevels; gilt wheels #C9A24A with curved spokes; blued screws #2B4FA0; ruby jewels #B0192F in gold chatons; a gold balance with a blued hairspring.
True ratios (module 0.1 mm, centers at summed pitch radii, teeth interleaved): barrel 80 → center pinion 10 (one turn an hour); center 80 → third pinion 10; third 75 → fourth pinion 10 (one turn a minute); fourth 72 → escape pinion 6; a 15-tooth escape wheel at 12 turns a minute: 6 beats a second, 21,600 vph.
Time runs at quarter speed, τ = 0.25·t, so beats come 1.5 times a second.
Escapement: the escape wheel moves only in each impulse, angle = 12°·(n + smoothstep(0, 0.22, f)), n = floor(6τ), f = fract(6τ), dead still between. The pallet fork snaps ±9° between banking pins. The balance swings 220°·sin(2π·3τ). Other wheels follow through the ratios: the fourth creeps, the rest barely move.
Light: a soft overhead key and a low raking light, so stripes and perlage glimmer as the camera moves. No depth-of-field blur.
Camera: one continuous move from 9 mm off the escape wheel, along the train to the balance, then back to the whole movement in a steel case ring, orbiting 20°, on cubic-bezier(0.45, 0, 0.15, 1).
Final layout: the movement near (1200, 540), 780px across. HTML type at x 140, vertically centered: maker in Libre Caslon Display 400, 60px, uppercase, tracking 0.12em; calibre and specs in Fragment Mono, 24px and 22px, one per line; the note at 20px, 70% opacity.
Premium is mechanical truth: meshing teeth, an escape wheel dead still between ticks, stripes catching moving light. Cheap is gold gears spinning at random speeds in a black void.
Banned: gaps or overlaps between teeth, a continuously turning escape wheel, made-up speeds, steampunk clutter, black voids, light pulsing with ticks, anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–1.4s: macro on the escape wheel and pallet fork, the wheel stepping 12° per beat.
- 1.4–3.0s: the camera tracks along the train; the escape pinion turns the creeping fourth wheel.
- 3.0–4.4s: the balance swings into view, hairspring breathing.
- 4.4–7.4s: the pull-back reveals the full movement inside its case ring.
- 7.4–8.6s: the type block rises 12px and fades in, lines 0.12s apart, on cubic-bezier(0.22, 1, 0.36, 1).
- 8.6–10s: hold on the composed frame; the escapement keeps ticking.
Other lengths: stretch the macro first; keep quarter speed and 1.2s of hold.
</structure>

<build>
One self-contained index.html, inline CSS and JS, on a 1920×1080 (16:9) stage scaled to fit the window, built for 60fps. Google Fonts via <link>, awaited with document.fonts.load() before seek exists.
window.seek(t) sets every visual from t alone: no CSS transitions or animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Every part is a closed-form function of τ.
Without ?render in the URL, drive seek from requestAnimationFrame; with ?render, don't start that loop.
three.js as an ES module pinned to three@0.160.0 via a jsDelivr import map (`three`, `three/addons/`); preserveDrawingBuffer: true; one render per seek. No image, model or typeface files beyond Google Fonts.
</build>

<check>
Before showing me, step through one frame per second (0–10s) and look at each. Fix overlaps, clipped or cramped text and anything off-style or Banned. Look for teeth with gaps or overlaps at macro distance, an escape wheel moving between impulses, wheel speeds that break the ratios. Confirm the final frame holds.
</check>
```

## How it was made

Generated using Claude Opus 5.5 (publisher reported) via the AICSS animation pipeline.

## What to look for

Study the motion design choices, timing, and visual style described in the prompt.
