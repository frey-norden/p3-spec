import turtle
wn = turtle.Screen()
wn.bgcolor("hotpink")

def pentagon(dist, ang):
    b = turtle.Turtle()
    for i in range(5):
      b.forward(dist)
      b.left(ang)
dist = 65
ang = 72
for _ in range(5):
  pentagon(dist, ang)
  ang += 1
