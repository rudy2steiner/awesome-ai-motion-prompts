---
title: "Inbox Triage"
author: "AI CSS Animations (@SaaSgod)"
model: "Claude Opus 5.5 in Claude Code"
source: "https://www.aicssanimations.com/directory/Motion-Prompts/inbox-triage"
license: "CC0"
collected: "2026-11-03"
---

# Inbox Triage

**Author:** AI CSS Animations (@SaaSgod)  
**Model:** Claude Opus 5.5 in Claude Code  
**Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/inbox-triage](https://www.aicssanimations.com/directory/Motion-Prompts/inbox-triage)  
**License:** CC0

## Prompt

```
Make a 10-second mobile interface animation: a thumb swipes through an inbox, archiving, snoozing and labelling until unread reaches zero and a calm empty state appears.

<inputs>
- App: default "Stillpost" (mail)
- Messages (sender . subject . action): default Rowan Feld . Invoice #2041 paid . archive; Ottilie Park . Lunch Thursday? . snooze; Build server . Build 1184 passed . archive; Hessa Karim . Contract draft v3 . label Work; Marlow Ito . Photos from the lake . archive.
- Empty state: default "All caught up." / "Nothing new. Enjoy the quiet."
- Length: default 10 seconds
</inputs>

<direction>
- Palette: stage pale sky #D5E2EC; phone #16191E; screen #FBFBF9; text #1E2A36; muted #6C7783; unread dot #3E6FD8; actions archive #2F9E6B, snooze #E39A2D, label #3E6FD8.
- Type: Albert Sans 400-700 in the phone; the giant counter in Fraunces 300 (SOFT 100) at 420px.
- Layout: a 448x936 phone at x 1060, y 72; left of it the unread numeral centered on x 600.
- Touch: a 56px white circle at 60% with a thin ring, pressing to 88%, moving on thumb arcs.
- Swipes: rows track the touch 1:1. At 35% the swipe commits: the action color blooms from the icon (180ms) and the icon pops 1->1.18->1.
- Premium feels like a real phone: rows glued to the thumb, a visible threshold, gaps closing in one motion.
Banned: confetti, rows fading or shrinking away, staggered reflow, rows faster than 3,000 px/s.
</direction>

<structure>
- 0.0-0.8: The phone rises 40px; rows populate 50ms apart; the giant 5 fades up.
- 0.8-1.5: Archive Rowan Feld. 5->4.
- 1.5-3.0: Snooze Ottilie Park. 4->3.
- 3.0-3.6: Archive the build. 3->2.
- 3.6-5.1: Label Hessa Karim. 2->1.
- 5.1-5.7: Archive Marlow Ito. 1->0.
- 5.7-7.6: Empty state draws in.
- 7.6-10.0: Chips and hold.
</structure>

<build>
One self-contained index.html, 1920x1080 stage, 60fps. HTML/CSS with inline SVG; no canvas or three.js. window.seek(t) sets every visual from t alone.
</build>
```
