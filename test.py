import turtle

import project

def test_rectangle_will_fit():
    project.test_rectangle_will_fit(200,-100)
    assert(turtle.xcor()==200)
    assert(turtle.ycor()==-100)


def test_triangle_will_fit():
    project.test_triangle_will_fil(-360,200)
    assert(turtle.xcor()==-360)
    assert(turtle.ycor()==200)


def test_cricle_will_fit():
    project.test_cricle_will_fit(10,-200)
    assert(turtle.xcor()==10)
    assert(turtle.ycor()==-200)
