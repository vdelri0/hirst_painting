from turtle import Turtle, Screen, colormode, Vec2D
from random import choice, randint

directions = [0, 90, 180, 270]
colors = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

tim = Turtle()
position = tim.pos()
tim.speed(10)
tim.hideturtle()

colormode(255)

for x in range(10):
    for y in range(10):
        tim.dot(20, choice(colors))
        tim.penup()
        tim.forward(30)

    position = Vec2D(position[0], position[1] + 30)
    tim.setpos(position[0], position[1])
    tim.penup()

screen = Screen()
screen.exitonclick()
