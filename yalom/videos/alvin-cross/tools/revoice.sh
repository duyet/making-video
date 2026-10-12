#!/bin/sh
# Re-voice given line ids with the chosen voice (Tung Dang, eleven_v3), then apply the 1.07x atempo + scaled alignment.
cd "$(dirname "$0")/.."
IDS="$1"
(cd narration && SSL_CERT_FILE=/etc/ssl/cert.pem python3 tts.py 3VnrjnYrskPMDsapTr8X eleven_v3 "$IDS") || exit 1
cd assets/vo && IDS="$IDS" python3 - <<'PY'
import json,subprocess,os,shutil
R=1.07; d=json.load(open('durations.json'))
for sid in os.environ['IDS'].split(','):
  shutil.copy(f'{sid}.mp3',f'raw/{sid}.mp3'); shutil.copy(f'{sid}.align.json',f'raw/{sid}.align.json')
  subprocess.run(['ffmpeg','-v','error','-y','-i',f'raw/{sid}.mp3','-filter:a',f'atempo={R}','-b:a','160k',f'{sid}.mp3'],check=True)
  a=json.load(open(f'raw/{sid}.align.json'))
  for k in ('character_start_times_seconds','character_end_times_seconds'): a[k]=[t/R for t in a[k]]
  json.dump(a,open(f'{sid}.align.json','w'),ensure_ascii=False)
  d[sid]=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{sid}.mp3']))
  print(sid,round(d[sid],2))
json.dump(d,open('durations.json','w'),indent=1); print('speech total',round(sum(d.values()),1))
PY
