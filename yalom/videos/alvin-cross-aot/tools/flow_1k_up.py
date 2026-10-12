"""When Flow's 2K upscale fails, take the 1K original (1376x768) fetched from the page, upscale it 2x (LANCZOS) to
2752x1536 so the Flow marks land where flow_unsparkle.py expects them, then clean it with flow_unsparkle.py.
usage: flow_1k_up.py <in_1k.jpg> <out.png> [<in> <out> ...]"""
import sys,os,subprocess
from PIL import Image
HERE=os.path.dirname(os.path.abspath(__file__))
for src,dst in zip(sys.argv[1::2],sys.argv[2::2]):
  up=os.path.splitext(src)[0]+'_up.png'
  Image.open(src).convert('RGB').resize((2752,1536),Image.LANCZOS).save(up)
  subprocess.run([sys.executable,os.path.join(HERE,'flow_unsparkle.py'),up,dst],check=True)
