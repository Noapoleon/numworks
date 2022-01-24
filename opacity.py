from math import *
from kandinsky import *
    
def opacity(x,y,w,h,col):
  for c in range(h):
    for l in range(w):
      p=get_pixel(x+l,y+c)
      set_pixel(x+l,y+c,(p[0]*(1-col[3])+col[0]*col[3],p[1]*(1-col[3])+col[1]*col[3],p[2]*(1-col[3])+col[2]*col[3]))

opacity(0,0,100,100,(250,0,0,0.5))
opacity(33,33,100,100,(0,0,255,0.5))
opacity(66,66,100,100,(0,255,0,0.5))
