import turtle
wn = turtle.Screen()

elon = turtle.Turtle()

distance = 50 
angle = 90
for _ in range(16):
    elon.forward(distance)
    elon.right(angle)
    distance += 10
    angle -= 3


