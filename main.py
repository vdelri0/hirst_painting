from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

colors = ["royal blue", "deep sky blue", "turquoise", "aquamarine", "pale green", "dark khaki", "goldenrod", "dark red"]

def draw_square():
    """Draw a square."""
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def draw_a_dashed_line():
    """Draw a dashed line."""
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

def draw_shape(sides):
    """Allows you to draw shapes no matter the sides."""
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

def draw_shapes():
    """Draw shapes from triangle to decagon."""
    for side_n in range(3,11):
        tim.color(choice(colors))
        draw_shape(side_n)

def select_walk(walk, distance):
    if walk == 1: tim.fd(distance)
    elif walk == 2: tim.bk(distance)
    elif walk == 3: tim.rt(distance)
    else: tim.lt(distance)

def draw_random_walk():
    """Generates a real random walk."""
    distance = 90
    tim.speed(10)

    for _ in range(100):
        color = choice(colors)
        tim.dot(10, color)
        tim.pen(pencolor=color, pensize=10)
        select_walk(randint(1, 4), distance)

draw_random_walk()


screen = Screen()
screen.exitonclick()
