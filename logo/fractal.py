from tealight.logo import move, turn

# Draws the von Koch Snowflake curve

def segment(scale, detail):
    move(scale)
    turn(120)
    move(scale)
    turn(120)
    move(scale)
    turn(120)


      

segment(100,1)
