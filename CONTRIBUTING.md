# Submissions welcome!

**Pick a category in [README.md](README.md#contents), click “＋ Submit to this category”, add your motion, and open a PR.** Any model, platform or creator is welcome.

## Add a work

The category link opens the README editor. Find that category and add your work above its `Add new ... motions above this line` comment. GitHub will guide you through forking the repository and opening a PR.

For a featured preview, copy a card from that category's table. Each `<tr>` holds up to three `<td>` cards; start a new row when needed:

```html
<tr>
<td width="33%" valign="top">
<a href="examples/your-motion.md"><img src="public/motion-previews/your-motion.gif" width="260" alt="Your motion title" /></a><br>
<a href="examples/your-motion.md"><b>Your motion title</b></a><br>
<a href="https://your-original-post-url">@creator</a> · <a href="examples/your-motion.md#prompt">Prompt</a><br>
<sub>Model name</sub>
</td>
</tr>
```

No preview yet? Add a simple text entry under the category instead:

```markdown
- [Your motion title](https://your-video-or-demo-url) — @creator · Model name · [Prompt](https://your-prompt-or-skill-url)
```

Maintainers can help turn it into a featured card. The **Full list is text-only**; it does not need a cover or image.

If you need somewhere to put your prompt, copy [`examples/_template.md`](examples/_template.md) to `examples/your-motion.md` and link it from your entry. Keep descriptions in English and prompts in their original language. Credit the original creator and mention required references, tools or important edits.

**No JSON editing, build commands or submission forms are required.** One work per PR. No follower, view or star threshold. Suggest a new category in your PR if none fits.

## For maintainers

The README stays manually editable. Review previews, attribution and prompt sources before merging. Normalize structured data separately using the [data contract](docs/DATA_FORMAT.md), then run `python3 scripts/build.py` and `python3 scripts/validate.py`. Building never replaces the README.

For corrections or removals, open an issue or PR identifying the work and requested change. See [third-party content](THIRD_PARTY.md) and [source verification](docs/SOURCING.md).
