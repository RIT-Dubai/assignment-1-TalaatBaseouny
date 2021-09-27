import turtle

import project

def test_rectangle_will_fit():
    project.test_rectangle_will_fit(0,0)
    assert(turtle.xcor()==0)
    assert(turtle.ycor()==0)
    assert(turtle.length()==400)
    assert(turtle.height()==400)
