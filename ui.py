from ion import *
from kandinsky import *

class VButtonGroup:
  def __init__(self,x,y,w,h):
    self.lines=[]
    self.buttons=[]
    self.x=x
    self.y=y
    self.w=w
    self.h=h
    self.selected=0
    self.lastselected=0
    
  def addLine(self, text):
    self.lines.append(text)
  def addButton(self,text):
    self.buttons.append(text)
  def display(self):
    lah=18*len(self.lines)+6 #lines area hight
    bah=self.h-lah #buttons area hight
    bh = int((bah-10-(len(self.buttons)-1)*5)/len(self.buttons)) #one button height
    fill_rect(self.x,self.y,self.w,18*len(self.lines)+6,color(248,180,48))
    for i in range(len(self.lines)):
      fill_rect(self.x+3,self.y+i*18+3,self.w-6,18,color(248,200,68))
      draw_string(self.lines[i],self.x+int(self.w/2)-int((len(self.lines[i])*10)/2),self.y+3+18*i,(0,0,0),(248,200,68))
    fill_rect(self.x,self.y+lah,self.w,bah,color(230,230,230))
    for i in range(len(self.buttons)):
      if i==self.selected:
        fill_rect(self.x+5,self.y+lah+5+(bh+5)*i,self.w-10,bh, color(200,200,200))
        draw_string(self.buttons[i],self.x+int(self.w/2)-int((len(self.buttons[i])*10)/2),self.y+lah+5+(bh+5)*i+int(bh/2)-9,(0,0,0),(200,200,200))
      else:
        fill_rect(self.x+5,self.y+lah+5+(bh+5)*i,self.w-10,bh, color(255,255,255))
        draw_string(self.buttons[i],self.x+int(self.w/2)-int((len(self.buttons[i])*10)/2),self.y+lah+5+(bh+5)*i+int(bh/2)-9)      

def keytogglebuild(keyname,value=0):
  return {"name":keyname,"value":value,"lastdown":0}

def keytoggle(key):
  # conditions of use:
  #  - inside a loop
  #  - key is a dictionary
  #  - key has at least 3 attributes:
  #    "name", "value" and "lastdown"
  
  if keydown(key["name"]) and not key["lastdown"]:
    key["value"]= (key["value"]+1)%2
    key["lastdown"]=(key["lastdown"]+1)%2
    return 1
  if not keydown(key["name"]):
    key["lastdown"]=0

def ui():
  k_up = keytogglebuild(KEY_UP)
  k_down = keytogglebuild(KEY_DOWN)
  
  v1 = VButtonGroup(30,30,250, 150)
  v1.addLine("Hello world!")
  v1.addLine("Is the ui good?")
  v1.addButton("Yes")
  v1.addButton("No")
  v1.addButton("Cancel")
  v1.display()
  while not keydown(KEY_OK):
    v1.lastselected=v1.selected
    if keytoggle(k_up):
      v1.selected-=1
      if v1.selected<0:v1.selected=0
    if keytoggle(k_down):
      v1.selected+=1
      if v1.selected>len(v1.buttons)-1:v1.selected=len(v1.buttons)-1
    if v1.lastselected != v1.selected:
      v1.display()
  return v1.selected
  #fill_rect(0,0,320,222,(0,0,0))
  #draw_string(str(v1.selected),30,30)
