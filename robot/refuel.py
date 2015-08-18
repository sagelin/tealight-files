from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                       right_side)
from tealight.robot import *
score = 0
while score < 32:
  
  if look() =='fruit':
    while touch() == 'none':
      move()"""
    if touch() == 'fruit':
      move()
      score += 1
    else:
      turn(1)
  if look() =='fruit':
    while touch() == 'none':
      move()
    if touch() == 'fruit':
      move()
      score += 1
    else:
      turn(2)
  if look() =='fruit':
    while touch() == 'none':
      move()
    if touch() == 'fruit':
      move()
      score += 1
    else:
      turn(3)
  if look() =='fruit':
    while touch() == 'none':
      move()
    if touch() == 'fruit':
      move()
      score += 1
    else:
      turn(4)"""