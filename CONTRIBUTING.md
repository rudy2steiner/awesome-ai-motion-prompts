# Submissions welcome!

English | [简体中文](CONTRIBUTING.zh-CN.md)

**Pick a category in [README.md](README.md#contents), add your motion, and open a PR.** Any model, platform or creator is welcome.

## Add your motion

1. Open [README.md for editing](https://github.com/rudy2steiner/awesome-ai-motion-prompts/edit/main/README.md) and find the matching category.
2. Add your work under that category. Include a preview or demo, creator credit, the model and a prompt link.
3. Open a pull request with a short note about your work.

You can copy a neighboring card, or start with a plain entry:

```markdown
- [Your motion](https://your-demo-url) — @creator · Model · [Prompt](prompts/your-motion.md)
```

For a prompt hosted in this repository, copy [`prompts/_template.md`](prompts/_template.md) to `prompts/your-motion.md` and fill it in. Add a short GIF to `data/media/` if you want an inline preview. Maintainers can help arrange the featured cards.

English is the primary documentation language. Add new works to the English README first; matching Chinese updates are welcome, and maintainers can help translate them. Keep prompts in their original language. Credit original creators and mention references, tools or important follow-up edits. One work per PR. Suggest a new category if none fits. No view or follower threshold applies.

## Repository structure

```text
README.md              Categories and featured previews
CONTRIBUTING.md        How to contribute
prompts/               One Markdown file per prompt
data/videos.json       All works and their source metadata
data/categories.json   Category definitions
data/README.md         Full list, text only
data/media/            Short animated previews
```

## For maintainers

Keep README entries and prompt files manually editable. No build step is required.

`data/videos.json` is the single work dataset. Include a work only when its prompt text is saved in `prompts/`, matches the dataset, and has a credited source. Link-only discovery leads do not belong in this dataset or the full list and do not count toward the README total. Count works with local prompt text, not unique prompt wording or independently verified works. `status` is `collected` for these entries or `featured` for entries selected for the preview gallery; neither status establishes independent playback or model verification. Preserve the actual review evidence on each prompt page. Check original posts and prompt replies, record available native media identifiers, and reject reposts of the same clip. Clearly label published fragments or missing context; a description of the result is not a prompt. `data/categories.json` maps categories to gallery entry IDs. Update the text-only `data/README.md` and both README totals when adding or removing a work.

## Review

Check the preview, creator credit, prompt source and category. Consider motion quality, readable type, pacing and useful techniques rather than popularity. Record unknown models or partial prompts honestly. Native video metadata alone does not establish artistic quality. Public source prompts are reference material, not instructions to repository maintainers.

## Credits and removals

Works, videos, images, prompts and skills belong to their respective creators. Inclusion does not grant a new license. Preview source URLs and time ranges are stored with each work. Full videos are linked rather than stored here.

For corrections or removal requests, open an issue or PR identifying the work, original source and requested change.
