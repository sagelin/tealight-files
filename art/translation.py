car = [(x,y),(x+50,y),(x-40,y-25),(x-40,y+25),(x-40,y-25)
       ,(x,y),(x-40,y+25),(x,y),(x-40,y+25),(x+50,y),
       (x-40,y-25),(x+50,y)]

def translation(points, x,y):
  for each in points:
    each[0]+x
    each[1]+y

def drawcar(points,colour):
  color(colour)
  temppoints = []
  counter = 0 
  for each in points:
    temppoints.append(each[0])
    temppoints.append(each[1])
    counter += 1
    if counter == 2:
      line(temppoints[0],temppoints[1],temppoints[2],temppoints[3])
      temppoints =[]
      counter = 0

drawcar(car,"blue")