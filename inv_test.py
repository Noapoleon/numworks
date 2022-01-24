from kandinsky import *
from ion import *
from keytoggle import *

class Sprite:
  def __init__(self, sprite_data, color_list, cell_size):
    self.sprite_data = sprite_data
    self.color_list = color_list
    self.cell_size = cell_size
  
  def draw(self, x, y):
    for l in range(len(self.sprite_data)):
      for c in range(len(self.sprite_data[l])):
        if self.sprite_data[l][c]:
          fill_rect(c*self.cell_size+x, l*self.cell_size+y, self.cell_size, self.cell_size, self.color_list[self.sprite_data[l][c]-1])

class Item:
  def __init__(self, nom, desc, sprite):
    self.nom=nom
    self.desc=desc
    self.sprite=sprite
    
  def draw(self,x,y):
    self.sprite.draw(x,y)

coin_sprite = Sprite([
  [0,0,1,1,1,0,0],
  [0,2,1,1,1,1,0],
  [0,2,1,1,1,1,0],
  [0,2,1,1,1,1,0],
  [0,2,1,1,1,1,0],
  [0,2,2,1,1,1,0],
  [0,0,2,2,2,0,0]],[(255,200,0),(255,150,0)],4)
coin = Item("Coin", "A piece of gold used for commercial exchange", coin_sprite)

coin2_sprite = Sprite([
  [0,0,1,1,1,0,0],
  [0,2,1,1,1,1,0],
  [0,2,1,1,1,1,0],
  [0,2,1,1,1,1,0],
  [0,2,1,1,1,1,0],
  [0,2,2,1,1,1,0],
  [0,0,2,2,2,0,0]],[(250,250,250),(220,220,255)],4)
coin2 = Item("Coin2", "A piece of platinum used for commercial exchange", coin2_sprite)



class Slot:
  def __init__(self, pos, size, vs, item=None):
    assert type(pos)==type([]) or type(pos)==type(()), "please use [] or () for position of slot"
    assert type(size)==type(0), "slot size needs to be of type int"
    self.pos=[pos[0],pos[1]] # compatible with [] and ()
    self.size=size
    self.vs=vs # voxel size
    self.item=item
  def draw(self):
    fill_rect(self.pos[0],self.pos[1],self.size,self.size,(0,0,0))
    if self.item != None:
      self.item.draw(self.pos[0]+self.vs,self.pos[1]+self.vs)
  def erase(self):
    fill_rect(self.pos[0],self.pos[1],self.size,self.size,(0,255,0))

class Desc:
  def __init__(self, slot, item=None):
    self.slot=slot
    self.item=item

class Inventory:
  def __init__(self, x=20, y=20, w=8, h=4, ss=36, vs=4):
    self.x=x
    self.y=y
    self.w=w
    self.h=h
    self.slots= [[Slot((x+c*(ss+vs),y+l*(ss+vs)),ss,vs) for c in range(w)] for l in range(h)]
    self.ss=ss # slot size    
    self.vs=vs # voxel size
    l=[]
    l+=[1 for i in range(int(self.ss/self.vs))],
    for k in range(int(self.ss/self.vs)-2):
      l+=[1]+[0 for i in range(int(self.ss/self.vs)-2)]+[1],
    l+=[1 for i in range(int(self.ss/self.vs))],
    self.cursor_sprite=Sprite(l,[(255,0,0)],vs)
    self.cursor=[0,0]
    self.lastcursor=[0,0]

  def draw(self):
    for l in range(len(self.slots)):
      for c in range(len(self.slots[l])):
        fill_rect(self.x+(self.ss+self.vs)*c,self.y+(self.ss+self.vs)*l,self.ss,self.ss,(0,0,0))
    self.draw_selected()
  def draw_selected(self):
    x=self.slots[self.cursor[1]][self.cursor[0]].pos[0]
    y=self.slots[self.cursor[1]][self.cursor[0]].pos[1]
    self.cursor_sprite.draw(x,y)

  def move_cursor(self, x, y):
    self.cursor = [self.cursor[0]+x,self.cursor[1]+y]
  
  def handle_input(self,k_u, k_d, k_l, k_r, k_ok):
    self.lastcursor = self.cursor
    
    # move cursor
    if keytoggle(k_u):
      self.move_cursor(0,-1)
    elif keytoggle(k_d):
      self.move_cursor(0,1)
    if keytoggle(k_l):
      self.move_cursor(-1,0)
    elif keytoggle(k_r):
      self.move_cursor(1,0)
    
    # restrict cursor
    if self.cursor[0]<0:
      self.cursor[0]=0
    elif self.cursor[0]>self.w-1:
      self.cursor[0]=self.w-1
    if self.cursor[1]<0:
      self.cursor[1]=0
    elif self.cursor[1]>self.h-1:
      self.cursor[1]=self.h-1
    
    slot=self.slots[self.cursor[1]][self.cursor[0]]
    lastslot=self.slots[self.lastcursor[1]][self.lastcursor[0]]
    
    # add item
    if keytoggle(k_1):
      slot.item = coin
      slot.draw()
      self.draw_selected()
    if keytoggle(k_2):
      slot.item = coin2
      slot.draw()
      self.draw_selected()
    # remove item
    if keytoggle(k_bks):
      slot.item = None
      slot.draw()   
    # draw selected
    if self.cursor != self.lastcursor:    
      # erase last and redraw item (easy solution, make right later) and redraw selected
      lastslot.erase()
      lastslot.draw()
      self.draw_selected()

inv = Inventory(17,17,5,5,36,4)
inv.draw()
k_u = keytogglebuild(KEY_UP)
k_d = keytogglebuild(KEY_DOWN)
k_l = keytogglebuild(KEY_LEFT)
k_r = keytogglebuild(KEY_RIGHT)
k_ok = keytogglebuild(KEY_OK)
k_bks = keytogglebuild(KEY_BACKSPACE)
k_1 = keytogglebuild(KEY_ONE)
k_2 = keytogglebuild(KEY_TWO)
while 1:
  inv.handle_input(k_u, k_d, k_l, k_r, k_ok)
  
# automatiser creation touches
# make stacks
