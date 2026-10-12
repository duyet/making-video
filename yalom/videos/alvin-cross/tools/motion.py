# Per-shot camera moves, atmosphere overlays, ink act transitions and titles.
# exec'd by build.py: uses shots [[fid,start,box,dur]], SHOTS, sstart, total, XF, prep. Produces html, js.
import random as _r

# fid: (scale0, scale1, x0, x1, y0, y1, ease)  — xPercent/yPercent; |x|,|y| <= (scale-1)*50 keeps edges hidden
P, N = 'sine.inOut', 'none'
CAM = {
 'F24': (1.15, 1.15, -6, 6, 0, 0, N),     'F31': (1.05, 1.18, 0, -4, 0, 0, P),
 'F33': (1.15, 1.15, 0, 0, 6, -6, P),      'F23': (1.12, 1.12, 4, -4, 0, 0, P),
 'F13': (1.04, 1.14, 0, 0, 0, 0, P),       'F20': (1.05, 1.20, 0, 5, 0, 3, P),
 'F15': (1.05, 1.16, 0, 0, 0, 0, P),       'F11': (1.15, 1.15, 6, -6, 0, 0, P),
 'F01': (1.05, 1.25, 0, -2, 0, -4, P),     'F10': (1.18, 1.18, 0, 0, -7, 7, P),
 'F05': (1.20, 1.05, 0, 0, 0, 0, P),       'F21': (1.05, 1.18, 0, -5, 0, 0, P),
 'F34': (1.05, 1.30, 0, -5, 0, 0, P),      'F08': (1.05, 1.15, 0, 0, 0, 0, P),
 'F19': (1.05, 1.20, 0, 0, 0, 4, P),       'F06': (1.14, 1.14, 5, -5, 0, 0, P),
 'F30': (1.12, 1.12, -4, 4, 0, 0, N),      'F27': (1.05, 1.20, 0, 0, 0, 0, P),
 'F28': (1.00, 1.35, 0, 0, 0, 0, 'power2.in'), 'F29': (1.40, 1.10, 0, 0, 0, 0, P),
 'F32': (1.12, 1.12, -4, 4, 0, 0, P),      'F14': (1.05, 1.18, 0, 0, 0, 0, P),
 'F04': (1.20, 1.05, 0, 0, 0, 0, P),       'F07': (1.05, 1.22, 0, -3, 0, 0, P),
 'F26': (1.05, 1.20, 0, 0, 0, 0, P),
 'F35': (1.10, 1.10, -3, 3, 0, 0, N),      'F36': (1.08, 1.18, 0, 0, 0, 1, P),       'F17': (1.05, 1.15, 0, -3, 0, 0, P),
 'F12': (1.14, 1.14, 4, -5, 0, 0, P),      'F25': (1.06, 1.16, 0, 0, 0, -3, P),
 'F18': (1.04, 1.12, 0, 0, 0, 0, P),       'F16': (1.05, 1.14, 0, -3, 0, 0, P),
 'F03': (1.05, 1.15, 0, 0, 0, 0, P),       'F02': (1.12, 1.12, 4, -3, 0, 0, P),
 'F09': (1.04, 1.12, 0, 0, 0, 0, P),       'F22': (1.00, 1.12, 0, 0, 0, 0, P),
}
for f, (a, b, x0, x1, y0, y1, _) in CAM.items():
  for sc, x, y in ((a, x0, y0), (b, x1, y1)):
    assert abs(x) <= (sc - 1) * 50 + 1e-9 and abs(y) <= (sc - 1) * 50 + 1e-9, f'{f} edge would show'

# atmosphere per shot; params in frame fractions
FX = {
 'F24': [('fog',)], 'F31': [('fog',)], 'F33': [('fog',)], 'F23': [('fog',)], 'F13': [('fog',)],
 'F09': [('fog',)], 'F22': [('fog',)],
 'F05': [('flicker', .17, .30, .14, .20), ('smoke', .70, .80)],
 'F08': [('smoke', .57, .30)], 'F19': [('smoke', .60, .70)],
 'F11': [('flicker', .30, .45, .16, .26)], 'F34': [('flicker', .50, .48, .40, .44)],
 'F27': [('dark',)], 'F28': [('dark',)], 'F29': [('dark',)],
 'F04': [('leak', .15, .2)], 'F07': [('leak', .85, .25)], 'F35': [('leak', .8, .2)], 'F36': [('leak', .7, .3)], 'F26': [('leak', .2, .15), ('dust',)],
 'F30': [('night', .62, .33)],
 'F12': [('dust',), ('rays', 245)], 'F25': [('dust',), ('rays', 235)], 'F16': [('dust',), ('rays', 115)],
 'F02': [('dust',), ('rays', 120)],
}
INK = {SHOTS['s06'][0][0], SHOTS['s12'][0][0], SHOTS['s18'][0][0]}

