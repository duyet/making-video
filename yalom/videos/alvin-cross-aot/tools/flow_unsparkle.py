"""Remove the marks Flow stamps on 2K 16:9 downloads (2752x1536).

Two marks:
- small sparkle (2K download), fixed at ~x2640,y1424, ~45px;
- large sparkle (baked into the generation), bottom-right, 110-190px, centre seen between x2556-2597, y1340-1426.
  Its size and position vary, so it is not reverse-blended: by default the frame is cropped to x0..2440, y82..1454
  (16:9, excludes both marks) and resized back to 2752x1536.

--keep-frame: no crop; only remove the small sparkle by reversing its alpha blend with white (96x96 alpha map in
  flow_sparkle_alpha.json, measured on a flat-background frame), then median-filter a thin band along the star's edge,
  where the map is least exact. The mark's strength varies a little between frames (it over-corrects into a dark
  diamond on near-black backgrounds), so the map is scaled per frame by the factor that makes the corrected star
  interior match the brightness of the ring around it. Use only when the large mark is absent (check the corner).

--check <file> [...]: exit 1 if a sparkle is still detectable (normalised cross-correlation at the known spots;
  small >= 0.5, large >= 0.5); prints the scores. It does not prove a frame is clean: always look at the corner too.

A 1K original (1376x768, used while Flow's 2K upscaling fails) gets the same crop at half scale and an INTERIM Lanczos
upscale to 2752x1536; replace it with the 2K download when that works.

usage: flow_unsparkle.py [--keep-frame] <in> <out> [<in> <out> ...]
       flow_unsparkle.py --check <file> [<file> ...]"""
import sys,os,json
from PIL import Image,ImageFilter
X0,Y0=2592,1376
CROP=(0,82,2440,1454)
LARGE=[(2556,1340,2.0),(2597,1426,1.2)]  # observed large-mark centres and scales (x the 96px map)
A=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'flow_sparkle_alpha.json'))); N=len(A)
on=lambda r,c: 0<=r<N and 0<=c<N and A[r][c]>0
near=lambda r,c,d,want: any(on(r+i,c+j)==want for i in range(-d,d+1) for j in range(-d,d+1))
EDGE=[(r,c) for r in range(N) for c in range(N) if near(r,c,2,True) and near(r,c,2,False)]
INNER=[(r,c) for r in range(N) for c in range(N) if A[r][c]>0.15]
RING=[(r,c) for r in range(N) for c in range(N) if not on(r,c) and near(r,c,6,True) and not near(r,c,2,True)]
MASK=Image.new('L',(N,N)); MASK.putdata([255 if near(r,c,2,True) else 0 for r in range(N) for c in range(N)])
MASK=MASK.filter(ImageFilter.GaussianBlur(2))
lum=lambda p: (p[0]*299+p[1]*587+p[2]*114)/1000
unblend=lambda p,a: tuple(max(0,min(255,round((p[k]-a*255)/(1-a)))) for k in range(3))

ring_lum=lambda px: sorted(lum(px[X0+c,Y0+r]) for r,c in RING)[len(RING)//2]

def strength(px):
  ring=ring_lum(px)
  err=lambda f: abs(sum(lum(unblend(px[X0+c,Y0+r],A[r][c]*f)) for r,c in INNER)/len(INNER)-ring)
  return min((f/100 for f in range(50,121,5)),key=err)

def remove_small(im):
  px=im.load(); f=strength(px); dark=ring_lum(px)<50
  for r,row in enumerate(A):
    for c,a in enumerate(row):
      if a: px[X0+c,Y0+r]=unblend(px[X0+c,Y0+r],a*f)
  med=im.crop((X0,Y0,X0+N,Y0+N)).filter(ImageFilter.MedianFilter(5)).load()
  for r,c in EDGE: px[X0+c,Y0+r]=med[c,r]
  # unblending amplifies JPEG noise inside the star, which shows as a speckled diamond on near-black backgrounds;
  # on lighter, grainy backgrounds a blur would read as a smooth diamond instead, so only smooth the dark case
  if dark: im.paste(im.crop((X0,Y0,X0+N,Y0+N)).filter(ImageFilter.GaussianBlur(2)),(X0,Y0),MASK)
  return f'strength {f:.2f}{" +smooth" if dark else ""}'

def template(scale,red):
  t=Image.new('F',(N,N)); t.putdata([v for row in A for v in row])
  n=round(N*scale/red); v=list(t.resize((n,n),Image.BILINEAR).get_flattened_data()); m=sum(v)/len(v)
  return n,[x-m for x in v]

def ncc(L,red,x0,y0,scale,rad):
  """best normalised cross-correlation of the alpha map (scaled) within +-rad*red px of (x0,y0), on L reduced by red"""
  n,K=template(scale,red); kk=sum(k*k for k in K)**.5; W,H=L.size; px=L.load(); best=-1.0
  for dy in range(-rad,rad+1):
    for dx in range(-rad,rad+1):
      X,Y=round(x0/red)+dx,round(y0/red)+dy
      if X<0 or Y<0 or X+n>W or Y+n>H: continue
      v=[px[X+c,Y+r] for r in range(n) for c in range(n)]; m=sum(v)/len(v)
      den=sum((a-m)**2 for a in v)**.5*kk
      if den: best=max(best,sum((a-m)*k for a,k in zip(v,K))/den)
  return best

def check(path):
  L=Image.open(path).convert('L'); assert L.size==(2752,1536),(path,L.size)
  small=ncc(L.reduce(2),2,X0,Y0,1,4)
  large=max(ncc(L.reduce(4),4,cx-N*s/2,cy-N*s/2,s,6) for cx,cy,s in LARGE)
  return small,large,small>=0.5 or large>=0.5

if sys.argv[1:2]==['--check']:
  bad=0
  for p in sys.argv[2:]:
    s,l,hit=check(p); bad|=hit
    print(f'{os.path.basename(p)}: small {s:.2f} large {l:.2f} {"MARK" if hit else "ok"}')
  sys.exit(1 if bad else 0)

keep='--keep-frame' in sys.argv
args=[a for a in sys.argv[1:] if a!='--keep-frame']
for src,dst in zip(args[0::2],args[1::2]):
  im=Image.open(src).convert('RGB')
  if im.size==(1376,768):  # 1K original while 2K upscaling is down: same crop at half scale, interim Lanczos upscale
    assert not keep,'--keep-frame needs a 2K frame'
    im=im.crop(tuple(v//2 for v in CROP)).resize((2752,1536),Image.LANCZOS); note='1K cropped, interim upscale'
  else:
    assert im.size==(2752,1536),(src,im.size)
    if keep: note=remove_small(im)
    else: im=im.crop(CROP).resize((2752,1536),Image.LANCZOS); note='cropped'
  im.save(dst)
  print(f'{os.path.basename(dst)}: {note}')
