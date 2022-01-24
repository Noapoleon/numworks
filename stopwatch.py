from math import *
from time import *
from kandinsky import *

def timer():
  currentTime = monotonic()
  lastTime = monotonic()
  m,s = 0,0
  while 1:
    currentTime = monotonic()
    if currentTime - lastTime >= 1:
      s += 1
      if s > 59:
        s = 0
        m += 1
      lastTime = monotonic()
      #print(str(m//10) + str(m%10) + ":" + str(s//10)+str(s%10))
      draw_string((str(m//10) + str(m%10) + ":" + str(s//10)+str(s%10)),160-25,20)
