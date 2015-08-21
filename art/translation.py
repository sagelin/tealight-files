from tealight.art import *
from math import * 

y = screen_height/2
x = screen_width/2


car = [(x,y),(x+50,y),(x-40,y-25),(x-40,y+25),(x-40,y-25)
       ,(x,y),(x-40,y+25),(x,y),(x-40,y+25),(x+50,y),
       (x-40,y-25),(x+50,y)]

def translation(points, x,y):
  print points
  newpoints = []
  for each in points:
    newx=each[0]+x
    newy=each[1]+y
    newpoints.append((newx,newy))
  return newpoints

def drawcar(points,colour):
  color(colour)
  temppoints = []
  counter = 0
  print points
  for each in points:
    temppoints.append(each[0])
    temppoints.append(each[1])
    counter += 1
    if counter == 2:
      line(temppoints[0],temppoints[1],temppoints[2],temppoints[3])
      temppoints =[]
      counter = 0

drawcar(car,"blue")
newcar = translation(car,60,200)
drawcar(newcar,"red")