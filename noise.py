from math import *
from kandinsky import *
from random import *

def fill(n=1):
  if n==1:
    for y in range(222):
      for x in range(320):
        set_pixel(x,y,(randint(0,255),randint(0,255),randint(0,255)))
  else:
    for y in range(0,222,n):
      for x in range(0,320,n):
        fill_rect(x,y,n,n,(randint(0,255),randint(0,255),randint(0,255)))
        
def noise(n=1):
  fill(n)
  if n==1:
    while 1:
      set_pixel(randint(0,319),randint(0,221),(randint(0,255),randint(0,255),randint(0,255)))
  else:
    xr,yr=int(320/2),int(222/n)    
    while 1:
      fill_rect(randint(0,xr)*n,randint(0,yr)*n,n,n,(randint(0,255),randint(0,255),randint(0,255)))
