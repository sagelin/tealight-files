from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                       right_side)
score = 0
if thing == fruit:
  score += 1
from tealight.robot import *
while score < 32:
  
  if look() =='fruit':
    while touch() == 'none':
      move()
    if look () == 'fruit':
      move()
      break
    else:
      turn(1)