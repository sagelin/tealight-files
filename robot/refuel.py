from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                       right_side)

turncounter = 0
while True:
  print "breaking"
  if look() =='wall':
    print "wall"
    turn(1)
    turncounter += 1
  if turncounter == 4:
    turncounter = 0
    while touch() == 'wall':
      turn(1)
    move()
  if look() =='fruit':
    turncounter = 0
  while look() =="fruit":
    move()
    break