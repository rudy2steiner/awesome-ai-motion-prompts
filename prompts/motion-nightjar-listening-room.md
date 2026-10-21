# Nightjar Listening Room

[Source work](https://developers.openai.com/showcase/nightjar-listening-room) · [Upstream prompt transcription](https://github.com/mikenevermiss/motionpromptgallery/blob/19ba3f6/data/items.json)

- **Source account:** Katia Gil Guzman (OpenAI)
- **Model:** GPT-6 Astra (directory reported; not independently confirmed for this work)
- **Category:** music-audiovisual
- **Prompt status:** Upstream transcription
- **Completeness:** Not independently assessed

Selected from the upstream prompt collection for its concrete creative direction. Prompt text was read from the public upstream collection through Chrome MCP; completeness is not independently assessed and any referenced inputs may be required; this import does not independently confirm the original post, model attribution, result fidelity or visual quality. Referenced files, music, images and project context are not bundled. Original upstream source notes are retained below. Upstream notes: Official OpenAI Developers showcase page labelled GPT-6 Astra; initial prompt copied verbatim from the page's build process (2 prompts total, follow-ups in the Code tab). Handle is OpenAI Developers' account, the page credits Katia Gil Guzman. Post date not shown on the page. Media from cdn.openai.com.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
Build a complete, polished, interactive landing page. Use clear, natural copy and a restrained layout with purposeful controls. Keep native scrolling, support phone and desktop layouts, keyboard controls, and reduced motion. The main interaction should work without a runtime AI call or account.

Scenario: Nightjar is an imagined listening room built around records, good speakers and comfortable seats. Visitors can preview the listening experience and explore the room. Demonstrate audiovisual craft and interface timing with a warm, tactile design.

Art direction: tobacco wood, near-black, oxblood and amber light, with excellent photography or original room renders. Use an understated serif for the venue name and a clear compact sans for the listening controls. The page should feel like a specific room at night, not a streaming-service dashboard.

Page and signature interaction:
- Hero: “A listening room for full albums.” A turntable, sleeve and speaker sit in an inviting room scene, with an obvious “Play a sample” button. Audio starts only from user action and always has visible pause/mute and volume controls.
- Offer three distinct original short instrumental samples/loops with accurately described styles and duration. Produce them procedurally with Web Audio or use properly licensed original assets. No copyrighted commercial recordings, fake artist credits, or claims that a short generated loop is an actual released album.
- Selecting a record changes the sleeve, label and sound. The tonearm lowers, platter rotates while playback runs, and subtle meter/room-light movement follows the actual audio amplitude. Pausing must stop the appropriate visual motion. The animation and playback state must stay synchronized.
- Scrolling reveals the room: a bench, a table near the speakers and the bar. Clicking one shows its view and a concise description. Keep the room layout consistent across hero and detail views.
- Include a compact authored listening programme with useful categories, and allow visitors to save a shortlist locally. Use fictional programming without presenting it as a real event booking.
- End with a clear room overview and “Replay the samples” or “View your shortlist.” A functioning preview is the destination; do not add fake ticketing.

Handle browser audio unlocking, sample switching, rapid play/pause, a tab becoming hidden, and reduced-motion preferences. Never require a microphone. Provide a visual alternative for the audio story. Make the mobile player compact and reliable. The result should combine an excellent hospitality landing page with a genuinely working miniature listening experience.
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
