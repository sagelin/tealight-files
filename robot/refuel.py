from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                       right_side)
from tealight.robot import *
score = 0
if touch() == 'fruit':
  score += 1
while score < 32:
  
  if look() =='fruit':
    while touch() == 'none':
      move()
    if look () == 'fruit':
      move()
    else:
      turn(1)
  if look() =='fruit':
    while touch() == 'none':
      move()
    if look () == 'fruit':
      move()
    else:
      turn(2)
if look() =='fruit':
    while touch() == 'none':
      move()
    if look () == 'fruit':
      move()
    else:
      turn(3)
if look() =='fruit':
    while touch() == 'none':
      move()
    if look () == 'fruit':
      move()
    else:
      turn(4)