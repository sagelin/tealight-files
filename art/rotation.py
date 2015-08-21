from tealight.art import *
from math import * 

keys = {"left": False,
        "right": False,
        "up": False,
        "down": False,
        }

car = [(x,y),(x+50,y),(x-40,y-25),(x-40,y+25),(x-40,y-25)
       ,(x,y),(x-40,y+25),(x,y),(x-40,y+25),(x+50,y),
       (x-40,y-25),(x+50,y)]
    
theta = 0
def rotation(shape, theta):
   theta = radians(theta)
   newshape = []
   for vertex in shape:
      print(vertex[0],vertex[1])
      newshape.append((((vertex[0]-x)*cos(theta)-(vertex[1]-y)*sin(theta))+x,((vertex[0]-x)*sin(theta)+(vertex[1]-y)*cos(theta)+y)))
   newcar = newshape
   print(newcar)
   return newcar


def drawcar(points,colour,x,y):
  color(colour)
  temppoints = []
  counter = 0 
  for each in points:
    temppoints.append(each[0])
    temppoints.append(each[1])
    counter += 1
    if counter == 2:
      line(x+temppoints[0],y+temppoints[1],x+temppoints[2],y+temppoints[3])
      temppoints =[]
      counter = 0
      
def handle_keydown(key): 
  keys[key] = True
  return

def handle_frame():
    if keys ["right"] == True:
      theta += 2
    elif keys["left"] == True:
      theta -= 2
      newcar = rotation(car, theta)
#  newcarpos = []
#  for i in newcar:
#    newcarpos.append(i[0]+vx)
#    newcarpos.append(i[1]+vy)
    color("white")
    box(0,0,screen_width,screen_height)
    drawcar(newcar,"blue", x, y)
  

