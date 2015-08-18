from tealight.logo import move, turn

# Draws the von Koch Snowflake curve
angle = 60
def fractal(scale, detail):
  move(scale)
  for i in range(0, int(detail)):
    turn(angle)
    move(scale/2)
    detail =- 1
   
    
   
fractal(100,3)