from tealight.logo import move, turn

# Draws the von Koch Snowflake curve

def segment(scale, detail):
    move(scale)
    turn(120)
    move(scale)
    turn(120)
    move(scale)
    turn(120)
    if detail > 0:
      segment(scale/2, detail -1)
    

      
turn(90)
segment(100,1)
