"""Redraw one shot via HeyGen prompt-avatar generation (prompt + up to 3 reference images, 16:9).
usage: heygen_redraw.py <out_name> <prompt_file> <ref1> [ref2] [ref3]"""
import sys,os,json,base64,subprocess,time,urllib.request,ssl
HB=os.path.expanduser('~/.local/bin/heygen'); OUT=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'assets','redraw')
name,pf,refs=sys.argv[1],sys.argv[2],sys.argv[3:6]
STYLE=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'style.txt')).read().strip()
body={'type':'prompt','name':f'alvin-cross-{name}','aspect_ratio':'16:9','prompt':open(pf).read().strip()+' '+STYLE,
      'reference_images':[{'type':'base64','media_type':'image/jpeg','data':base64.b64encode(open(r,'rb').read()).decode()} for r in refs]}
req=os.path.join(OUT,f'{name}.req.json'); json.dump(body,open(req,'w'))
def hg(*a): 
  r=subprocess.run([HB,*a],capture_output=True,text=True); 
  try: return json.loads(r.stdout)
  except Exception: raise SystemExit(f'heygen error: {r.stdout} {r.stderr}')
r=hg('avatar','create','-d',req); os.remove(req)
print(json.dumps(r)[:600],flush=True)
d=r.get('data',{}); gid=(d.get('avatar_group') or {}).get('id'); aid=(d.get('avatar_item') or d.get('avatar') or {}).get('id')
for _ in range(120):
  g=hg('avatar','looks','get',aid) if aid else hg('avatar','get',gid)
  gd=g.get('data',{}); url=gd.get('image_url') or gd.get('preview_image_url'); st=gd.get('status')
  if url and st in (None,'completed','ready','succeeded','active'): break
  if st=='failed': raise SystemExit(f'failed: {g}')
  time.sleep(5)
else: raise SystemExit('timeout')
data=urllib.request.urlopen(url,context=ssl.create_default_context(cafile='/etc/ssl/cert.pem')).read()
open(os.path.join(OUT,f'{name}.png'),'wb').write(data); print('saved',name,len(data))
