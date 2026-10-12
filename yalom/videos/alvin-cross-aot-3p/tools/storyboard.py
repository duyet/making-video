"""Storyboard review page for molly-v2: every line with its 3p and 1p VO and the shots that cut on it (thumbnail, cue word, rating).
usage: storyboard.py <out.html> [--with-1p]   (3p only by default)"""
import base64,io,json,os,sys
from PIL import Image
V=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ONLY3P='--with-1p' not in sys.argv
P3,P1=os.path.join(V,'alvin-cross-aot-3p'),os.path.join(V,'alvin-cross-aot')
SC=lambda p:os.path.join(p,'narration','scripts','molly-v2')
L3={l['id']:l['text'] for l in json.load(open(os.path.join(SC(P3),'lines.json')))}
L1={l['id']:l['text'] for l in json.load(open(os.path.join(SC(P1),'lines.json')))}
S3=json.load(open(os.path.join(SC(P3),'shots.json')))['shots']; S1=json.load(open(os.path.join(SC(P1),'shots.json')))['shots']
ACTS={a['scene']:a['label'] for a in json.load(open(os.path.join(SC(P3),'script.json')))['acts']}
R=os.path.join(P1,'script-src','molly-v2','ratings')
score={}
for f in ('library.json','winners.json'):
  for e in json.load(open(os.path.join(R,f))): score[e['shot']]=e['total']
NEW={r for r in score if r[0] in 'MR'}
SBF=os.path.join(R,'storyboard.json'); SB=json.load(open(SBF)) if os.path.exists(SBF) else {'lines':{}}
PASS=9.0
thumbs={}
def thumb(ref):
  if not os.path.exists(os.path.join(P1,'assets','redraw',ref+'.png')): return None
  if ref not in thumbs:
    im=Image.open(os.path.join(P1,'assets','redraw',ref+'.png')).convert('RGB'); im.thumbnail((560,316))
    b=io.BytesIO(); im.save(b,'JPEG',quality=72); thumbs[ref]='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
  return thumbs[ref]
esc=lambda s:s.replace('&','&amp;').replace('<','&lt;')
import re
# on-screen timing from the built 3p composition, in timeline order (one <img class="clip shot"> per cut)
HTML=open(os.path.join(P3,'index.html')).read()
TIMES=[(float(a),float(b)) for a,b in re.findall(r'class="clip shot"[^>]*data-start="([\d.]+)" data-duration="([\d.]+)"',HTML)]
TOTAL=max((a+b for a,b in TIMES),default=0)
SHORT=2.5  # seconds: a cut shorter than this reads as hurried
k=[0]
MF=os.path.join(P1,'script-src','molly-v2','MOTION.json'); MOTION=json.load(open(MF)) if os.path.exists(MF) else {}
mmss=lambda t:f'{int(t//60)}:{t%60:04.1f}'
rows=[]
for lid,shots in S3.items():
  if lid in ACTS: rows.append(f'<h2 class="act">{esc(ACTS[lid])}</h2>')
  same=[i['ref'] for i in shots]==[i['ref'] for i in S1[lid]]
  def cell(it,it1=None):  # a shot not drawn yet shows its stand-in (fallback) or a placeholder
    r=it['ref']; sc=score.get(r); tag='new' if r in NEW or r[0]=='S' else 'lib'; low=' low' if sc is not None and sc<PASS else ''
    cue=f'<span class="cue">“{esc(it["cue"])}”</span>' if it.get('cue') else '<span class="cue start">line start</span>'
    if it1 and it1.get('cue') and it1['cue']!=it.get('cue'): cue+=f'<span class="cue p1">1p “{esc(it1["cue"])}”</span>'
    xf=it.get('xf')
    if xf is not None: cue+=f'<span class="cue xf">{"hard cut" if xf in ("cut",0) else "dissolve" if xf=="dissolve" else f"{xf} s crossfade"}</span>'
    src=thumb(r); fb=it.get('fallback'); src_fb=None if src or not fb else thumb(fb)
    img=f'<img src="{src}" alt="{r}" loading="lazy">' if src else (f'<img class="standin" src="{src_fb}" alt="{fb}" loading="lazy">' if src_fb else '<div class="todo">not drawn yet</div>')
    note='' if src else f'<span class="cue standin">not drawn · {"stand-in " + fb if src_fb else "previous shot holds"}</span>'
    if it1 is None and k[0]<len(TIMES):
      t0,d=TIMES[k[0]]; k[0]+=1
      note+=f'<span class="cue tm{" low" if d<SHORT else ""}">{mmss(t0)} · {d:.1f} s</span>'
    if r in MOTION: note+=f'<span class="cue mv">{MOTION[r]["move"].replace("_"," ")}{" · hero" if MOTION[r].get("hero") else ""}</span>'
    return (f'<figure>{img}<figcaption><b class="{tag}">{r}</b>'
            f'<span class="sc{low}">{sc if sc is not None else "—"}</span>{cue}{note}</figcaption></figure>')
  cells=[cell(it,it1) for it,it1 in zip(shots,S1[lid])] if same and not ONLY3P else [cell(it) for it in shots]
  p1=f'<div class="p1row"><span class="p1lbl">1p</span><div class="shots">{"".join(cell(it) for it in S1[lid])}</div></div>' if not same and not ONLY3P else ''
  ls=SB['lines'].get(lid,{}); lt=ls.get('total')
  badge=f'<span class="ls{"" if lt is not None and lt>=PASS else " low"}">{lt if lt is not None else "not scored"}</span>'
  gaps=''.join(f'<li>{esc(g)}</li>' for g in ls.get('gaps',[]))
  rows.append(f'<section class="line"><div class="vo"><span class="id">{lid}</span>{badge}<p class="t3">{esc(L3[lid])}</p>'
              +(f'<p class="t1"><span>1p</span> {esc(L1[lid])}</p>' if not ONLY3P else '')+f'{f'<ul class="gaps">{gaps}</ul>' if gaps else ''}</div><div><div class="shots">{"".join(cells)}</div>{p1}</div></section>')