def cam_tw(sel, fid, s, d):
  a, b, x0, x1, y0, y1, e = CAM[fid]
  return (f'tl.fromTo("{sel}",{{scale:{a},xPercent:{x0},yPercent:{y0}}},'
          f'{{scale:{b},xPercent:{x1},yPercent:{y1},duration:{d:.3f},ease:"{e}",immediateRender:false}},{s:.3f});')

html, js = [], []
uid = 0
def clip(cls, s, d, style='', track=3):
  global uid
  uid += 1; i = f'fx{uid}'
  html.append(f'      <div id="{i}" class="clip {cls}" data-start="{s:.3f}" data-duration="{d:.3f}" data-track-index="{track}"{f" style={chr(34)}{style}{chr(34)}" if style else ""}></div>')
  return '#' + i

def fade_in(sel, s, to, first):
  if first: js.append(f'tl.set("{sel}",{{opacity:{to}}},0);')
  else: js.append(f'tl.fromTo("{sel}",{{opacity:0}},{{opacity:{to},duration:{XF},ease:"sine.inOut"}},{s:.3f});')

for i, (fid, s, box, d) in enumerate(shots):
  src = prep(fid, box)
  ink = fid in INK
  html.append(f'      <img id="img{i}" class="clip shot{""}" src="{src}" alt="" data-start="{s:.3f}" data-duration="{d:.3f}" data-track-index="{1 + i % 2}" />')
  js.append(cam_tw(f'#img{i}', fid, s, d))
  if ink:  # act boundary: longer, softer dissolve (ink-mask reveal read as a glitch in snapshots)
    js.append(f'tl.fromTo("#img{i}",{{opacity:0}},{{opacity:1,duration:1.6,ease:"sine.inOut",immediateRender:false}},{s:.3f});')
  elif i > 0:
    js.append(f'tl.fromTo("#img{i}",{{opacity:0}},{{opacity:1,duration:{XF},ease:"sine.inOut",immediateRender:false}},{s:.3f});')
  rnd = _r.Random(i * 101 + 7)
  for fx in FX.get(fid, []):
    k = fx[0]
    if k == 'fog':
      for layer, op, sp in (('fog-a', .42, 38), ('fog-b', .32, -64)):
        sel = clip(f'fog {layer}', s, d)
        fade_in(sel, s, op, i == 0)
        js.append(f'tl.fromTo("{sel}",{{backgroundPosition:"0px 0px"}},{{backgroundPosition:"{sp * d:.0f}px 0px",duration:{d:.3f},ease:"none",immediateRender:false}},{s:.3f});')
    elif k == 'smoke':
      _, cx, cy = fx
      for n, off in enumerate((0, 2.3)):
        sel = clip('smoke', s, d, f'background-position:{cx * 1920 - 150:.0f}px {cy * 1080 - 760:.0f}px')
        js.append(cam_tw(sel, fid, s, d))
        cyc = 4.6; reps = max(0, int((d - off) / cyc))
        js.append(f'tl.set("{sel}",{{opacity:0}},0);')
        js.append(f'tl.fromTo("{sel}",{{opacity:0,backgroundPosition:"{cx * 1920 - 150:.0f}px {cy * 1080 - 760:.0f}px"}},'
                  f'{{keyframes:{{opacity:[0,.55,.35,0]}},backgroundPosition:"{cx * 1920 - 150 + (14 if n else -10):.0f}px {cy * 1080 - 1060:.0f}px",'
                  f'duration:{cyc},ease:"none",repeat:{reps},immediateRender:false}},{s + off:.3f});')
    elif k == 'flicker':
      _, cx, cy, rx, ry = fx
      sel = clip('flicker', s, d, f'background:radial-gradient(ellipse {rx * 1920:.0f}px {ry * 1080:.0f}px at {cx * 100:.1f}% {cy * 100:.1f}%, rgba(250,252,255,.55), rgba(250,252,255,0) 100%)')
      js.append(cam_tw(sel, fid, s, d))
      t = 0.0; js.append(f'tl.set("{sel}",{{opacity:0}},0);')
      while t < d:
        js.append(f'tl.set("{sel}",{{opacity:{rnd.choice([.55,.6,.65,.6,.3,.7]):.2f}}},{s + t:.3f});')
        t += rnd.choice([0.08, 0.12, 0.5, 0.9, 1.4, 0.2])
    elif k == 'dark':
      sel = clip('dark', s, d)
      js.append(f'tl.fromTo("{sel}",{{opacity:0,scale:1.5}},{{opacity:.9,scale:1.0,duration:{d:.3f},ease:"sine.in",immediateRender:false}},{s:.3f});')
    elif k == 'leak':
      _, cx, cy = fx
      sel = clip('leak', s, d, f'background:radial-gradient(circle 900px at {cx * 100:.0f}% {cy * 100:.0f}%, rgba(255,196,128,.42), rgba(255,170,100,.12) 45%, rgba(255,170,100,0) 75%)')
      reps = max(0, int(d / 3.2))
      js.append(f'tl.set("{sel}",{{opacity:0}},0);')
      js.append(f'tl.fromTo("{sel}",{{opacity:0}},{{keyframes:{{opacity:[0,.9,.55,.85]}},duration:{d:.3f},ease:"sine.inOut",immediateRender:false}},{s:.3f});')
      js.append(f'tl.fromTo("{sel}",{{xPercent:-3}},{{xPercent:3,duration:{d:.3f},ease:"sine.inOut",immediateRender:false}},{s:.3f});')
    elif k == 'night':
      _, cx, cy = fx
      sel = clip('night', s, d, f'background:radial-gradient(circle 260px at {cx * 100:.0f}% {cy * 100:.0f}%, rgba(255,226,170,.35), rgba(255,226,170,0) 100%), rgba(14,22,40,.30)')
      js.append(cam_tw(sel, fid, s, d)); fade_in(sel, s, 1, i == 0)
    elif k == 'dust':
      sel = clip('dust', s, d)
      fade_in(sel, s, .55, i == 0)
      js.append(f'tl.fromTo("{sel}",{{backgroundPosition:"0px 0px"}},{{backgroundPosition:"{14 * d:.0f}px {-22 * d:.0f}px",duration:{d:.3f},ease:"none",immediateRender:false}},{s:.3f});')
    elif k == 'rays':
      _, ang = fx
      sel = clip('rays', s, d, f'background:linear-gradient({ang}deg, rgba(255,242,215,0) 18%, rgba(255,242,215,.20) 28%, rgba(255,242,215,0) 38%, rgba(255,242,215,.13) 50%, rgba(255,242,215,0) 60%, rgba(255,242,215,.09) 70%, rgba(255,242,215,0) 80%)')
      js.append(f'tl.set("{sel}",{{opacity:0}},0);')
      js.append(f'tl.fromTo("{sel}",{{opacity:0}},{{keyframes:{{opacity:[0,1,.7,1]}},duration:{d:.3f},ease:"sine.inOut",immediateRender:false}},{s:.3f});')

