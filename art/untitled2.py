from tealight.art import *
from math import * 
carcolour = "red"
y = screen_height/2
x = screen_width/2


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
      
def drawcar(points,colour):
  color(colour)
  temppoints = []
  counter = 0 
  for each in points:
    temppoints.append(each[0])
    temppoints.append(each[1])
    counter += 1
    if counter == 2:
      line(temppoints[0],temppoints[1],temppoints[2],temppoints[3])
      temppoints =[]
      counter = 0
#moved = False 
newcar = rotation(car,0)
drawcar(newcar,"blue")

        

  #if moved == True:
    
   # drawcar(newcar,"white")
  #elif moved == False:
  #  drawcar(newcar,"blue")
  
keys = {"left": False,
        "right": False,
        "up": False,
        "down": False,
        }
   
acceleration = 3
vx = x
vy = y
forwardv = 0 
decelerate = False

def handle_keydown(key): 
  keys[key] = True
  return
  global newcar
  
def handle_keyup(key):
  keys[key] = False
  return 
    
def handle_frame():
  global forwardv, decelerate,theta, x, y, vx, vy, keys 
  if keys["up"] == True:
    forwardv += acceleration
  elif keys ["up"] == False:
    forwardv -= acceleration
  elif keys["down"] == True:
    forwardv -= acceleration
  if keys ["right"] == True:
    theta += 2
  elif keys["left"] == True:
    theta -= 2
  if forwardv > 60:
    forwardv = 60
#  vx += forwardv*cos(theta)
# vy -= forwardv*sin(theta)
  newcar = rotation(car, theta)
#  newcarpos = []
#  for i in newcar:
#    newcarpos.append(i[0]+vx)
#    newcarpos.append(i[1]+vy)
  color("white")
  box(0,0,screen_width,screen_height)
  drawcar(newcar,"blue")
  #color("white")
  #vx = forwarda*cos(theta)
  #vy = forwarda*sin(theta)
  #x += vx 
  #y += vy
  
  

