# Chaos to Calm Transition

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/before-after-chaos-to-calm](https://www.aicssanimations.com/directory/Motion-Prompts/before-after-chaos-to-calm)
- **Collected:** 2026-11-08

## Prompt

```
Make a 10-second before-and-after promo: a dark, crowded desktop of conflicting spreadsheets, sticky notes, pinging chats and email chains jostles for attention, freezes for a beat, then every piece flies to its place and turns into part of one calm, light project screen, which breathes for the rest of the film.

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Evenkeel (fictional), one workspace for a team's projects. Project: "Spring launch", launch date Mar 21, team Dana Ruiz, Kofi Mensah, Ines Varga, Mo Haddad (all fictional).
- The mess, all fictional:
  Spreadsheets: "Launch budget v3 FINAL", "launch budget (Dana's copy)", "Timeline old DO NOT USE".
  Sticky notes: "who owns onboarding??", "call Dana re: launch date", "budget v2 or v3?", "ship Mar 14?? or 21", "fix pricing page copy", "where's the latest deck".
  Chat pings: "Mo: is launch the 14th or the 21st?", "Ines: which budget is the real one", "Dana: I thought Kofi owned onboarding", "Kofi: I thought Dana did", "Mo: can someone send the latest deck".
  Emails: "Re: Re: Fwd: launch timeline (14)", "Budget — final final".
  Calendar: "Launch sync", "Launch sync (moved)", "Budget review", overlapping on Thursday.
  Unread counter: climbs from 12 to 47.
- The calm screen:
  Tasks (6): "Assign onboarding owner" · Kofi; "Confirm launch date: Mar 21" · Dana; "Lock budget v3" · Ines; "Fix pricing page copy" · Mo; "Share final deck" · Mo; "QA the signup flow" · Kofi.
  Timeline: Mar 3 "Beta" · Mar 14 "Press preview" · Mar 21 "Launch".
  Budget: Ads $18,000 · Events $9,500 · Content $6,200 · Tools $2,300 · Total $36,000.
  Thread: Dana "Launch is Mar 21. Locked." · Kofi "I'll own onboarding." · Ines "Budget v3 is final: $36,000."
- Headline: "Your whole launch, in one calm place." Sign-off: Evenkeel · "Free for teams up to 10".
- Length: 10 seconds.
</inputs>

<direction>
- Look: two halves with opposite physics. Before is dim, cramped and restless: overlapping windows at odd angles, saturated sticky notes, red badges, everything slightly moving. After is warm, light and still: one app with generous spacing, and the only motion is a checkbox being ticked. The switch is a single gesture in which each messy object is seen becoming its tidy counterpart.
- Before palette: background #24262A with a vignette to #17181B at the corners; window bodies #E9EAEC with title bars #C9CCD1 and text #1C1D1F; sticky notes #F5D547, #F2A2B6, #A6D49B, #F4B266, #9DC7E6, #F5D547, each with a slightly darker fold shadow at the bottom; chat bubbles #FFFFFF with names in 600 weight; unread badges #E5484D with white numbers. After palette: background #F3EFE7; app window #FFFFFF with a 1px #E6E0D6 border and shadow 0 30px 80px rgba(60,48,30,0.14); cards #FAF8F4; hairlines #E6E0D6; ink #24221F; secondary #77716A; accent slate blue #3F6B8E (timeline, links, the active avatar ring); done green #5B8C6A (checks and "On track"). The sticky colors survive in the after only as 6px dots beside each task, so the viewer can trace them.
- Type: Outfit 400 / 500 / 600 for the app and the chats; Patrick Hand 400 for sticky notes, 26px; DM Mono 400 for spreadsheet cells, 15px; Archivo 700 for the headline, 54px, tracked −0.01em.
- The mess (before), placed by hand with seeded jitter, overlapping on purpose but every label readable on at least one of its copies: spreadsheet A 520×340 at (110, 80), −4°; spreadsheet B 480×300 at (1250, 610), 5°; spreadsheet C 440×280 at (690, 700), −2°; the calendar 420×300 at (1370, 120), 3°; six sticky notes 200×200 spread over the middle band (y 280–760) at angles between −9° and 8°; chat bubbles 380×84 and email notifications 420×92 sliding in from the edges and stacking near the right and bottom; the unread counter as a red pill "Unread 12" at (60, 1000) that climbs. Spreadsheet cells hold real-looking numbers that disagree (Ads 18,000 in one, 16,500 in another).
- Before motion: every object drifts on its own slow seeded noise (6–12px, ±1° rotation, periods 2–4 s); a new chat or email slides in every 0.4 s from the nearest edge on easeOutBack, nudging its neighbors 8px aside; badges count up; the whole frame carries a 2px handheld drift. Busy and slightly stressful, never strobing: nothing flashes, and new items slide rather than appear.
- The freeze: at 3.5 s every object stops dead for 0.2 s, the counter at 47, a held breath.
- The collapse, 3.7–5.0 s: each object flies to its target slot in the calm app on a curved path (a quadratic curve bowing away from the frame's center), its rotation easing to 0 and its rectangle easing to the slot's rectangle over 0.95 s on easeInOutCubic, staggered 25 ms by distance from the center. During the flight its face crossfades from the messy look to its calm component, drawn into the same moving rectangle. Mapping: each sticky note becomes one task row (its color becomes the row's dot); spreadsheets A and B fly into the budget card and merge into one table, spreadsheet C and the calendar become the timeline card; all chats and emails fly into the thread card, merging into its three messages. Nothing fades out unaccounted for.
- The light arrives with it: a circular reveal of #F3EFE7 grows from the app's center (960, 590) to cover the frame (3.8–4.6 s, easeInOutSine), and the app window's frame fades in around the arriving parts (4.4–4.8 s).
- The calm app (after): window 1360×760 at x 280–1640, y 210–970, radius 20. Header y 210–290: "Spring launch" in Outfit 600 30px at (320, 262), a chip "Launch Mar 21" (#3F6B8E text on #E7EEF4), four 30px avatars (DR, KM, IV, MH) and "On track" with a green dot at the right. Tasks card x 312–812, y 310–940: "Tasks · 6" in 18px 600, six 72px rows with a 22px checkbox, the task in 18px, its color dot and the owner's avatar at the right. Timeline card x 836–1608, y 310–450: a 2px #3F6B8E line with three milestones (dot, date in 600, label in secondary), Launch emphasized with a filled 14px dot. Budget card x 836–1212, y 470–940: four rows and a total row with a hairline above, amounts right-aligned in tabular figures. Thread card x 1232–1608, y 470–940: three messages with 28px avatars, names in 600, text in 17px, and a reply field at the bottom.
- After motion: almost none. Cards settle the last 2% over 0.4 s. The headline rises 10px and fades in at y 140, centered. Then one task gets done, one reply arrives, and the sign-off appears. Everything moves on easeOutCubic, slowly.
- Premium: specific, recognizable mess with real conflicting details; one clean gesture where every piece is seen becoming something; a long, quiet after with real spacing; the sticky colors carried through as dots. Cheap: things that vanish in a poof, explosions, glitch transitions, a whoosh blur, a cheesy "Before / After" label, a calm screen that's just as crowded, sparkles when it resolves.
- Banned: real company names, logos and UI copied from existing products; real file-format icons or office app chrome; emoji; glitch or datamosh transitions; particles or confetti; whip blur; flashing badges; anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.4s: the mess is already there, dim, drifting; the counter reads 12.
- 0.4–3.5s: escalation: chats and emails slide in every 0.4 s (the five chats, then the two emails, then repeats of the first questions with "(2)" and "(3)" added), badges climb, the counter reaches 47 by 3.4 s, sticky notes are bumped and swing a few degrees.
- 3.5–3.7s: the freeze: all motion stops.
- 3.7–5.0s: the collapse: every object flies to its slot and becomes its component; the light reveal spreads (3.8–4.6 s); the window frame fades in (4.4–4.8 s).
- 5.0–5.4s: the settle: the last 2% of every card eases in; the unread counter flies with the chats into the thread card's header, counts down to 0 and fades.
- 5.4–5.85s: the headline "Your whole launch, in one calm place." fades in and rises at y 140.
- 5.85–6.3s: the 6.0 s frame is the hero: the headline above the complete calm app, all six tasks, the timeline, the budget totaling $36,000 and the three-message thread, everything still and readable on the warm light background.
- 6.6–7.1s: "Confirm launch date: Mar 21" gets ticked: its checkbox fills green with a drawn check (0.25 s) and the text takes a hairline strike and fades to secondary.
- 7.2–7.7s: a fourth message slides up into the thread: Mo "Deck is in the project files." and the reply field stays empty.
- 8.0–8.5s: below the window, the Evenkeel mark (an original glyph: a short horizontal line with a shallow arc above it, both 3px #3F6B8E strokes) and "Evenkeel" in Outfit 600 26px fade in centered at y 1020, with "Free for teams up to 10" in 18px secondary beside it.
- 8.5–10.0s: hold, perfectly still.
For other lengths, keep the freeze and the 1.3 s collapse, stretch the escalation or the calm, and keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: every object is drawn in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Drift is seeded noise sampled at t; the neighbor nudges are scripted offsets that ease in and out, not a physics simulation. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face and weight before defining window.seek. Canvas won't fetch fonts itself, so the awaited loads matter.
- Engine: Canvas 2D, repainting every frame from scratch, the backing store sized from CSS size × devicePixelRatio. Each object is a record with its before rectangle and angle, its after slot, its two face-drawing functions and its timing; seek computes its current rectangle, angle and crossfade and draws both faces into it with the context transformed. The reveal is a clipped circle of the light background drawn under the arriving objects.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that the mess is dense but each item is readable somewhere, nothing strobes, the freeze is a true stop, every object is visibly tracked into a component (none vanishes), the budget adds to $36,000, the task dots match the sticky colors, and the after half is spacious and still. At 2.0 s the mess is busy with the counter in the 30s; at 4.3 s objects are mid-flight and half transformed; the 6.0 s frame shows the headline and the complete calm app; at 7.0 s the launch-date task is ticked; the final frame adds Mo's message and the sign-off. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