n=sum(len(v) for v in S3.values())  # 3p cuts
html=f'''<title>Thank You, Molly storyboard</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;700&family=Be+Vietnam+Pro:wght@400;500&display=swap">
<style>
/* layout: one row per VO line, text column then a strip of shot frames; act headers as slate bands */
:root{{--bg:#eceae3;--panel:#f7f6f1;--fg:#22251f;--muted:#646a5c;--line:#cfccc0;--accent:#7a5a1e;--new:#2f6b4f;--warn:#a8432c;
 --disp:"Barlow Condensed","Arial Narrow",sans-serif;--body:"Be Vietnam Pro",system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#191b17;--panel:#23261f;--fg:#e7e5dc;--muted:#a3a894;--line:#383c32;--accent:#d6ae5c;--new:#7cc39b;--warn:#e07a5f;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#191b17;--panel:#23261f;--fg:#e7e5dc;--muted:#a3a894;--line:#383c32;--accent:#d6ae5c;--new:#7cc39b;--warn:#e07a5f;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:15px/1.55 var(--body);padding-inline:16px;padding-block:24px 48px}}
main{{max-width:1240px;margin:0 auto;display:flex;flex-direction:column;gap:14px}}
h1{{font:700 2.4rem/1 var(--disp);letter-spacing:.02em;text-transform:uppercase;margin:0;text-wrap:balance}}
.lede{{color:var(--muted);margin:0;max-width:70ch}}
.key{{display:flex;flex-wrap:wrap;gap:16px;font:500 .85rem var(--disp);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.key b.new,.key b.lib{{font-weight:700}}
h2.act{{font:700 1.3rem var(--disp);letter-spacing:.08em;text-transform:uppercase;margin:18px 0 0;padding-bottom:6px;border-bottom:2px solid var(--accent);color:var(--accent)}}
.line{{display:grid;grid-template-columns:minmax(0,320px) minmax(0,1fr);gap:16px;background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:14px}}
.vo{{min-width:0}} .id{{font:700 1rem var(--disp);letter-spacing:.08em;color:var(--accent)}}
.t3{{margin:4px 0 8px}} .t1{{margin:0;color:var(--muted);font-size:.9rem}} .t1 span{{font:700 .75rem var(--disp);letter-spacing:.08em}}
.shots{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;min-width:0}}
figure{{margin:0;display:flex;flex-direction:column;gap:4px}}
img{{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:3px;display:block}}
figcaption{{display:flex;flex-wrap:wrap;gap:4px 8px;align-items:baseline;font-size:.8rem}}
figcaption b{{font:700 .95rem var(--disp);letter-spacing:.05em}} b.new{{color:var(--new)}} b.lib{{color:var(--fg)}}
.sc{{font:500 .85rem var(--disp);font-variant-numeric:tabular-nums;color:var(--muted)}}
.ls{{margin-left:8px;font:700 .85rem var(--disp);padding:1px 7px;border-radius:9px;background:var(--new);color:var(--panel)}} .ls.low,.sc.low{{background:var(--warn);color:var(--panel)}} .sc.low{{padding:0 5px;border-radius:7px}}
.gaps{{margin:8px 0 0;padding-left:18px;font-size:.82rem;color:var(--muted)}}
.cue{{flex-basis:100%;color:var(--fg)}} .cue.start{{color:var(--muted)}} .cue.p1{{color:var(--muted)}} .cue.xf{{color:var(--accent)}} .cue.standin{{color:var(--warn)}} .cue.tm{{color:var(--muted);font-variant-numeric:tabular-nums}} .cue.tm.low{{color:var(--warn)}} .cue.mv{{color:var(--accent)}}
img.standin{{opacity:.45;filter:grayscale(1)}} .todo{{aspect-ratio:16/9;border:1px dashed var(--line);border-radius:3px;display:grid;place-items:center;color:var(--muted);font-size:.8rem}}
.p1row{{margin-top:10px;padding-top:10px;border-top:1px dashed var(--line);display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px;align-items:start}} .p1lbl{{font:700 .85rem var(--disp);letter-spacing:.08em;color:var(--muted)}}
@media (max-width:760px){{.line{{grid-template-columns:minmax(0,1fr)}}}}
</style>
<main>
<h1>Thank You, Molly · v2 storyboard{' · 3p' if ONLY3P else ''}</h1>
<p class="lede">{len(S3)} VO lines, {n} cuts, {len(thumbs)} images. {'Each frame starts on its cue word in the 3p (third-person) text.' if ONLY3P else 'Each frame starts on its cue word in the 3p text (the 1p cue is shown when it differs).'} Image scores are the validator's rubric totals out of 10 and line badges are the storyboard score against the sheet; both pass at 9.0. Storyboard overall: {SB.get("overall","not scored yet")}. Runtime {mmss(TOTAL)}; each frame shows its start time and seconds on screen (under {SHORT} s is flagged as hurried).</p>
<div class="key"><span><b class="new">M/R</b> new Flow image</span><span><b class="lib">F/N/X/B</b> existing library</span></div>
{"".join(rows)}
</main>'''
open(sys.argv[1],'w').write(html)
print(sys.argv[1],round(len(html)/1e6,2),'MB')
