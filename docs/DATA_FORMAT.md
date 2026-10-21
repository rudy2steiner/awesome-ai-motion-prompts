# Open Prompts data contract

`data/motion-prompts.json` is the canonical array. Its objects use the existing `MotionEntry` interface from `open-prompts/src/data/promptMotion.ts` without adding application-facing fields.

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | string | Stable slug used by the detail route |
| `title` | string | Concise English work title |
| `author` | string | Original creator's handle or name |
| `type` | `Prompt` or `Skill` | Published prompt or reusable skill workflow |
| `model` | string | Source-reported model; use “not specified” when unknown |
| `categories` | string[] | Existing Open Prompts category values |
| `prompt` | string | Published prompt in its original language; never an invented reconstruction |
| `sourceUrl` | HTTPS URL | Original work, not an unattributed repost |
| `promptSourceUrl` | HTTPS URL | The actual prompt, reply or skill source |
| `collectionUrl` | HTTPS URL | Discovery / collection source |
| `poster` | string | `/motion-posters/...` public asset or external image URL |
| `width`, `height` | positive integers | Linked preview dimensions |
| `video` | optional HTTPS URL | Direct video preview, when available |
| `skillUrl` | optional HTTPS URL | Reusable skill repository or page |
| `requiresReference` | optional boolean | Whether the published prompt needs supplied assets |

Categories: `Product UI`, `Phone`, `Charts`, `Diagrams`, `Kinetic type`, `Shapes`, `Particles`, `Characters`, `Photos`, `Music`, `Code`.

The model field is not the agent or renderer. For example, GPT can run in ChatGPT, Codex or another agent, while Remotion, HyperFrames and Blender are production tools. Store these distinctions and verification details in `data/provenance.json`, keyed by entry ID.

Incomplete records belong in `data/candidates.json` under `cases`, with a matching `count`. Keep missing prompts as null or absent there; do not invent a prompt to satisfy the import interface. Model claims marked `directory_reported` remain unconfirmed.

`python3 scripts/build.py` generates the TypeScript export and candidate index; README.md is edited directly and is never regenerated. `python3 scripts/validate.py` checks schema compatibility, unique sources, public assets, prompt cards and generated-export consistency. These are local integrity checks, not external link or visual-quality verification.
