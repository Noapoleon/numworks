from math import *
from kandinsky import *

def clean_circle(r=75, ox=160, oy=111):
  for y in range(r*2):
    for x in range(r*2):
      if (sqrt((x-r)**2 + (y-r)**2) < r):
        set_pixel(x+ox-int(r), y+oy-int(r), (255,0,0))
        
def grad_circle(r1=50, r2=75, ox=160, oy=111):
  offset = r2 - r1
  for y in range(r2*2):
    for x in range(r2*2):
      centerDist = sqrt((x-r2)**2+(y-r2)**2)
      if (r2 > centerDist > r1):
        saturation = int((r2-centerDist)/offset * 255)
        set_pixel(x+ox-int(r2), y+oy-int(r2), (255,saturation,saturation))
      elif (centerDist <= r1):
        set_pixel(x+ox-int(r2), y+oy-int(r2), (255,0,0))
