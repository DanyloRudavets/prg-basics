import turtle
import figures
side_length=figures.sdl('entre your number')


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
draw_square(side_length)