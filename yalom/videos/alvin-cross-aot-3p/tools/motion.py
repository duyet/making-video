# Per-shot camera moves, atmosphere overlays, ink act transitions and titles.
# exec'd by build.py: uses shots [{ref,start,box,dur,cam,ink,xf}], FX, SCRIPT_DATA, sstart, total, XF, prep. Produces html, js.
import random as _r

# CAM (per-ref camera move: scale0, scale1, x0, x1, y0, y1, ease as xPercent/yPercent) and FX (per-ref atmosphere, params in
# frame fractions) come from the script's shots.json; |x|,|y| <= (scale-1)*50 keeps the image edges hidden
# CALM (script.json 'calm', set by build.py; 1 = as authored) scales every camera move toward a still frame. Scaling the
# zoom excess and the pan by the same factor keeps the edge rule below satisfied.
for sh in shots:
  a, b, x0, x1, y0, y1, e = sh['cam']
  sh['cam'] = [1 + (a - 1) * CALM, 1 + (b - 1) * CALM, x0 * CALM, x1 * CALM, y0 * CALM, y1 * CALM, e]
for sh in shots:
  a, b, x0, x1, y0, y1, _ = sh['cam']
  for sc, x, y in ((a, x0, y0), (b, x1, y1)):
    assert abs(x) <= (sc - 1) * 50 + 1e-9 and abs(y) <= (sc - 1) * 50 + 1e-9, f"{sh['ref']} edge would show"

def cam_tw(sel, cam, s, d):
  a, b, x0, x1, y0, y1, e = cam
  return (f'tl.fromTo("{sel}",{{scale:{a},xPercent:{x0},yPercent:{y0}}},'
          f'{{scale:{b},xPercent:{x1},yPercent:{y1},duration:{d:.3f},ease:"{e}",immediateRender:false}},{s:.3f});')

html, js = [], []
uid = 0
def clip(cls, s, d, style='', track=3):
  global uid
  uid += 1; i = f'fx{uid}'
  html.append(f'      <div id="{i}" class="clip {cls}" data-start="{s:.3f}" data-duration="{d:.3f}" data-track-index="{track}"{f" style={chr(34)}{style}{chr(34)}" if style else ""}></div>')
  return '#' + i

def fade_in(sel, s, to, xf):  # xf 0: first shot or hard cut
  if not xf: js.append(f'tl.set("{sel}",{{opacity:{to}}},0);')
  else: js.append(f'tl.fromTo("{sel}",{{opacity:0}},{{opacity:{to},duration:{xf},ease:"sine.inOut"}},{s:.3f});')

