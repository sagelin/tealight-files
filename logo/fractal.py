from tealight.logo import move, turn

# Draws the von Koch Snowflake curve

def segment(scale, detail):
    move(scale)
    turn(60)
    move(scale)
    turn(60)
    move(scale)


      
turn(90)
move(-300)
segment(600,1)
move(-300)