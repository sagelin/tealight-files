from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.net import*
connect("drawingpad")

xpos = 0
ypos = 0

c="blue"

color(c)

def handle_mousedown(x,y):
  global xpos, ypos
  lastx = x
  lasty = y

def handle_mousemove(x, y, button):
   global xpos, ypos
    
   if button == "left":
    line(xpos, ypos, x, y)
    send({"xpos":xpos, "ypos":ypos, "x":x,"y":y})
    xpos = x
    ypos = y
def handle_message(message):
      line(message["xpos"],message["ypos"],message["x"],message["y"])


  
  