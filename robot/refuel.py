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
while score < 32:
  
  if look() =='fruit':
    turncounter = 0
    while look() =="fruit":
      if touch() == 'None':
        move()
      if touch() == 'fruit':
       move()
       score += 1
       break
  if look() =='wall':
    print "wall"
    turn(1)
    turncounter += 1
  if turncounter == 4:
    print "counter"
    turncounter = 0
    move()
