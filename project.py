#code that draws scenery

import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(0)

def draw_border(height):
   turtle.penup()
turtle.goto(-400,-400)
turtle.pendown()
turtle.goto(400,-400)
turtle.goto(400,400)
turtle.goto(-400,400)
turtle.goto(-400,-400)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor()

