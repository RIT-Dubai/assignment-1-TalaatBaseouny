import turtle

import project

def test_draw_triangle():
    project.test_draw_triangle(-360,200)
    assert(turtle.xcor()==-360)
    assert(turtle.ycor()==200)


def test_draw_rectangle():
    project.test_draw_rectangle(200,-100)
    assert(turtle.xcor()==200)
    assert(turtle.ycor()==-100)


