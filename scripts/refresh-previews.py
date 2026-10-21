#!/usr/bin/env python3
"""Rebuild short inline GIFs from reviewed source ranges; requires FFmpeg."""
import argparse,json,pathlib,shutil,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]
def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--ffmpeg',default=shutil.which('ffmpeg'));parser.add_argument('--id');args=parser.parse_args()
 if not args.ffmpeg:parser.error('Pass --ffmpeg /absolute/path/to/ffmpeg')
 records=json.loads((ROOT/'data/previews.json').read_text())
 if args.id:
  records=[r for r in records if r['id']==args.id]
  if not records:parser.error('Unknown preview ID')
 for r in records:
  dest=ROOT/r['asset'];dest.parent.mkdir(parents=True,exist_ok=True);tmp=dest.with_name(dest.stem+'.new.gif')
  filt=f"fps={r['fps']},scale=320:240:force_original_aspect_ratio=decrease:force_divisible_by=2:flags=lanczos,split[a][b];[a]palettegen=max_colors=80:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=5"
  try:
   subprocess.run([args.ffmpeg,'-hide_banner','-loglevel','error','-y','-ss',str(r['startSeconds']),'-i',r['video'],'-t',str(r['durationSeconds']),'-filter_complex',filt,'-loop','0',str(tmp)],check=True);tmp.replace(dest)
  finally:tmp.unlink(missing_ok=True)
  print('Updated',r['id'])
if __name__=='__main__':main()
