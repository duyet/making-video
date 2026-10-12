"""Mix one voice's fitted VO + the music bed (looped with a crossfade to cover the timeline, ducked under the VO) + SFX per mix.json, and mux it onto the silent picture.
usage: mux.py <script> <voice> <picture.mp4> <out.mp4>"""
import json,math,os,sys,subprocess
HERE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT,VOICE,PIC,OUT=sys.argv[1:5]; SC=os.path.join(HERE,'narration','scripts',SCRIPT)
XM=4.0  # crossfade at the music loop seam
DUCK='sidechaincompress=threshold=0.012:ratio=5:knee=4:attack=20:release=450'  # music under the VO; with LEVEL, matches the old carve's bed within ~2 dB
LEVEL='acompressor=threshold=0.05:ratio=4:attack=200:release=1000'  # evens out the bed's loud passages, like the carve's level match
PEAK='alimiter=limit=-1dB:level=disabled:attack=1:release=50'  # final peak ceiling, -1 dB; leaves the mix level alone
F='aformat=sample_rates=48000:channel_layouts=stereo'
VOUP='aresample=48000,pan=stereo|c0=0.827*c0|c1=0.827*c0'  # mono VO to both channels at the level the HyperFrames mix gave it
mix=json.load(open(os.path.join(SC,'mix.json'))); use=json.load(open(os.path.join(SC,'slots.json')))['voices']
if VOICE not in use: raise SystemExit(f'{VOICE} is not in the {SCRIPT} timeline ({", ".join(use)}): tts.py it, then rebuild.sh {SCRIPT} visuals')
if os.path.getmtime(PIC)<os.path.getmtime(os.path.join(SC,'mix.json')): raise SystemExit(f'{PIC} is older than the last build: rebuild.sh {SCRIPT} visuals')
probe=lambda f: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
inp=['-i',PIC]; fl=[]; bus=[]
def add(p): inp.extend(['-i',os.path.join(HERE,p)]); return len(inp)//2-1
def fades(c): return f"volume={c['volume']},afade=t=in:d={c['fade_in']},afade=t=out:st={c['dur']-c['fade_out']:.3f}:d={c['fade_out']}"
vo=[]
for sid,st in mix['vo'].items():
  k=add(f'narration/scripts/{SCRIPT}/{VOICE}/{sid}.mp3'); fl.append(f'[{k}:a]{VOUP},adelay={round(st*1000)}:all=1[v{k}]'); vo.append(f'[v{k}]')
fl.append(f'{"".join(vo)}amix=inputs={len(vo)}:normalize=0,apad=whole_dur={mix["total"]}[vo]'); bus.append('[vo]')  # full length, so the ducking key outlasts the last line
if 'music' in mix:
  m=mix['music']; bd=probe(os.path.join(HERE,m['src'])); ks=[add(m['src']) for _ in range(1+math.ceil(max(0,m['dur']-bd)/(m['loop_end']-XM)))]
  fl+= [f'[{k}:a]{F}'+(f',atrim=0:{m["loop_end"]}' if k!=ks[-1] else '')+f'[m{k}]' for k in ks]; prev=f'[m{ks[0]}]'  # loop before the bed's own ending
  for k in ks[1:]: fl.append(f'{prev}[m{k}]acrossfade=d={XM}[x{k}]'); prev=f'[x{k}]'
  fl.append(f'{prev}atrim=0:{m["dur"]},{LEVEL},{fades(m)}[mb]'); fl+= ['[vo]asplit[vom][sc]',f'[mb][sc]{DUCK}[md]']; bus[0]='[vom]'; bus.append('[md]')
for c in mix['sfx']:
  k=add(c['src']); fl.append(f'[{k}:a]{F},atrim=0:{c["dur"]},{fades(c)},adelay={round(c["start"]*1000)}:all=1[s{k}]'); bus.append(f'[s{k}]')
fl.append(f'{"".join(bus)}amix=inputs={len(bus)}:normalize=0:duration=longest,apad,atrim=0:{mix["total"]},{PEAK}[out]')
subprocess.run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',';'.join(fl),'-map','0:v','-map','[out]','-c:v','copy','-c:a','aac','-b:a','192k','-t',str(mix['total']),OUT],check=True)
print(OUT,round(probe(OUT),2),'s')
