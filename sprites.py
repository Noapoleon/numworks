from kandinsky import *
class Sprite:
  def __init__(self, sprite_data, color_list, cell_size):
    self.sprite_data = sprite_data
    self.color_list = color_list
    self.cell_size = cell_size
  
  def draw(self, x, y):
    for l in range(len(self.sprite_data)):
      for c in range(len(self.sprite_data[l])):
          fill_rect(c*self.cell_size+x, l*self.cell_size+y, self.cell_size, self.cell_size, self.color_list[self.sprite_data[l][c]])

sus1_data=[
  [0,1,1,1],
  [1,1,2,2],
  [1,1,1,1],
  [1,1,1,1],
  [0,1,0,1]]
sus1_sprite=Sprite(sus1_data,((255,255,255),(255,0,0),(0,255,255)),8)


sus2_data=[
  [1,1,1,0],
  [2,2,1,1],
  [1,1,1,1],
  [1,1,1,1],
  [1,0,1,0]]
sus2_sprite=Sprite(sus2_data,((255,255,255),(0,0,255),(0,255,255)),8)

sus1_sprite.draw(100,100)
sus2_sprite.draw(200,100)
