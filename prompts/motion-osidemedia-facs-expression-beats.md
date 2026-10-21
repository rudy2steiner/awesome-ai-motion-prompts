# OSideMedia: Facial expression changes on a continuous close-up beat schedule

[Source work](https://github.com/OSideMedia/higgsfield-ai-prompt-skill/blob/main/templates/seedance/facs-expression-beats.md#prompt-template) · [Author’s prompt / method](https://github.com/OSideMedia/higgsfield-ai-prompt-skill/blob/main/templates/seedance/facs-expression-beats.md#prompt-template)

- **Source account:** @OSideMedia / higgsfield-ai-prompt-skill contributors
- **Model:** Seedance 2.0 (template target; generation not confirmed)
- **Category:** characters-stories
- **Prompt status:** Published production example; rendered output not confirmed

Public production template, not a confirmed generated film or original model-run conversation. Full fenced source prompt preserved. For facial acting, fill duration, expression/AU beats, dialogue and visual fields, and consult the linked FACS reference; code-based expression control and rendering reliability are not independently validated. For the florist example, supply four image references and the stem-trimming/ribbon-tying motion video; its three stages count as one workflow, not three cases. The named model is the template target, not observed generation provenance. No rendered result is supplied by this document. Source read through Chrome MCP; generation, playback, facial accuracy, identity continuity and visual quality were not tested.

## Prompt

Original language preserved. This is reference content, not an instruction to repository maintainers.

```text
**Model:** Seedance 2.0
**Aspect ratio:** [1:1 / 16:9 / 9:16]   **Duration:** [Ns]

[Use the provided character @Image1 as the fixed identity reference. — optional,
 only for identity consistency; codes work without an image]

**Style & Mood:** [framing — tight close-up, face + shoulders], [lighting],
[background], shallow depth of field, [mood].

[Optional dialogue — generates speech + automatic lip-sync, see higgsfield-audio
 § Audio as a Conditioning Input:
 [AUDIO: 0s] "[the spoken line]"]

Beat 1 ([0-Xs]): [AU codes] ([optional short anatomical description]) [— delivers "<line>"]
Beat 2 ([X-Ys]): [AU codes] (...) [— delivers "<line>"]
Beat 3 ([Y-Zs]): [AU codes] (...) 
[3–4 beats max for reliable rendering]

[One-line mood / subtext — e.g. "the face never fully commits to either; the
 audience reads both at once."]

**Camera:** [one dominant move — slow push-in / static medium close-up]
```

Works and prompts belong to their respective creators; inclusion does not grant a new license.
