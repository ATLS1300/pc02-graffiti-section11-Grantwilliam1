#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Grant Young
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

turtle.pensize(1)
turtle.color("DarkGoldenrod1")
turtle.up()
turtle.goto(0,150)
turtle.down()
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(160)
turtle.left(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(10)
turtle.end_fill()

turtle.pensize(5)
turtle.color("red4")
turtle.up()
turtle.goto(0,160)
turtle.left(90)
turtle.down()
turtle.begin_fill()
turtle.forward(55)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(160)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(110)
turtle.end_fill()

turtle.pensize(2)
turtle.color("yellow")
turtle.up()
turtle.goto(300, 200)
turtle.down()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.pensize(1)
turtle.color("black")
turtle.up()
turtle.goto(40,100)
turtle.down()
turtle.left(15)
turtle.forward(20)
turtle.up()
turtle.goto(47, 105)
turtle.down()
turtle.right(105)
turtle.forward(10)
turtle.up()
turtle.goto(54, 107)
turtle.down()
turtle.forward(8)
turtle.up()
turtle.goto(0,0)

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
