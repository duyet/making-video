"""Build assets/img (graded, cropped refs), the silent picture index.html and the audio plan mix.json from a script's shot list + its shared VO slots (narration/fit.py).
usage: build.py <script>"""
import json,math,os,random,sys
from PIL import Image,ImageOps,ImageFilter,ImageEnhance, ImageStat
HERE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF=os.path.join(HERE,'..','..','ref','final')
SCRIPT=sys.argv[1]; SC=os.path.join(HERE,'narration','scripts',SCRIPT)
IDX=[l.rstrip('\n').split(' ',1) for l in open(os.path.join(SC,'ref-index.txt'))]
REFS={n:f for n,f in IDX}
W,H=1920,1080; LEAD=0.8; GAP=0.12; TAIL=1.8; XF=1.0; XFS={'cut':0,'dissolve':1.6}
lines={l['id']:l['text'] for l in json.load(open(os.path.join(SC,'lines.json')))}
fit=json.load(open(os.path.join(SC,'slots.json'))); dur,CUES=fit['slots'],fit['cues']
# shots: scene -> list of {ref, cue phrase, box (crop of the original ref), crop (crop of any image, incl. redraws), ink, fallback,
# xf (transition into the shot: 'cut' = 0, 'dissolve' = 1.6 or seconds; default the XF crossfade)}; cam/fx: per-ref camera move and atmosphere; sfx id -> (scene, offset, volume)
E=0.06
sh=json.load(open(os.path.join(SC,'shots.json'))); SHOTS,SFX,CAM,FX=sh['shots'],sh['sfx'],sh['cam'],sh['fx']
SCRIPT_DATA=json.load(open(os.path.join(SC,'script.json')))  # act cards, file card, end title

def lift(im, target=128):
  # adaptive exposure: gamma-lift dark frames toward a mid-grey mean, raise the black floor
  m=max(ImageStat.Stat(ImageOps.grayscale(im)).mean[0],1)
  gam=min(max(math.log(target/255)/math.log(m/255),0.55),1.0) if m<target else 1.0
  lut=[int(18+237*((i/255)**gam)) for i in range(256)]
  return im.point(lut*3)

def prep(num,box,crop=None):  # crop: l,t,r,b fractions applied to the redrawn image too (box only applies to the original ref)
  name=num+(''.join(f'-{x:g}' for x in crop) if crop else '')
  out=os.path.join(HERE,'assets','img',f'{name}.jpg')
  rd=os.path.join(HERE,'assets','redraw',f'{num}.png')
  if os.path.exists(rd): im=Image.open(rd).convert('RGB'); box=None  # redrawn shot: full frame, default edge trim
  else: im=Image.open(os.path.join(REF,REFS[num])).convert('RGB')
  box=crop or box
  w,h=im.size; l,t,r,b=box or (E,E*1.4,1-E,1-E*1.4)
  im=im.crop((int(l*w),int(t*h),int(r*w),int(b*h)))
  im=ImageOps.fit(im,(W,H),Image.LANCZOS)
  im=lift(im)
  g=ImageOps.grayscale(im); g=ImageEnhance.Contrast(g).enhance(1.06)
  tone=ImageOps.colorize(g,black=(22,20,18),white=(244,238,226),mid=(128,122,112))
  Image.blend(im,tone,0.12).save(out,quality=90)
  return f'assets/img/{name}.jpg'

os.makedirs(os.path.join(HERE,'assets','img'),exist_ok=True)

# a line's picture can hold before its VO (hold_before) or after it (hold_after) and then cut to black (black_after), all in script.json
HOLD,AFTER,BLACK=SCRIPT_DATA.get('hold_before',{}),SCRIPT_DATA.get('hold_after',{}),SCRIPT_DATA.get('black_after',{})
t=LEAD; scenes=[]; shots=[]; vo={}
for sid in SHOTS:
  scenes.append((sid,t)); vo[sid]=t+HOLD.get(sid,0); t=vo[sid]+dur[sid]+AFTER.get(sid,0)+BLACK.get(sid,0)+GAP
