"""Shared per-script VO timeline. Each line's slot = median over voices of its length at the voice's tempo, raised only when a voice
cannot reach it even at HI speed-up with its internal pauses cut down to MINP.
Every voice is then fitted to the slots in one pass from its raw take: atempo = tempo x fit (fit clamped to LO..HI), and what the clamp
leaves over is taken out of, or added to, the line's own pauses (at most MAXADD each, any rest trails the line). Each shots.json cue
is placed at the median of the voices' fitted cue times.
usage: fit.py <script>          -> scripts/<script>/slots.json + scripts/<script>/<voice>/<id>.mp3, <id>.align.json for every voice
       fit.py <script> <voice>  -> fit one more voice to the existing slots (cues unchanged; it may go past HI so it never overruns a slot)"""
import json,os,re,sys,subprocess,statistics
P=os.path.dirname(os.path.abspath(__file__))
SCRIPT=sys.argv[1]; ADD=sys.argv[2] if len(sys.argv)>2 else None; SC=os.path.join(P,'scripts',SCRIPT)
LO,HI=0.9,1.12; LEADIN=0.25  # cut to a shot this long before its cue word
MINP,MAXADD=0.25,0.6  # fitted pause bounds: never shorter than MINP, never lengthened by more than MAXADD
voices=json.load(open(os.path.join(P,'voices.json')))
lines=json.load(open(os.path.join(SC,'lines.json'))); ids=[l['id'] for l in lines]
SHOTS=json.load(open(os.path.join(SC,'shots.json')))['shots']
probe=lambda f: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
def pauses(f):  # internal silences of a raw take, (start, end) in seconds
  o=subprocess.run(['ffmpeg','-hide_banner','-i',f,'-af','silencedetect=n=-35dB:d=0.2','-f','null','-'],capture_output=True,text=True).stderr
  d=probe(f); ss=[float(x) for x in re.findall(r'silence_start: (-?[\d.]+)',o)]; se=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',o)]
  return [(a,b) for a,b in zip(ss,se) if a>0.05 and b<d-0.05]
use=[]
for slug in ([ADD] if ADD else voices):
  tk=os.path.join(SC,slug,'raw','takes.json'); takes=json.load(open(tk)) if os.path.exists(tk) else {}
  if all(takes.get(l['id'])==l['text'] for l in lines): use.append(slug)
  else: print(f'{slug}: no current takes for every line (run tts.py {SCRIPT} {slug}); left out of the timeline')
if not use: raise SystemExit('no voice has current takes for every line')
if ADD: prev=json.load(open(os.path.join(SC,'slots.json')))
raw={(v,sid):probe(os.path.join(SC,v,'raw',sid+'.mp3')) for v in use for sid in ids}
pz={(v,sid):pauses(os.path.join(SC,v,'raw',sid+'.mp3')) for v in use for sid in ids}
nat={k:raw[k]/voices[k[0]]['tempo'] for k in raw}
def shortest(v,sid):
  r=voices[v]['tempo']*HI; return raw[v,sid]/r-sum(max(0,(b-a)/r-MINP) for a,b in pz[v,sid])
slots={} if not ADD else prev['slots']
for sid in ([] if ADD else ids):
  m=statistics.median(nat[v,sid] for v in use); need=max(shortest(v,sid) for v in use); slots[sid]=round(max(m,need),3)
  if need>m: print(f'{sid}: slot raised {m:.2f} -> {need:.2f}s so every voice fits')
