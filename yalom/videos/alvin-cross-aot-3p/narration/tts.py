"""TTS one script with one voice (narration/voices.json) into raw 1x takes in scripts/<script>/<voice>/raw/; fit.py turns them into timed lines.
usage: tts.py <script> <voice> [id,id,...]  -- listed ids are always re-taken; otherwise only lines with no take or changed text are generated."""
import json,os,sys,base64,urllib.request,urllib.error,subprocess,time
os.environ.setdefault('SSL_CERT_FILE','/etc/ssl/cert.pem')
P=os.path.dirname(os.path.abspath(__file__))
SCRIPT,VOICE=sys.argv[1],sys.argv[2]; force=sys.argv[3].split(',') if len(sys.argv)>3 else []
v=json.load(open(os.path.join(P,'voices.json')))[VOICE]
SC=os.path.join(P,'scripts',SCRIPT); RAW=os.path.join(SC,VOICE,'raw'); os.makedirs(RAW,exist_ok=True)
lines=json.load(open(os.path.join(SC,'lines.json')))
TK=os.path.join(RAW,'takes.json'); takes=json.load(open(TK)) if os.path.exists(TK) else {}
probe=lambda f: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
key=os.environ['ELEVENLABS_API_KEY']
for l in lines:
  sid=l['id']
  if sid not in force and takes.get(sid)==l['text']: continue
  body=json.dumps({'text':l['text'],'model_id':v['model'],'language_code':'vi','voice_settings':v['settings']}).encode()
  req=urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{v["voice_id"]}/with-timestamps?output_format=mp3_44100_128',data=body,headers={'xi-api-key':key,'Content-Type':'application/json'})
  for wait in (5,15,30,60,0):  # 429 = account concurrency limit: back off and retry
    try: r=json.load(urllib.request.urlopen(req,timeout=180)); break
    except urllib.error.HTTPError as e:
      if e.code!=429 or not wait: raise
      time.sleep(wait)
  open(os.path.join(RAW,sid+'.mp3'),'wb').write(base64.b64decode(r['audio_base64']))
  json.dump(r.get('alignment'),open(os.path.join(RAW,sid+'.align.json'),'w'),ensure_ascii=False)
  takes[sid]=l['text']; json.dump(takes,open(TK,'w'),ensure_ascii=False,indent=1)
  print('take',sid,round(probe(os.path.join(RAW,sid+'.mp3')),2),flush=True)
