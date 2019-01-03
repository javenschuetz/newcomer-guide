import turtle

def draw_circle_with_squares():
    window = turtle.Screen()
    window.bgcolor('red');
    banjo = turtle.Turtle() #important: my dog's name is banjo
    banjo.speed(10)
    
    j = 0
    while j < 36:
        i = 0
        while i < 4:
            banjo.forward(100)
            banjo.right(90)
            i += 1
        banjo.right(10)
        j += 1
    window.exitonclick()
 

draw_circle_with_squares()
