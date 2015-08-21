from tealight.art import *
from math import * 
carcolour = "red"
y = screen_height/4
x = screen_width/4


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
#moved = False 

        

  #if moved == True:
    
   # drawcar(newcar,"white")
  #elif moved == False:
  #  drawcar(newcar,"blue")
  
keys = {"left": False,
        "right": False,
        "up": False,
        "down": False,
        }
   
acceleration = 0
forwardv = 10 

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
    forwardv += 0.1
  elif keys ["up"] == False:
    forwardv -= 0.1
  elif keys["down"] == True:
    forwardv -= acceleration
  if keys ["right"] == True:
    theta += 2
  elif keys["left"] == True:
    theta -= 2
  if forwardv > 2:
    forwardv = 2
  x += forwardv*cos(theta)
  y -= forwardv*sin(theta)
  newcar = rotation(car, theta)
#  newcarpos = []
#  for i in newcar:
#    newcarpos.append(i[0]+vx)
#    newcarpos.append(i[1]+vy)
  color("white")
  box(0,0,screen_width,screen_height)
  drawcar(newcar,"blue", x, y)
  #color("white")
  #vx = forwarda*cos(theta)
  #vy = forwarda*sin(theta)
  #x += vx 
  #y += vy
  
  

