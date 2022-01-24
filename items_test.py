from kandinsky import *

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
 

default_sprite = Sprite([
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],],[[0,0,0]],4)
default = Item("", "", default_sprite)

b_sprite = Sprite([
  [0,1,1,1,1,1,0],
  [1,1,2,2,2,1,1],
  [1,0,1,1,1,0,1],
  [1,1,1,0,1,1,1],
  [1,0,1,1,1,0,1],
  [1,1,2,2,2,1,1],
  [0,1,1,1,1,1,0]],[[255,200,0],[255,180,0]],4)
b = Item("B", "A blue item of unknown origins", b_sprite)

zero_sprite = Sprite([
  [0,1,0],
  [1,0,1],
  [1,0,1],
  [1,0,1],
  [0,1,0]],[[255,0,0]],2)
zero = Item("", "", zero_sprite)


one_sprite = Sprite([
  [0,1,0],
  [1,1,0],
  [0,1,0],
  [0,1,0],
  [1,1,1]],[[255,0,0]],2)
one = Item("", "", one_sprite)

two_sprite = Sprite([
  [1,1,0],
  [0,0,1],
  [0,1,0],
  [1,0,0],
  [1,1,1]],[[255,0,0]],2)
two = Item("", "", two_sprite)

three_sprite = Sprite([
  [1,1,0],
  [0,0,1],
  [0,1,0],
  [0,0,1],
  [1,1,0]],[[255,0,0]],2)
three = Item("", "", three_sprite)

four_sprite = Sprite([
  [1,0,0],
  [1,0,1],
  [1,1,1],
  [0,0,1],
  [0,0,1]],[[255,0,0]],2)
four = Item("", "", four_sprite)

five_sprite = Sprite([
  [1,1,1],
  [1,0,0],
  [1,1,0],
  [0,0,1],
  [1,1,0]],[[255,0,0]],2)
five = Item("", "", five_sprite)

six_sprite = Sprite([
  [0,1,1],
  [1,0,0],
  [1,1,0],
  [1,0,1],
  [0,1,0]],[[255,0,0]],2)
six = Item("", "", six_sprite)

seven_sprite = Sprite([
  [1,1,1],
  [0,0,1],
  [1,1,1],
  [0,1,0],
  [0,1,0]],[[255,0,0]],2)
seven = Item("", "", seven_sprite)

eight_sprite = Sprite([
  [0,1,0],
  [1,0,1],
  [0,1,0],
  [1,0,1],
  [0,1,0]],[[255,0,0]],2)
eight = Item("", "", eight_sprite)

nine_sprite = Sprite([
  [0,1,0],
  [1,0,1],
  [0,1,1],
  [0,0,1],
  [0,1,0]],[[255,0,0]],2)
nine = Item("", "", nine_sprite)

class Desc:
  def __init__(self, pos, item=None):
      self.pos = pos
      self.slot = Slot([self.pos[0]+25,self.pos[1]+50],50,4)

  def draw(self):
    fill_rect(self.pos[0],self.pos[1],100,200,(200,100,20))
    self.slot.draw()
fill_rect(0,0,320,222,(0,0,0))
b.draw(50,50)
zero.draw(92,50)
one.draw(100,50)
two.draw(108,50)
three.draw(116,50)
four.draw(124,50)
five.draw(132,50)
six.draw(140,50)
seven.draw(148,50)
eight.draw(156,50)
nine.draw(164,50)
print(b.desc)

desc = Desc([200,10])
desc.draw()
