from math import *
from kandinsky import *
from ion import *
from random import *
from time import *
###############-GLOBALS-###############
startx, starty = 20,20
p = { #player dictionnary to avoid using "global" keyword each time
  'speed':1,
  'size':20,
  'x':startx,
  'y':starty,
  'lastx':startx,
  'lasty':starty,
}
cp = {
  'coins': [],
  'lastgen' : monotonic(),
  'collected':0
}
bc = [20,240,70]
################320x222################
def clear():
  if p['x']>p['lastx']:
    fill_rect(p['lastx'],p['lasty'],p['x']-p['lastx'],p['y']-p['lasty']+22,bc)
  else:
    fill_rect(p['lastx']+20,p['lasty'],p['x']-p['lastx'],p['y']-p['lasty']+22,bc)
  if p['y']>p['lasty']:
    fill_rect(p['lastx'],p['lasty'],p['x']-p['lastx']+22,p['y']-p['lasty'],bc)
  else:
    fill_rect(p['lastx'],p['lasty']+20,p['x']-p['lastx']+22,p['y']-p['lasty'],bc)
def drawplayer():
  fill_rect(p['x'],p['y'],p['size'],p['size'],(0,0,0))
def handle_input():
  p['lastx'],p['lasty']=p['x'],p['y']
  if keydown(KEY_OK):
    p['speed'] *= 2
  if keydown(KEY_RIGHT):
    p['x'] += p['speed']
  if keydown(KEY_LEFT):
    p['x'] -= p['speed']
  if keydown(KEY_UP):
    p['y'] -= p['speed']
  if keydown(KEY_DOWN):
    p['y'] += p['speed']
  restrain_border()
  p['speed'] = 1
def restrain_border():
  if p['x']<0:p['x']=0
  if p['x']+p['size']>320:p['x']=320-p['size']
  if p['y']<0:p['y']=0
  if p['y']+p['size']>222:p['y']=222-p['size']
def check_collision_player(point):
  if point.x >= p['x'] and point.x <= p['x']+p['size'] and point.y >= p['y'] and point.y <= p['y']+p['size']:
    cp['collected'] += 1
    fill_rect(point.x-3,point.y-3,6,6,bc)
    return True
  return False
class Coin:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def draw(self):
    fill_rect(self.x-3, self.y-3,6,6,(255,255,0))
def coingen(d):
  if (monotonic() - cp['lastgen']) > d:
    cp['coins'].append(Coin(randint(20,300),randint(20,202)))
    cp['lastgen']=monotonic()
def draw_score():
  draw_string(str(cp['collected']),0,0)
def main():
  fill_rect(0,0,320,222,bc)
  cp['coins'].append(Coin(60,50))
  cp['coins'].append(Coin(120,80))
  cp['coins'].append(Coin(30,120))
  cp['coins'].append(Coin(50,75))
  while 1:
    clear()
    handle_input()
    draw_score()
    coingen(1)
    cp['coins'] = [c for c in cp['coins'] if not check_collision_player(c)]
    #for i in range(len(coins)):
      #if check_collision_player(coins[i]):
        #del coins[i]
    for c in cp['coins']:
      c.draw()
    drawplayer()
######IDEAS######
#win block
#teleport block/gate/dot
#coins (done)
#different sized coins, gives different amount of points
#score objective and score count (top left and right)
#put coins list into the c dictionnary
#################
main()
