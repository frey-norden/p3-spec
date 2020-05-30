#!/usr/bin/env python3
# File: turle2.py

import turtle

wn = turtle.Screen()
color = input('Enter a color for background: ')
wn.bgcolor(color)        # set the window background color

tess = turtle.Turtle()
tcolor = input('Enter the turtle color: ')
tess.color(tcolor)              # make tess blue
tess.pensize(3)                 # set the width of her pen

tess.forward(150)               # sequence makes a triangle, what what??!!
tess.left(120)
tess.forward(150)
tess.left(120)
tess.forward(150)
wn.exitonclick()                # wait for a user click on the canvas
