"""QA a muxed render against the build that made it (timeline.json + index.html): length, unplanned black, loudness, the right shot on screen
mid-way through every shot, and shot-length pacing. Writes a labelled contact sheet of those frames next to the video.
usage: qa.py <video.mp4> [--ref <older render.mp4>]   exit 1 if any check fails"""
import json,os,re,statistics,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
HERE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VID=sys.argv[1]; REF=sys.argv[sys.argv.index('--ref')+1] if '--ref' in sys.argv else None
FLASH=2.5; MEDIAN=4.0; BRIEF=3.3; LEN_TOL=0.25; LOUD_TOL=1.5
tl=json.load(open(os.path.join(HERE,'timeline.json'))); idx=open(os.path.join(HERE,'index.html')).read()
total,shots=tl['total'],tl['shots']
srcs=[s for _,s in re.findall(r'<img id="img(\d+)" class="clip shot" src="([^"]+)"',idx)]
assert len(srcs)==len(shots),'index.html and timeline.json are from different builds'
checks=[]
def check(name,ok,detail): checks.append((name,ok,detail)); print(('PASS' if ok else 'FAIL'),name,'|',detail)

dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',VID]))
check('length',abs(dur-total)<=LEN_TOL,f'video {dur:.2f}s, timeline {total:.2f}s')

planned=[(0,1.8),(total-2.8,total)]+[(float(a),float(a)+float(b)) for a,b in re.findall(r'id="black\d+" class="clip" data-start="([\d.]+)" data-duration="([\d.]+)"',idx)]
o=subprocess.run(['ffmpeg','-hide_banner','-i',VID,'-vf','scale=320:-2,blackdetect=d=0.25:pix_th=0.08','-an','-f','null','-'],capture_output=True,text=True).stderr
black=[(float(a),float(b)) for a,b in re.findall(r'black_start:([\d.]+) black_end:([\d.]+)',o)]
stray=[(a,b) for a,b in black if not any(a>=p0-0.3 and b<=p1+0.3 for p0,p1 in planned)]
check('black',not stray,f'{len(black)} black spans, unplanned: {[(round(a,1),round(b,1)) for a,b in stray]}')

def loud(f):
  e=subprocess.run(['ffmpeg','-hide_banner','-i',f,'-vn','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
  return float(re.findall(r'I:\s+(-?[\d.]+) LUFS',e)[-1]),float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS',e)[-1])
I,pk=loud(VID)
if REF:
  RI,_=loud(REF); check('loudness',abs(I-RI)<=LOUD_TOL and pk<=-0.5,f'{I:.1f} LUFS (ref {RI:.1f}), true peak {pk:.1f} dBFS')
else: check('loudness',pk<=-0.5,f'{I:.1f} LUFS, true peak {pk:.1f} dBFS')

def vec(im):  # small grey, centre-cropped for the Ken Burns zoom, mean/std normalised
  im=im.convert('L'); w,h=im.size; c=0.07
  a=list(im.crop((int(w*c),int(h*c),int(w*(1-c)),int(h*(1-c)))).resize((64,36)).tobytes())
  m=statistics.fmean(a); sd=statistics.pstdev(a)+1e-6
  return [(x-m)/sd for x in a]
lib=[vec(Image.open(os.path.join(HERE,s))) for s in srcs]
frames=[]; miss=[]
for i,(ref,st,d) in enumerate(shots):
  t=st+d/2
  raw=subprocess.run(['ffmpeg','-v','error','-ss',f'{t:.3f}','-i',VID,'-frames:v','1','-vf','scale=480:270','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
  if len(raw)<480*270*3: miss.append(f'{ref}@{t:.1f}s past the end of the video'); continue
  fr=Image.frombytes('RGB',(480,270),raw); frames.append((fr,i,ref,t,d))
  fv=vec(fr); sc=[sum(map(float.__mul__,v,fv))/len(v) for v in lib]; best=max(range(len(sc)),key=sc.__getitem__)
  if srcs[best]!=srcs[i]: miss.append(f'{ref}@{t:.1f}s looks like {shots[best][0]} ({sc[best]:.2f} vs {sc[i]:.2f})')
check('shots on screen',not miss,f'{len(shots)-len(miss)}/{len(shots)} match'+(': '+'; '.join(miss) if miss else ''))

# screen time = cut to next cut (fade-in midpoint to fade-out midpoint); 'dur' would also count the crossfade overlap
seen=[(shots[i+1][1] if i+1<len(shots) else total)-st for i,(_,st,_) in enumerate(shots)]
flash=[f'{shots[i][0]} {x:.1f}s' for i,x in enumerate(seen) if x<FLASH]; brief=[f'{shots[i][0]} {x:.1f}s' for i,x in enumerate(seen) if FLASH<=x<BRIEF]
check('pacing',not flash and statistics.median(seen)>=MEDIAN,f'{len(shots)} shots on screen min {min(seen):.2f}s, median {statistics.median(seen):.2f}s (bar {MEDIAN}s), {len(shots)/total*60:.1f} cuts/min, flashes <{FLASH}s: {flash or "none"}'+(f'; brief (info) <{BRIEF}s: {brief}' if brief else ''))
cols=8; W,H=240,135; sheet=Image.new('RGB',(cols*W,((len(frames)+cols-1)//cols)*(H+18)),'white'); dr=ImageDraw.Draw(sheet)
f=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',13)
for k,(fr,i,ref,t,d) in enumerate(frames):
  x,y=(k%cols)*W,(k//cols)*(H+18); sheet.paste(fr.resize((W,H)),(x,y+18)); dr.text((x+3,y+2),f'{i} {ref} {t:.0f}s ({d:.1f}s)',fill='black',font=f)
out=os.path.splitext(VID)[0]+'.qa.jpg'; sheet.save(out,quality=80); print('contact sheet',out)
sys.exit(0 if all(ok for _,ok,_ in checks) else 1)
