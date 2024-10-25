import turtle





def draw_square(side_length):
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    pen = turtle.Turtle()
    pen.speed(5)
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)
    pen.hideturtle()
    window.mainloop()
