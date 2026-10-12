"""Generate seeded, static overlay textures used by the composition (fog, dust, smoke, ink mask, grain)."""
import os,random,math
from PIL import Image,ImageDraw,ImageFilter,ImageChops
OUT=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'assets','fx')
rnd=random.Random(11)
def fog(name,w,h,blobs,alpha):
  im=Image.new('L',(w,h),0); d=ImageDraw.Draw(im)
  for _ in range(blobs):
    x,y=rnd.uniform(0,w),rnd.uniform(h*0.25,h*1.0); rx,ry=rnd.uniform(180,520),rnd.uniform(60,160)
    for dx in (0,-w,w):  # wrap horizontally so the strip tiles
      d.ellipse([x+dx-rx,y-ry,x+dx+rx,y+ry],fill=int(rnd.uniform(60,140)))
  im=im.filter(ImageFilter.GaussianBlur(70))
  rgba=Image.new('RGBA',(w,h),(236,232,224,0)); rgba.putalpha(im.point(lambda v:int(v*alpha))); rgba.save(os.path.join(OUT,name))
fog('fog-a.png',3840,1080,60,0.85); fog('fog-b.png',3840,1080,40,0.6)
# dust motes
im=Image.new('RGBA',(1920,1080),(0,0,0,0)); d=ImageDraw.Draw(im)
for _ in range(220):
  x,y,r=rnd.uniform(0,1920),rnd.uniform(0,1080),rnd.choice([1,1,1.5,2,2.5,3.5])
  d.ellipse([x-r,y-r,x+r,y+r],fill=(255,246,225,int(rnd.uniform(90,220))))
im.filter(ImageFilter.GaussianBlur(0.8)).save(os.path.join(OUT,'dust.png'))
# smoke wisps (tall strip, rises)
w,h=600,1600; im=Image.new('L',(w,h),0); d=ImageDraw.Draw(im)
for k in range(5):
  ph=rnd.uniform(0,6.28); amp=rnd.uniform(25,70); x0=w/2+rnd.uniform(-40,40); pts=[]
  for y in range(h,0,-8):
    t=(h-y)/h; pts.append((x0+math.sin(y/90+ph)*amp*(0.3+t)+math.sin(y/37+ph*2)*12*t,y))
  d.line(pts,fill=int(rnd.uniform(90,160)),width=int(rnd.uniform(10,22)))
im=im.filter(ImageFilter.GaussianBlur(14)); grad=Image.linear_gradient('L').resize((w,h))  # fade toward top
im=ImageChops.multiply(im,grad)
sm=Image.new('RGBA',(w,h),(225,222,215,0)); sm.putalpha(im); sm.save(os.path.join(OUT,'smoke.png'))
# ink blot mask (alpha) for act transitions
w=h=1200; im=Image.new('L',(w,h),0); d=ImageDraw.Draw(im)
d.ellipse([w*.3,h*.3,w*.7,h*.7],fill=255)
for _ in range(90):
  a=rnd.uniform(0,6.28); r=rnd.uniform(0.12,0.36)*w; s=rnd.uniform(18,90)
  x,y=w/2+math.cos(a)*r,h/2+math.sin(a)*r; d.ellipse([x-s,y-s,x+s,y+s],fill=255)
im=im.filter(ImageFilter.GaussianBlur(22)).point(lambda v:255 if v>120 else int(v*1.6))
im=im.filter(ImageFilter.GaussianBlur(3)); mk=Image.new('RGBA',(w,h),(0,0,0,255)); mk.putalpha(im); mk.save(os.path.join(OUT,'ink.png'))
# grain tile
g=Image.effect_noise((960,540),48).convert('L'); gr=Image.merge('RGBA',(g,g,g,Image.new('L',g.size,22))); gr.save(os.path.join(OUT,'grain.png'))
print('fx ok')
