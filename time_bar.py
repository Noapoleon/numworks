from math import *
from kandinsky import *
from time import *
from ion import *

def clamp(var,min,max):
  if min<=var<=max:
    return var
  if var<min:
    var=min
    return var
  if var>max:
    var=max
    return var

def main(t=10,bar_width=200,loss=0):
  start=monotonic()
  w_blue=bar_width
  while monotonic()-start<10:
    delta=monotonic()-start
    
    # calculate blue & black bars width
    w_black=int(((t-delta)/t)*bar_width)-bar_width
    w_blue=int(((t-delta)/t)*bar_width)
    
    # clamp values
    if keydown(KEY_OK):
      start+=0.02
    start=clamp(start,0,t)
    
    fill_rect(int((320-bar_width)/2)+bar_width,0,w_black,10,(0,0,0))
    fill_rect(int((320-bar_width)/2),0,w_blue,10,(0,200,255))
  fill_rect(0,0,320,222,(255,0,0))
  draw_string("GAME OVER",115,30,(255,255,255),(255,0,0))
