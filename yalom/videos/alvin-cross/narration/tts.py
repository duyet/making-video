import json,os,sys,base64,urllib.request,subprocess
P=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(P,'..','assets','vo')
VOICE=sys.argv[1] if len(sys.argv)>1 else 'QqID1ZB0DTItNxAKGBNW'; MODEL=sys.argv[2] if len(sys.argv)>2 else 'eleven_v3'
only=sys.argv[3].split(',') if len(sys.argv)>3 else None
key=os.environ['ELEVENLABS_API_KEY']; meta={}
for l in json.load(open(os.path.join(P,'lines.json'))):
  if only and l['id'] not in only: continue
  body=json.dumps({'text':l['text'],'model_id':MODEL,'language_code':'vi','voice_settings':{'stability':0.5,'similarity_boost':0.75}}).encode()
  req=urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE}/with-timestamps?output_format=mp3_44100_128',data=body,headers={'xi-api-key':key,'Content-Type':'application/json'})
  r=json.load(urllib.request.urlopen(req,timeout=180))
  mp3=os.path.join(OUT,l['id']+'.mp3'); open(mp3,'wb').write(base64.b64decode(r['audio_base64']))
  json.dump(r.get('alignment'),open(os.path.join(OUT,l['id']+'.align.json'),'w'),ensure_ascii=False)
  d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',mp3]))
  meta[l['id']]=d; print(l['id'],round(d,2),flush=True)
old=json.load(open(os.path.join(OUT,'durations.json'))) if os.path.exists(os.path.join(OUT,'durations.json')) else {}
old.update(meta); json.dump(old,open(os.path.join(OUT,'durations.json'),'w'),indent=1)
print('total',round(sum(old.values()),1))
