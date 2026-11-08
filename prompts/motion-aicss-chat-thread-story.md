# Chat Thread Story Ad

- **Author:** AI CSS Animations
- **Model:** Claude Opus 5.5 in Claude Code
- **Source:** [https://www.aicssanimations.com/directory/Motion-Prompts/chat-thread-story](https://www.aicssanimations.com/directory/Motion-Prompts/chat-thread-story)
- **Collected:** 2026-11-08

## Prompt

```
Make a 10-second ad told as a team chat thread: three coworkers at a small furniture shop trade quick messages about a customer emailing for the third time, typing dots appear between messages, a "Two weeks later" divider jumps to the fix, a shared-inbox card shows it working, and the chat slides aside for the product's end card.

<inputs>
If I don't give you something, use the default and don't ask.
- Product: Fernpost (fictional), one shared inbox for support teams. Company: Birchwood Home (fictional), an online furniture shop. Channel: "# support", 3 members.
- People (initials · avatar color): Priya Shah, support lead (PS · #E0703A); Marcus Bell, operations (MB · #3C7A9E); Jen Ortiz, founder (JO · #4F8A5B). Customer: Hannah Cole.
- Messages, exactly (time · person · text):
  9:02 · Priya · "hannah cole just emailed a 3rd time about her missing table leg"
  9:02 · Marcus · "which inbox? support@ or hello@?"
  9:03 · Priya · "both. and someone answered her from orders@"
  9:04 · Jen · "we can't see each other's replies. trying Fernpost today"
  divider: "Two weeks later"
  4:41 PM · Priya · "hannah's leg shipped. reply went out in 12 min" with a Fernpost card: "Missing table leg" · "Hannah Cole · Order BW-48213" · chips "Assigned: Priya", "Replied in 12 min", "Shipped".
  4:43 PM · Jen · "first reply time this week: 3 h → 18 min" with a reaction "♥ 3".
- End card: "Fernpost" · "One inbox for the whole team." · button "Try it free for 14 days".
- Length: 10 seconds.
</inputs>

<direction>
- Look: a bright, bold social ad. One clean chat window on a flat sunflower field, messages arriving at a believable typing rhythm, the tension in the words, the relief in the numbers. The chat UI is original and minimal: avatar, name, time, a soft bubble. The end card speaks in a confident serif.
- Palette: background sunflower #F5CF4E with fixed seeded grain at 2%; chat window #FFFFFF with shadow 0 40px 90px rgba(90,64,0,0.22) and 0 6px 18px rgba(90,64,0,0.12); window hairlines #ECE8DD; message bubbles #F3F1EB; text #1E2A22; secondary #6F756C; divider text #8A8F86; avatar fills as given with white initials; the embedded card #FBFAF6 with a 1px #E4E0D4 border and a 4px #1E3A2F left bar; chips #E3F0E5 with #2F6B3E text; brand ink #1E3A2F (logo, CTA); the reaction chip #FBE3D6 with #C2512A heart and count. No blue gradients, no purple.
- Type: Lexend 400 / 500 / 600 / 700 for all chat UI (names 600 18px, times 400 14px secondary, messages 400 21px with 30px line height); DM Serif Display 400 for the end headline at 76px; Lexend 700 48px for the wordmark.
- The window: 900×1000 at x 510–1410, y 40–1040, radius 24. Header y 40–112: "# support" in Lexend 600 22px at x 548, "Birchwood Home" in 14px secondary under it, and at the right three overlapping 30px avatars and "3 members". Composer y 968–1040: a rounded field 836×48 at x 542 with "Message # support" in 17px #A3A79F and a send glyph. Message area y 112–968 with 32px side padding.
- Messages: each row has a 40px avatar circle at x 542, the name and time on one line at x 598, and below it the text in a bubble (padding 12px 18px, radius 16 with a 4px top-left corner) starting at x 598, max width 740px. A run of messages from the same person drops the repeated avatar and name. Rows stack from y 136 with 18px gaps; lay them out so the whole thread, card and reaction fit inside the message area without scrolling.
- Typing indicator: before each message, a small bubble at the sender's position with three 8px #9CA19A dots that rise 4px one after another on a 0.9 s cycle (easeInOutSine), shown for 0.3–0.4 s and replaced by the message. The indicator's avatar and name appear with it.
- Message entrance: the bubble grows from scale 0.94 and 10px lower to full on easeOutBack (overshoot 1.15) in 0.3 s; the text is fully set when it lands (no letter-by-letter typing inside bubbles). The time stamps are real minutes, in order.
- Divider: a 1px #E4E0D4 line across the message area with "Two weeks later" in Lexend 500 14px #8A8F86 on a white pill in the middle; it draws out from the center in 0.35 s.
- The Fernpost card, inside Priya's second message, below its bubble: 560×156, radius 12. Top row: an original Fernpost mark at 18px (two rounded rectangles stacked and offset like letters in a tray, in #1E3A2F) and "Fernpost · Shared inbox" in 13px secondary; "Missing table leg" in Lexend 600 19px; "Hannah Cole · Order BW-48213" in 15px secondary; then the three chips (13px 500, radius 8) in a row. It unfolds: its height grows from 0 on easeOutCubic in 0.35 s while its contents fade in 0.1 s later, chips 60 ms apart.
- The numbers: in Jen's last message, "3 h" lands with a hairline strike that draws through it in 0.2 s after the message lands, and "18 min" is set in Lexend 600. The reaction chip under it appears as "♥ 2" and ticks to "♥ 3" 0.3 s later; the heart is a drawn SVG shape, not an emoji.
- The end move: the chat window slides left on easeInOutCubic to x 160–1060 while staying full size; on the right, the end card fades in and rises: the Fernpost mark at 88px and "Fernpost" at (1160, 300); the headline "One inbox for the whole team." on three lines in DM Serif Display at (1160, 400), max width 640px, color #1E2A22; the button at (1160, 760), 340×64, radius 32, #1E3A2F with "Try it free for 14 days" in Lexend 600 20px #F5CF4E.
- Premium: messages that sound like real coworkers, typing pauses that set the rhythm, a clear before and after split by the divider, a product card that shows the fix in real data, a bold flat color field with one clean window. Cheap: phone-messenger blue and green bubbles, emoji spam, a fake "seen" checkmark race, notification sounds drawn as icons, words typing letter by letter inside bubbles, bouncing reaction emoji, text that cuts in without rhythm.
- Banned: real company names, logos and UI copied from existing products (no real chat app's layout, colors or icons); emoji glyphs; a real email domain; bubble tails copied from phone messengers; confetti; shaking windows; anything flashing more than 3 times per second.
</direction>

<structure>
- 0.0–0.45s: the sunflower field; the window rises 30px and fades in (easeOutCubic) with its header and empty composer.
- 0.45–0.85s: Priya's typing dots; her first message lands at 0.85 s.
- 1.15–1.5s: Marcus's typing dots; his message lands at 1.5 s.
- 1.75–2.1s: Priya types; her second message lands at 2.1 s.
- 2.4–2.85s: Jen types; her message lands at 2.85 s (a beat longer: it's the decision).
- 3.2–3.55s: the "Two weeks later" divider draws out.
- 3.65–4.05s: Priya types; her message lands at 4.05 s and the Fernpost card unfolds beneath it (4.2–4.65 s), chips last.
- 4.85–5.2s: Jen types; her message lands at 5.2 s; the strike through "3 h" draws (5.35–5.55 s); the reaction "♥ 2" appears at 5.6 s and ticks to "♥ 3" at 5.9 s.
- 5.9–6.4s: the 6.0 s frame is the hero: the full thread in the centered window, every message, the divider, the Fernpost card with its chips and Jen's number with the strike and reaction, all readable.
- 6.6–7.3s: the window slides left.
- 7.1–7.9s: the end card builds on the right: the mark and wordmark (7.1 s), the headline line by line, 0.12 s apart (7.3 s), the button (7.7 s), each rising 12px and fading in on easeOutCubic.
- 7.9–10.0s: hold on the thread and the end card side by side.
For other lengths, keep reading-speed pauses (about 0.3 s per 5 words plus the typing dots), keep the divider beat, and keep at least 1 s of hold.
</structure>

<build>
- One self-contained index.html (inline CSS and JS), a 1920×1080 (16:9) stage scaled to fit the window, designed for 60fps. No image, video, texture or model files: avatars, icons, the heart and the logo are drawn in code.
- window.seek(t), t in seconds, computes every visual from t alone: no CSS transitions or CSS animations, no setTimeout/setInterval, no state carried between frames, randomness only from a seeded PRNG. Past the end, seek clamps to the last frame.
- Without ?render in the URL, drive seek from requestAnimationFrame so it plays in a browser (loop after a 1s end hold); with ?render, don't start that loop.
- Google Fonts via <link> are fine; await document.fonts.load() for each face and weight before defining window.seek.
- Engine: plain DOM and CSS. Build every row once at load in its final position (so the layout never shifts), measure it, and let seek set each row's opacity, transform and the typing indicator's state from one message timeline. The typing dots' offsets are a pure function of t. The card's unfold sets its height and clip from t.
</build>

<check>
Before showing me, step through one frame per second (t = 0…10): screenshot each and look at it. Fix overlaps, clipped or cramped text, and anything off-style or Banned. Check that every message is word for word as given and fits on its line or wraps cleanly inside its bubble, the thread fits the window without scrolling, the time stamps are in order, typing dots never flash, the heart is drawn (not an emoji), and no real chat app's look is copied. At 1.0 s Priya's first message is in; at 3.0 s the four "before" messages are in; at 4.5 s the Fernpost card is unfolding; the 6.0 s frame shows the complete thread centered; the final frame shows the thread on the left and the end card on the right. Confirm seek(10) and seek(11) match, so the final frame holds.
</check>
```