for i, sh in enumerate(shots):
  fid, s, box, d, cam, ink = sh['ref'], sh['start'], sh['box'], sh['dur'], sh['cam'], sh['ink']
  src = prep(fid, box, sh['crop'])
  html.append(f'      <img id="img{i}" class="clip shot{""}" src="{src}" alt="" data-start="{s:.3f}" data-duration="{d:.3f}" data-track-index="{1 + i % 2}" />')
  js.append(cam_tw(f'#img{i}', cam, s, d))
  # fade-in: the shot's own xf (0 = hard cut), else at an ink act boundary a longer, softer dissolve (ink-mask reveal read as a
  # glitch in snapshots), else the XF crossfade; overlays fade with the shot (XF at ink boundaries)
  xf = sh['xf']; fd = xf if xf is not None else 1.6 if ink else XF if i > 0 else 0; ofd = (XF if xf is None else xf) if i > 0 else 0
  if fd:
    js.append(f'tl.fromTo("#img{i}",{{opacity:0}},{{opacity:1,duration:{fd},ease:"sine.inOut",immediateRender:false}},{s:.3f});')
  rnd = _r.Random(i * 101 + 7)
  for fx in FX.get(fid, []):
    k = fx[0]
    if k == 'fog':
      for layer, op, sp in (('fog-a', .42, 38), ('fog-b', .32, -64)):
        sel = clip(f'fog {layer}', s, d)
        fade_in(sel, s, op, ofd)
        js.append(f'tl.fromTo("{sel}",{{backgroundPosition:"0px 0px"}},{{backgroundPosition:"{sp * d:.0f}px 0px",duration:{d:.3f},ease:"none",immediateRender:false}},{s:.3f});')
    elif k == 'smoke':
      _, cx, cy = fx
      for n, off in enumerate((0, 2.3)):
        sel = clip('smoke', s, d, f'background-position:{cx * 1920 - 150:.0f}px {cy * 1080 - 760:.0f}px')
        js.append(cam_tw(sel, cam, s, d))
        cyc = 4.6; reps = max(0, int((d - off) / cyc))
        js.append(f'tl.set("{sel}",{{opacity:0}},0);')
        js.append(f'tl.fromTo("{sel}",{{opacity:0,backgroundPosition:"{cx * 1920 - 150:.0f}px {cy * 1080 - 760:.0f}px"}},'
                  f'{{keyframes:{{opacity:[0,.55,.35,0]}},backgroundPosition:"{cx * 1920 - 150 + (14 if n else -10):.0f}px {cy * 1080 - 1060:.0f}px",'
                  f'duration:{cyc},ease:"none",repeat:{reps},immediateRender:false}},{s + off:.3f});')
    elif k == 'flicker':
      _, cx, cy, rx, ry = fx
      sel = clip('flicker', s, d, f'background:radial-gradient(ellipse {rx * 1920:.0f}px {ry * 1080:.0f}px at {cx * 100:.1f}% {cy * 100:.1f}%, rgba(250,252,255,.55), rgba(250,252,255,0) 100%)')
      js.append(cam_tw(sel, cam, s, d))
      js.append(f'tl.set("{sel}",{{opacity:0}},0);')  # steady glow: the old random flicker was uncomfortable to watch
      js.append(f'tl.fromTo("{sel}",{{opacity:0}},{{opacity:.55,duration:0.6,ease:"sine.inOut",immediateRender:false}},{s:.3f});')
    elif k == 'dark':
      sel = clip('dark', s, d)
      js.append(f'tl.fromTo("{sel}",{{opacity:0,scale:1.1}},{{opacity:.9,scale:1.0,duration:{d:.3f},ease:"sine.in",immediateRender:false}},{s:.3f});')
    elif k == 'leak':
      _, cx, cy = fx
      sel = clip('leak', s, d, f'background:radial-gradient(circle 900px at {cx * 100:.0f}% {cy * 100:.0f}%, rgba(255,196,128,.42), rgba(255,170,100,.12) 45%, rgba(255,170,100,0) 75%)')
      reps = max(0, int(d / 3.2))
      js.append(f'tl.set("{sel}",{{opacity:0}},0);')
      js.append(f'tl.fromTo("{sel}",{{opacity:0}},{{keyframes:{{opacity:[0,.9,.55,.85]}},duration:{d:.3f},ease:"sine.inOut",immediateRender:false}},{s:.3f});')
      js.append(f'tl.fromTo("{sel}",{{xPercent:-3}},{{xPercent:3,duration:{d:.3f},ease:"sine.inOut",immediateRender:false}},{s:.3f});')
    elif k == 'night':
      _, cx, cy = fx
      sel = clip('night', s, d, f'background:radial-gradient(circle 260px at {cx * 100:.0f}% {cy * 100:.0f}%, rgba(255,226,170,.35), rgba(255,226,170,0) 100%), rgba(14,22,40,.14)')
      js.append(cam_tw(sel, cam, s, d)); fade_in(sel, s, 1, ofd)
    elif k == 'dust':
      sel = clip('dust', s, d)
      fade_in(sel, s, .55, ofd)
      js.append(f'tl.fromTo("{sel}",{{backgroundPosition:"0px 0px"}},{{backgroundPosition:"{14 * d:.0f}px {-22 * d:.0f}px",duration:{d:.3f},ease:"none",immediateRender:false}},{s:.3f});')
    elif k in ('warm', 'cold'):  # grade: soft-light tint over the shot
      sel = clip(k, s, d, 'position:absolute;inset:0;pointer-events:none;mix-blend-mode:soft-light;background:' + ('rgba(255,166,84,.38)' if k == 'warm' else 'rgba(84,132,200,.34)'))
      fade_in(sel, s, 1, ofd)
    elif k == 'rays':
      _, ang = fx
      sel = clip('rays', s, d, f'background:linear-gradient({ang}deg, rgba(255,242,215,0) 18%, rgba(255,242,215,.20) 28%, rgba(255,242,215,0) 38%, rgba(255,242,215,.13) 50%, rgba(255,242,215,0) 60%, rgba(255,242,215,.09) 70%, rgba(255,242,215,0) 80%)')
      js.append(f'tl.set("{sel}",{{opacity:0}},0);')
      js.append(f'tl.fromTo("{sel}",{{opacity:0}},{{keyframes:{{opacity:[0,1,.7,1]}},duration:{d:.3f},ease:"sine.inOut",immediateRender:false}},{s:.3f});')

# ---- text from the script's script.json: paper-card labels at act starts, file label, end title
scene_start = lambda sid: 0 if sid == next(iter(sstart)) else sstart[sid]
TEXT = []
for act in SCRIPT_DATA['acts']:
  st = max(1.8, scene_start(act['scene']) + 1.2)
  TEXT.append(('card act' + (' darkcard' if act.get('dark') else ''), st, 4.2, f'<span class="lbl">{act["label"]}</span>'))
fc = SCRIPT_DATA['file']
TEXT.append(('card file', scene_start(fc['scene']) + 0.8, 5.2, f'<span class="kicker">{fc["kicker"]}</span><span class="name">{fc["name"]}</span>'))
end = SCRIPT_DATA['end']
TEXT.append(('endtitle', total - 8.0, 8.0, f'<span class="t1">{end["title"]}</span>' + (f'<span class="t2">{end["subtitle"]}</span>' if end.get('subtitle') else '')))
for cls, st, d, txt in TEXT:
  uid += 1; i = f'tx{uid}'
  html.append(f'      <div id="{i}" class="clip {cls}" data-start="{st:.3f}" data-duration="{d:.3f}" data-track-index="5">{txt}</div>')
  if cls == 'endtitle':
    js.append(f'tl.fromTo("#{i}",{{opacity:0,y:12}},{{opacity:1,y:0,duration:1.4,ease:"sine.out",immediateRender:false}},{st:.3f});')
  else:  # paper label wipes on/off so the text never sits at low contrast
    js.append(f'tl.fromTo("#{i}",{{clipPath:"inset(0% 100% 0% 0%)"}},{{clipPath:"inset(0% 0% 0% 0%)",duration:0.9,ease:"power2.out",immediateRender:false}},{st:.3f});')
    js.append(f'tl.to("#{i}",{{clipPath:"inset(0% 0% 0% 100%)",duration:0.8,ease:"power2.in"}},{st + d - 0.85:.3f});')