total=t-GAP+TAIL
sstart=dict(scenes)
order=list(SHOTS)
# a shot whose image is not drawn yet uses its fallback ref, or is left out (the previous shot holds); if a line's first shot
# is left out, the next one starts with the line and takes over its ink flag
has_img=lambda ref: os.path.exists(os.path.join(HERE,'assets','redraw',f'{ref}.png')) or ref in REFS
standins=[]
for k,sid in enumerate(order):
  st=sstart[sid]; items=[]
  for j,it in enumerate(SHOTS[sid]):
    if has_img(it['ref']): items.append((j,it)); continue
    fb=it.get('fallback'); fb=fb if fb and has_img(fb) else None
    standins.append(f"{sid} {it['ref']} -> {fb or 'left out'}")
    if fb: items.append((j,{**it,'ref':fb}))
  if items and items[0][0]>0: items[0]=(0,{**items[0][1],'cue':None,'ink':SHOTS[sid][0].get('ink') or items[0][1].get('ink'),'xf':SHOTS[sid][0].get('xf')})
  for j,it in items:
    phrase=it.get('cue')
    s=0 if (k==0 and j==0) else (vo[sid]+CUES[sid][phrase] if phrase else st)
    shots.append({'ref':it['ref'],'start':s,'box':it.get('box'),'crop':it.get('crop'),'ink':bool(it.get('ink')),'cam':it.get('cam') or CAM[it['ref']],'xf':XFS.get(it.get('xf'),it.get('xf'))})
for i,sh in enumerate(shots):  # a shot runs until the next one has faded in over it; a hard cut (xf 0) ends it on the cue
  nx=shots[i+1]['xf'] if i+1<len(shots) else None
  e=shots[i+1]['start']+(XF if nx is None else nx) if i+1<len(shots) else total
  sh['dur']=e-sh['start']
if standins: print('stand-ins (image not drawn yet):',', '.join(standins))

exec(open(os.path.join(HERE,'tools','motion.py')).read())
# audio is mixed per voice by tools/mux.py: VO slots, music bed under the whole timeline, SFX with linear fades
mix={'total':round(total,3),'vo':{sid:round(t,3) for sid,t in vo.items()},'sfx':[]}
have=lambda p: os.path.exists(os.path.join(HERE,p)) and os.path.getsize(os.path.join(HERE,p))>1000
for name,uses in SFX.items():
  if not have(f'assets/sfx/{name}.mp3'): continue
  for n,(sid,off,vol) in enumerate(uses):
    import subprocess
    sd=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',os.path.join(HERE,f'assets/sfx/{name}.mp3')]))
    st=max(0,sstart[sid]+off); sd=min(sd,total-st)
    mix['sfx'].append({'src':f'assets/sfx/{name}.mp3','start':round(st,3),'dur':round(sd,3),'volume':vol,'fade_in':round(min(2.5,sd/4),3),'fade_out':round(min(3,sd/3),3)})
if have('assets/music/bed.mp3'):
  mix['music']={'src':'assets/music/bed.mp3','dur':round(total,3),'volume':1,'fade_in':3,'fade_out':5,'loop_end':166}  # full level before ducking, as the old composition played it; the bed's own ending starts ~166s, loops cut there
json.dump(mix,open(os.path.join(SC,'mix.json'),'w'),indent=1)

for n,(sid,b) in enumerate(BLACK.items()):  # hard cut to black on the last word (or after the hold), lifting as the next line starts
  st=vo[sid]+dur[sid]+AFTER.get(sid,0); d=b+GAP+0.6
  html.append(f'      <div id="black{n}" class="clip" data-start="{st:.3f}" data-duration="{d:.3f}" data-track-index="4" style="position:absolute;inset:0;background:#000"></div>')
  js.append(f'tl.to("#black{n}",{{opacity:0,duration:0.6,ease:"sine.inOut"}},{st+d-0.6:.3f});')
js+=[f'tl.fromTo("#fade",{{opacity:1}},{{opacity:0,duration:1.6,ease:"sine.out"}},0);',
     f'tl.fromTo("#fade",{{opacity:0}},{{opacity:1,duration:2.4,ease:"sine.in",immediateRender:false}},{total-2.6:.3f});',
     f'tl.fromTo("#grain",{{backgroundPosition:"0px 0px"}},{{backgroundPosition:"{int(total*12)*397}px {int(total*12)*233}px",duration:{total:.3f},ease:"steps({int(total*12)})"}},0);']
tpl=open(os.path.join(HERE,'tools','index.tpl.html')).read()
open(os.path.join(HERE,'index.html'),'w').write(tpl.replace('{{TOTAL}}',f'{total:.3f}').replace('{{SHOTS}}','\n'.join(html)).replace('{{JS}}','\n      '.join(js)))
json.dump({'total':total,'scenes':scenes,'shots':[(sh['ref'],round(sh['start'],2),round(sh['dur'],2)) for sh in shots]},open(os.path.join(HERE,'timeline.json'),'w'),indent=1)
print('total',round(total,2),'shots',len(shots))
