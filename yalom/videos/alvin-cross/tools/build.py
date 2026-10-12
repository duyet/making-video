"""Build assets/img (graded, cropped refs) and index.html from the shot list + VO timing."""
import json,os,random
from PIL import Image,ImageOps,ImageFilter,ImageEnhance
HERE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF=os.path.join(HERE,'..','..','ref','final')
IDX=[l.rstrip('\n').split(' ',1) for l in open(os.environ['REF_INDEX'])]
REFS={n:f for n,f in IDX}
W,H=1920,1080; LEAD=0.8; GAP=0.12; TAIL=1.8; XF=1.0
lines={l['id']:l['text'] for l in json.load(open(os.path.join(HERE,'narration','lines.json')))}
dur=json.load(open(os.path.join(HERE,'assets','vo','durations.json')))

# scene -> list of (ref number, cue phrase or None, crop box fractions l,t,r,b)
E=0.06
SHOTS={
 's01':[('F24',None,None),('F31','Hôm nay',None)],
 's02':[('F33',None,None)],
 's03':[('F23',None,None),('F13','Bên cạnh',None),('F20','Tôi bối rối',None)],
 's04':[('F15',None,None)],
 's05':[('F11',None,None),('F01','Ngoài ba mươi',None),('F10','mặc áo',None)],
 's06':[('F05',None,None),('F21','Jason tìm đến',None)],
 's07':[('F34',None,None),('F08','Vậy mà',None),('F19','ánh mắt Jason',None)],
 's08':[('F06',None,None),('F30','Jason ôm',None)],
 's10':[('F27',None,None),('F28','lao thẳng',None),('F29','Con quạ của',None)],
 's12':[('F32',None,None),('F14','Nhưng sâu',None)],
 's14':[('F04',None,None),('F35','người bạn Ralph',None),('F07','lồng phổi',None),('F36','chấm hết',None)],
 's16':[('F26',None,None)],
 's17':[('F17',None,None)],
 's18':[('F12',None,None),('F25','Một tâm trí',None)],
 's20':[('F18',None,(0.05,0.05,0.95,0.86))],
 's21':[('F16',None,None)],
 's22':[('F03',None,None),('F02','Bà ấy',None),('F09','để tôi mở lòng',None)],
 's23':[('F22',None,None)],
}
SFX={ # sfx id -> (scene, offset, volume)
 'wind':[('s01',-1.0,0.35),('s23',-0.5,0.3)],'clock':[('s05',0,0.18),('s16',0,0.2)],
 'hum':[('s06',-0.5,0.16)],'raven':[('s10',3.0,0.35)],'paper':[('s21',-0.3,0.3)],
}
def cue(sid,phrase):
  a=json.load(open(os.path.join(HERE,'assets','vo',sid+'.align.json')))
  txt=''.join(a['characters']); i=txt.find(phrase)
  if i<0: raise SystemExit(f'cue not found {sid}: {phrase}')
  return max(0.0,a['character_start_times_seconds'][i]-0.25)

def prep(num,box):
  out=os.path.join(HERE,'assets','img',f'{num}.jpg')
  rd=os.path.join(HERE,'assets','redraw',f'{num}.png')
  if os.path.exists(rd): im=Image.open(rd).convert('RGB'); box=None  # redrawn shot: full frame, default edge trim
  else: im=Image.open(os.path.join(REF,REFS[num])).convert('RGB')
  w,h=im.size; l,t,r,b=box or (E,E*1.4,1-E,1-E*1.4)
  im=im.crop((int(l*w),int(t*h),int(r*w),int(b*h)))
  im=ImageOps.fit(im,(W,H),Image.LANCZOS)
  g=ImageOps.grayscale(im); g=ImageEnhance.Contrast(g).enhance(1.06)
  tone=ImageOps.colorize(g,black=(22,20,18),white=(244,238,226),mid=(128,122,112))
  Image.blend(im,tone,0.82).save(out,quality=90)
  return f'assets/img/{num}.jpg'

os.makedirs(os.path.join(HERE,'assets','img'),exist_ok=True)

t=LEAD; scenes=[]; shots=[]
for sid in SHOTS:
  scenes.append((sid,t)); t+=dur[sid]+GAP
total=t-GAP+TAIL
sstart=dict(scenes)
order=list(SHOTS)
for k,sid in enumerate(order):
  st=sstart[sid]; end_scene=(sstart[order[k+1]] if k+1<len(order) else total)
  items=SHOTS[sid]
  for j,(num,phrase,box) in enumerate(items):
    s=st+(cue(sid,phrase) if phrase else 0) - (0 if (k==0 and j==0) else 0)
    if k==0 and j==0: s=0
    shots.append([num,s,box])
for i,sh in enumerate(shots):
  e=shots[i+1][1]+XF if i+1<len(shots) else total
  sh.append(e-sh[1])

exec(open(os.path.join(HERE,'tools','motion.py')).read())
aud=[]
for sid,st in scenes:
  aud.append(f'      <audio id="vo-{sid}" src="assets/vo/{sid}.mp3" data-start="{st:.3f}" data-duration="{dur[sid]:.3f}" data-track-index="10" data-volume="1"></audio>')
def fade(d,fi,fo,v=1):
  return " data-automation='"+json.dumps({'version':1,'lanes':[{'target':'volume','points':[{'t':0,'v':0},{'t':fi,'v':v},{'t':round(d-fo,3),'v':v},{'t':round(d,3),'v':0}]}]})+"'"
have=lambda p: os.path.exists(os.path.join(HERE,p)) and os.path.getsize(os.path.join(HERE,p))>1000
for name,uses in SFX.items():
  if not have(f'assets/sfx/{name}.mp3'): continue
  for n,(sid,off,vol) in enumerate(uses):
    import subprocess
    sd=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',os.path.join(HERE,f'assets/sfx/{name}.mp3')]))
    st=max(0,sstart[sid]+off); sd=min(sd,total-st); aud.append(f'      <audio id="sfx-{name}-{n}" src="assets/sfx/{name}.mp3" data-start="{st:.3f}" data-duration="{sd:.3f}" data-track-index="12" data-volume="{vol}"{fade(sd,min(2.5,sd/4),min(3,sd/3))}></audio>')
if have('assets/music/bed.mp3'):
  md=min(total,180.0)
  aud.append(f'      <audio id="music-bed" src="assets/music/bed.mp3" data-start="0" data-duration="{md:.3f}" data-track-index="11" data-volume="0.3"></audio>')

js+=[f'tl.fromTo("#fade",{{opacity:1}},{{opacity:0,duration:1.6,ease:"sine.out"}},0);',
     f'tl.fromTo("#fade",{{opacity:0}},{{opacity:1,duration:2.4,ease:"sine.in",immediateRender:false}},{total-2.6:.3f});',
     f'tl.fromTo("#grain",{{backgroundPosition:"0px 0px"}},{{backgroundPosition:"{int(total*12)*397}px {int(total*12)*233}px",duration:{total:.3f},ease:"steps({int(total*12)})"}},0);']
tpl=open(os.path.join(HERE,'tools','index.tpl.html')).read()
open(os.path.join(HERE,'index.html'),'w').write(tpl.replace('{{TOTAL}}',f'{total:.3f}').replace('{{SHOTS}}','\n'.join(html)).replace('{{AUDIO}}','\n'.join(aud)).replace('{{JS}}','\n      '.join(js)))
json.dump({'total':total,'scenes':scenes,'shots':[(n,round(s,2),round(d,2)) for n,s,b,d in shots]},open(os.path.join(HERE,'timeline.json'),'w'),indent=1)
print('total',round(total,2),'shots',len(shots))
