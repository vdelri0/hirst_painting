from turtle import Turtle, colormode
from random import randint

tim = Turtle()
colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)

def draw_shape(sides):
    """Allows you to draw shapes no matter the sides."""
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

def draw_shapes():
    """Draw shapes from triangle to decagon."""
    for side_n in range(3,11):
        tim.color(random_color())
        draw_shape(side_n)