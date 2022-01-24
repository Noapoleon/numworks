from math import *
from kandinsky import *
from random import *

def genList(n):
  return [(randint(0,320),randint(0,222),(randint(0,255),randint(0,255),randint(0,255))) for _ in range(n)]
def dist(x,y,a,b):
  return sqrt((x-a)**2+(y-b)**2)
def closest(list,x,y):
  closest_point=(0,0,(0,0,0))
  mindist = dist(list[0][0],list[0][1],x,y)
  for i in range(1,len(list)-1):
    d = dist(list[i][0],list[i][1],x,y)
    if d <= mindist:
      mindist = d
      closest_point = list[i]
  return closest_point
def voronoi(n):
  plist = genList(n)
  for y in range(222):
    for x in range(320):
      closestP = closest(plist,x,y)
      set_pixel(x,y,closestP[2])
  for p in plist:
    fill_rect(p[0]-2,p[1]-2,2,2,(0,0,0))
