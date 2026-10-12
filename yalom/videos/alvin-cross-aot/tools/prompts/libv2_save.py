"""Save a library-redraw winner: trim black edge bars (keep 16:9), resize to 2752x1536, write to both projects' assets/redraw.
usage: libv2_save.py [--notrim] <src.png> <R##>"""
import sys, os
from PIL import Image, ImageStat
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
notrim = '--notrim' in sys.argv
src, shot = [a for a in sys.argv[1:] if a != '--notrim']
im = Image.open(src).convert('RGB'); W, H = im.size; g = im.convert('L')
dark = lambda box: g.crop(box).getextrema()[1] < 40 and ImageStat.Stat(g.crop(box)).mean[0] < 12
t = 0
while t < 80 and dark((0, t, W, t+1)): t += 1
b = 0
while b < 80 and dark((0, H-b-1, W, H-b)): b += 1
l = 0
while l < 80 and dark((l, 0, l+1, H)): l += 1
r = 0
while r < 80 and dark((W-r-1, 0, W-r, H)): r += 1
if notrim:
    t = b = l = r = 0
if t or b or l or r:
    m = max(t, b, l * H / W, r * H / W) + 4
    mx, my = round(m * W / H), round(m)
    im = im.crop((mx, my, W - mx, H - my)).resize((W, H), Image.LANCZOS)
print(f'{shot}: bars t{t} b{b} l{l} r{r}')
for proj in ('alvin-cross-aot', 'alvin-cross-aot-3p'):
    im.save(os.path.join(os.path.dirname(ROOT), proj, 'assets/redraw', shot + '.png'))
