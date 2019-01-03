import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor('green');
    banjo = turtle.Turtle()
    banjo.speed(10)

    #stem
    banjo.left(90)
    stem = 100

    banjo.forward(stem)

    #petals
    #angles - must add up to 180 since each occurs twice
    small = 45
    big = 180 - small

    i = 0
    while i < 36:
        banjo.left(small / 2)
        banjo.forward(stem/4)
        banjo.right(small)
        banjo.forward(stem / 4)
        banjo.right(180-small)
        banjo.forward(stem / 4)
        banjo.right(small)
        banjo.forward(stem / 4)
        #reset position, increment by 10 degrees
        banjo.right(180)
        banjo.left(small)
        banjo.right(10)
        i += 1

    window.exitonclick()
    # should be some sort of teardown to prevent crashes on subsequent runs!

#put this in a main function later
#draw_flower()
