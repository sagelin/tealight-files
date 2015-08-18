from tealight.logo import move, turn

# Draws the von Koch Snowflake curve

def fractal(scale, detail):
  move(scale)
  while detail > 0:
    turn(60)
    move(scale/2)
    turn(180)
    move(scale/2)
    turn(60)
    move(scale/2)
    detail =-1
   

fractal(100,2)