import turtle

import project

def test_draw_triangle():
    project.draw_triangle('blue',-360,200)
    color_code='blue'
    assert(color_code=='blue')

    x=-360
    assert(x==-360)

    y=200
    assert(y==200)


def test_draw_circle():
    project.draw_circle('green', 10, -200)
    color_code='green'
    assert(color_code=='green')

    x=10
    assert(x==10)

    y=-200
    assert(y==-200)


def test_draw_rectangle():
    project.draw_rectangle('red',200, -100)
    color_code='red'
    assert(color_code=='red')


    x=200
    assert(x==200)


    y=-100
    assert(y==-100)
