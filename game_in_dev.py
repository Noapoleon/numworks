from math import *
from kandinsky import *
from ion import *

###############-GLOBALS-###############
speed = 1
psize = 20
px,py = 20,20
lastx,lasty = px,py
shouldclose = False
################320x222################
def cb():
  if px>lastx:
    fill_rect(lastx,lasty,px-lastx,py-lasty+22,color(20,255,70))
  else:
    fill_rect(lastx+20,lasty,px-lastx,py-lasty+22,color(20,255,70))
  if py>lasty:
    fill_rect(lastx,lasty,px-lastx+22,py-lasty,color(20,255,70))
  else:
    fill_rect(lastx,lasty+20,px-lastx+22,py-lasty,color(20,255,70))
def drawplayer():
  fill_rect(px,py,psize,psize,(0,0,0))

def handle_input():
  global px,py,lastx,lasty,speed,shouldclose
  lastx,lasty=px,py
  if keydown(KEY_OK):
    speed *= 2
  if keydown(KEY_RIGHT):
    px += speed
  if keydown(KEY_LEFT):
    px -= speed
  if keydown(KEY_UP):
    py -= speed
  if keydown(KEY_DOWN):
    py += speed
  speed=1
def main():
  fill_rect(0,0,320,222,color(20,255,70))
  while 1:
    cb()
    handle_input()    
    drawplayer()
    
main()
