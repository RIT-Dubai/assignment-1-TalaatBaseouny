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

#command that draws square
def draw_triangle (s,c):
   turtle.penup()
turtle.goto(-360,200)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
for i in range(3):
    turtle.forward(225)
    turtle.left(120)
turtle.end_fill()


def draw_circle(c ,l, w):
    turtle.penup()
turtle.goto(10,-200)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()


def draw_rectangle (s,h,a,a2,c):
   turtle.penup()
turtle.goto(200,-100)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.forward(150)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.end_fill()
