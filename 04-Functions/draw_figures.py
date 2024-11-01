import turtle
import figures
side_length=figures.sdl('entre your number')
side_lengt=figures.tr("enter your number")
side_leng=figures.rect('enter your number')
side_width=figures.rectt("enter your number")


def draw_square(side_length):
    global window
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    global pen
    pen = turtle.Turtle()
    pen.speed(5)
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)
    pen.penup()
    pen.goto(-100,100)
    pen.down()
def draw_triangle(side_lengt):
    pen.speed(5)
    for g in range(3):
        pen.right(120)
        pen.forward(side_lengt)
    pen.penup()
    pen.goto(-250,250)
    pen.down()
def draw_rectangle(side_leng,side_width):
    pen.speed(5)
    for g in range(4):
        if g%2==1:
            pen.right(90)
            pen.forward(side_leng)
        if g%2==0:
            pen.right(90)
            pen.forward(side_width)
    pen.penup()
    pen.goto(400,-100)
    pen.down()
draw_square(side_length)
draw_triangle(side_lengt)
draw_rectangle(side_leng,side_width)
pen.hideturtle()

window.mainloop()