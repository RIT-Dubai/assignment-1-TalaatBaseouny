import turtle



def rectangle_will_fit(x,y, length, height):
    turtle.goto(x,y)
    turtle.screen(length=400, height=400)



    rectangle_will_fit(x,y, length, height)
    x=input("give me x of your point")
    y=input("give me y")
    length=input("give me length")
    height=input("give me height")
    rectangle_will_fit(X,y, length, height)




