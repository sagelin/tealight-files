from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                       right_side)
from tealight.robot import *
score = 0
turncounter = 0
while 1 == 1:
  print "breaking"
  if look() =='wall':
    print "wall"
    turn(1)
    turncounter += 1
  if turncounter == 4:
    turncounter = 0
    move()
  if look() =='fruit':
    turncounter = 0
    while look() =="fruit":
      if touch() == 'None':
        move()
      if touch() == 'fruit':
       move()
       score += 1