# ---- text: paper-card labels at act starts, file label, end title
def shot_start(sid, j=0):
  fid = SHOTS[sid][j][0]
  return next(s for f, s, b, d in shots if f == fid)
TEXT = []
for sid, label in (('s01', 'I · Tang lễ của Molly'), ('s06', 'II · Vết thương mang tên Jason'),
                   ('s12', 'III · Phòng trị liệu'), ('s18', 'IV · Căn nhà đóng băng')):
  st = max(1.8, shot_start(sid) + 1.2)
  TEXT.append(('card act' + (' darkcard' if sid == 's06' else ''), st, 4.2, f'<span class="lbl">{label}</span>'))
f11 = shot_start('s05')
TEXT.append(('card file', f11 + 0.8, 5.2, '<span class="kicker">Hồ sơ bệnh án · 1982</span><span class="name">Bác sĩ Alvin Cross</span>'))
TEXT.append(('endtitle', total - 8.0, 8.0, '<span class="t1">Món quà của Molly</span><span class="t2">Theo lời kể của bác sĩ Irvin D. Yalom</span>'))
for cls, st, d, txt in TEXT:
  uid += 1; i = f'tx{uid}'
  html.append(f'      <div id="{i}" class="clip {cls}" data-start="{st:.3f}" data-duration="{d:.3f}" data-track-index="5">{txt}</div>')
  if cls == 'endtitle':
    js.append(f'tl.fromTo("#{i}",{{opacity:0,y:12}},{{opacity:1,y:0,duration:1.4,ease:"sine.out",immediateRender:false}},{st:.3f});')
  else:  # paper label wipes on/off so the text never sits at low contrast
    js.append(f'tl.fromTo("#{i}",{{clipPath:"inset(0% 100% 0% 0%)"}},{{clipPath:"inset(0% 0% 0% 0%)",duration:0.9,ease:"power2.out",immediateRender:false}},{st:.3f});')
    js.append(f'tl.to("#{i}",{{clipPath:"inset(0% 0% 0% 100%)",duration:0.8,ease:"power2.in"}},{st + d - 0.85:.3f});')