fits={}; at={}
for v in use:
  R=voices[v]['tempo']; fits[v]={}
  for sid in ids:
    f=nat[v,sid]/slots[sid]; fc=min(max(f,LO),HI)
    if shortest(v,sid)>slots[sid]:  # only when adding a voice to fixed slots: speed past HI until the line fits with its pauses at MINP
      pp=pz[v,sid]; fc=(raw[v,sid]-sum(b-a for a,b in pp))/(R*(slots[sid]-len(pp)*MINP)); print(f'{v} {sid}: needs x{fc:.2f}, past the x{HI} clamp')
    r=R*fc; fits[v][sid]=round(fc,3)
    pp=pz[v,sid]; D=slots[sid]-raw[v,sid]/r  # what the clamped tempo leaves over, in fitted seconds
    if D<-1e-3:
      room=[max(0,(b-a)/r-MINP) for a,b in pp]; k=-D/sum(room); change=[-x*k for x in room]
    elif D>1e-3 and pp: change=[min(MAXADD,D/len(pp))]*len(pp)
    else: change=[0]*len(pp)
    if f<LO or f>HI: print(f'{v} {sid}: needs x{f:.2f}, x{fc} with pauses {sum(change):+.2f}s'+(f' and {D-sum(change):.2f}s trailing' if D-sum(change)>0.05 else ''))
    segs=[]; s=0.0  # raw-time pieces between pause edits: (start, end, silence added after)
    for (a,b),c in zip(pp,change):
      mid=(a+b)/2; h=-c*r/2 if c<0 else 0
      if abs(c)>1e-3: segs.append((s,mid-h,max(c,0))); s=mid+h
    segs.append((s,None,0))
    fl=[f'[0:a]asplit={len(segs)}'+''.join(f'[i{n}]' for n in range(len(segs)))]
    for n,(a,b,ins) in enumerate(segs):
      fl.append(f'[i{n}]atrim=start={a:.4f}'+(f':end={b:.4f}' if b is not None else '')+f',asetpts=PTS-STARTPTS,atempo={r:.5f}'+(f',apad=pad_dur={ins:.4f}' if ins else '')+f'[o{n}]')
    fl.append(''.join(f'[o{n}]' for n in range(len(segs)))+f'concat=n={len(segs)}:v=0:a=1,apad=whole_dur={slots[sid]}')
    subprocess.run(['ffmpeg','-v','error','-y','-i',os.path.join(SC,v,'raw',sid+'.mp3'),'-filter_complex',';'.join(fl),'-b:a','160k',os.path.join(SC,v,sid+'.mp3')],check=True)
    def fitted(t):  # raw time -> fitted time
      out=0.0
      for a,b,ins in segs:
        if t<a: return out
        if b is None or t<=b: return out+(t-a)/r
        out+=(b-a)/r+ins
      return out
    al=json.load(open(os.path.join(SC,v,'raw',sid+'.align.json')))
    for k in ('character_start_times_seconds','character_end_times_seconds'): al[k]=[fitted(t) for t in al[k]]
    json.dump(al,open(os.path.join(SC,v,sid+'.align.json'),'w'),ensure_ascii=False)
    txt=''.join(al['characters'])
    for it in SHOTS.get(sid,[]):
      if not it.get('cue'): continue
      i=txt.find(it['cue'])
      if i<0: raise SystemExit(f'cue not found {v} {sid}: {it["cue"]}')
      at.setdefault((sid,it['cue']),{})[v]=max(0.0,al['character_start_times_seconds'][i]-LEADIN)
if ADD:
  prev['voices']=[v for v in prev['voices'] if v!=ADD]+[ADD]; prev['fit'][ADD]=fits[ADD]
  json.dump(prev,open(os.path.join(SC,'slots.json'),'w'),ensure_ascii=False,indent=1)
  off=[(abs(t[ADD]-prev['cues'][sid][ph]),sid,ph) for (sid,ph),t in at.items()]
  print(SCRIPT,ADD,'added to the existing slots; worst cue offset %.2fs (%s "%s")'%max(off)); sys.exit()
cues={}; spread=[]
for (sid,phrase),t in at.items():
  m=statistics.median(t.values()); cues.setdefault(sid,{})[phrase]=round(m,3)
  spread.append((max(abs(x-m) for x in t.values()),sid,phrase,{v:round(x-m,2) for v,x in t.items()}))
json.dump({'voices':use,'slots':slots,'cues':cues,'fit':fits},open(os.path.join(SC,'slots.json'),'w'),ensure_ascii=False,indent=1)
for dv,sid,phrase,d in sorted(spread,reverse=True)[:5]: print(f'cue {sid} "{phrase}": max off {dv:.2f}s {d}')
print(SCRIPT,'voices',', '.join(use),'| VO total',round(sum(slots.values()),1),'s')
