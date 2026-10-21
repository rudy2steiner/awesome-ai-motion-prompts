#!/usr/bin/env python3
"""Build structured exports and the candidate index; preserve the community-edited README."""
import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
def main():
 entries=read('data/motion-prompts.json');candidates=read('data/candidates.json')['cases'];resources=read('data/resources.json')
 ts=ROOT/'src/data/promptMotion.ts';text=ts.read_text();header=text[text.index('export const MOTION_CATEGORIES'):text.index('export const MOTION_ENTRIES')]
 ts.write_text('/** Generated from data/motion-prompts.json. Run python3 scripts/build.py. */\n'+header+'export const MOTION_ENTRIES: MotionEntry[] = '+json.dumps(entries,ensure_ascii=False,indent=2)+';\nexport const MOTION_RESOURCES = '+json.dumps(resources,ensure_ascii=False,indent=2)+';\n')
 lines=['# Research candidates','','Discovery leads are not recommendations or verified full prompts. Existing X metadata checks are preserved separately from model, prompt and playback review.','','| Work | Reported model | Platform | Prompt status |','| --- | --- | --- | --- |']
 for e in candidates:lines.append(f'| [{e["title"].replace("|","/").replace(chr(10)," ")}]({e["sourceUrl"]}) | {e["model"]} | {e.get("platform","X")} | {e.get("promptStatus","not_collected")} |')
 (ROOT/'docs/CANDIDATES.md').write_text('\n'.join(lines)+'\n')
 playback=read('data/playback.json')
 lines=['# Full list','','[▶ Play online](https://www.open-prompts.com/motion-prompts) · [Browse categories](../README.md#prompt-library) · [Submit a PR](../CONTRIBUTING.md)','','## Collected prompts','','| Motion | Model | Watch | Prompt |','| --- | --- | --- | --- |']
 for e in entries:
  watch=f'[Play online]({playback[e["id"]]})' if e['id'] in playback else f'[Original post]({e["sourceUrl"]})'
  title=e['title'].replace('|','/')
  lines.append(f'| {title} | {e["model"]} | {watch} | [Prompt](../examples/{e["id"]}.md) |')
 lines+=['','## Research candidates','','These works are discovery leads, not verified full prompts or published online-gallery entries. Open the original post to review the video.','','| Motion | Reported model | Watch | Prompt source |','| --- | --- | --- | --- |']
 for e in candidates:
  title=e['title'].replace('|','/').replace(chr(10),' ')
  prompt=f'[Source to check]({e["promptSourceUrl"]})' if e.get('promptSourceUrl') else 'Not collected'
  lines.append(f'| {title} | {e["model"]} | [Original post]({e["sourceUrl"]}) | {prompt} |')
 (ROOT/'docs/FULL_LIST.md').write_text('\n'.join(lines)+'\n')
 print(f'Built {len(entries)} records and {len(candidates)} candidates. README.md left unchanged.')
if __name__=='__main__':main()
