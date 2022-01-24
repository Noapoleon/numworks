from math import *
from kandinsky import *
from ion import *

def sus(x=120,y=60,n=8):
  
  susman=[
    [0,1,1,1],
    [1,1,2,2],
    [1,1,1,1],
    [1,1,1,1],
    [0,1,0,1]]
  
  for l in range(len(susman)):
    for c in range(len(susman[l])):
      if susman[l][c]==1:
        fill_rect(x+c*n,y+l*n,n,n,(255,0,0))
      elif susman[l][c]==2:
        fill_rect(x+c*n,y+l*n,n,n,(0,255,255))
      else:
        fill_rect(x+c*n,y+l*n,n,n,(255,255,255))
def clearbuffer(x,y,w,h,s):
  pass
        
def amogus():
  x,y=146,160
  lx,ly=x,y
  
  while 1:  
    if keydown(KEY_LEFT):
      x-=2
    elif keydown(KEY_RIGHT):
      x+=2
    if keydown(KEY_UP):
      y-=2
    elif keydown(KEY_DOWN):
      y+=2
    
    if x>lx:
      fill_rect(lx,ly,2,8*5,(255,255,255))
    else:
      fill_rect(x+8*4,ly,2,8*5,(255,255,255))
    if y>ly:
      fill_rect(lx,ly,8*4,2,(255,255,255))
    else:
      fill_rect(lx,y+8*5,8*4,2,(255,255,255))
 
    lx,ly=x,y
    sus(x,y)
