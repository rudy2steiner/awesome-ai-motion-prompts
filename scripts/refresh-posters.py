#!/usr/bin/env python3
"""Re-extract reviewed poster frames. Requires FFmpeg with libwebp support."""
import argparse,json,pathlib,shutil,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]
def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--ffmpeg',default=shutil.which('ffmpeg'));parser.add_argument('--id',help='Refresh one entry instead of every reviewed poster');args=parser.parse_args()
 if not args.ffmpeg:parser.error('FFmpeg is required; pass --ffmpeg /absolute/path/to/ffmpeg')
 records=json.loads((ROOT/'data/poster-frames.json').read_text())
 if args.id:
  records=[r for r in records if r['id']==args.id]
  if not records:parser.error('No reviewed frame for that entry ID')
 for r in records:
  target=ROOT/'public'/r['poster'].lstrip('/');temp=target.with_name(target.stem+'.new.webp')
  try:
   subprocess.run([args.ffmpeg,'-hide_banner','-loglevel','error','-y','-ss',str(r['timeSeconds']),'-i',r['video'],'-frames:v','1','-vf','scale=640:-2','-c:v','libwebp','-quality','88',str(temp)],check=True)
   temp.replace(target)
  finally:temp.unlink(missing_ok=True)
  print(f"Updated {r['id']} at {r['timeSeconds']}s")
if __name__=='__main__':main()
