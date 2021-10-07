import turtle

import project

def test_draw_triangle():
    project.test_draw_triangle(-360,200)
    assert(turtle.xcor()==-360)
    assert(turtle.ycor()==200)




