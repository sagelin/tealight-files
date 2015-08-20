from tealight.art import *
from math import * 
carcolour = "red"
y = screen_height/2
x = screen_width/2


car = [(x,y),(x+50,y),(x-40,y-25),(x-40,y+25),(x-40,y-25)
       ,(x,y),(x-40,y+25),(x,y),(x-40,y+25),(x+50,y),
       (x-40,y-25),(x+50,y)]
    

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

def handle_keydown(key):
  global newcar
  if key == "left":
    color("white")
    box(0,0,screen_width,screen_height)
      
    #drawcar(newcar,"white")
      
    newcar = rotation(newcar,-10)
    drawcar(newcar,"blue")
  elif key == "right":
    color("white")
    box(0,0,screen_width,screen_height)
    #drawcar(newcar,"white")
      
    newcar = rotation(newcar,10)
    drawcar(newcar,"blue")
        

  #if moved == True:
    
   # drawcar(newcar,"white")
  #elif moved == False:
  #  drawcar(newcar,"blue")
   


vx = 0
vy = 0
ax = 0
ay = 0

gravityx = screen_width/2
gravityy = screen_height/2

power = 0.3
gravity_power = 0.1

while True:
  

def handle_keydown(key):
  global ax, ay
  
  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0

    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)

