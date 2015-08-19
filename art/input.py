from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.net import connect, send
connect(drawingpad)

xpos = 0
ypos = 0



color(selected color)

def handle_mousedown(x,y):
  global xpos, ypos
  lastx = x
  lasty = y

  def handle_mousemove(x, y, button):
    global xpos, ypos