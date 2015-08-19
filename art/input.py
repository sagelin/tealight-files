from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.net import connect, send
connect(drawingpad)

xpos = 0
ypos = 0

color = ()

def handle_mousedown(x,y):
  global lastx, lasty
  lastx = x
  lasty = y
