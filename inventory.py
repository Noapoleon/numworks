from math import *
from kandinsky import *

class Sprite:
  def __init__(self, sprite_data, color_list, cell_size=4):
    self.sprite_data = sprite_data
    self.color_list = color_list
    self.cell_size = cell_size
  
  def get_cell_size(self):
    return self.cell_size
  
  def draw(self, x, y, cc=8):
    for l in range(len(self.sprite_data)):
      for c in range(len(self.sprite_data[l])):
        if self.sprite_data[l][c]:
          fill_rect(c*cc+x, l*cc+y, cc, cc, self.color_list[self.sprite_data[l][c]-1])
    
class Item:
  def __init__(self, name, desc, sprite):
    self.name = name
    self.desc = desc
    self.sprite = sprite
  
  def draw(self, x, y):
    self.sprite.draw(x, y)

backpack_sprite = Sprite([
  [0,1,1,1,1,0],
  [1,2,2,2,2,1],
  [1,1,2,2,1,1],
  [1,2,1,1,2,1],
  [1,1,3,3,1,1],
  [1,2,2,2,2,1],
  [0,1,1,1,1,0]],
  ((45,18,12),(80,28,16),(240,128,15)),16)
backpack = Item('Backpack', 'A container that expands your carrying capacity',backpack_sprite)
#fill_rect(0,0,320,222,(255,0,0))
#backpack.draw(100, 100)

#slots = [{'content': None, 'amount': None} for _ in range(32)]
#for slot in slots:
  #print(slot)

#for y in range(4):
#  for x in range(8):
#    fill_rect(x*30+x*5,y*30+y*5,32, 32,(0,0,0))

# to do:
#   - sprites
#   - "add" buttons for testing
#   - OK = left click, pick all, place all
#   - BACK = right click, pick one
