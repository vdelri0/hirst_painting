from turtle import Turtle, Screen, colormode
from random import choice, randint

tim = Turtle()
colormode(255)
# tim.shape("turtle")
# tim.color("red")

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)

colors = ["royal blue", "deep sky blue", "turquoise", "aquamarine", "pale green", "dark khaki", "goldenrod", "dark red"]
directions = [0, 90, 180, 270]
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
        tim.color(random_color())
        draw_shape(side_n)

def select_walk(walk, distance):
    if walk == 1: tim.fd(distance)
    elif walk == 2: tim.bk(distance)
    elif walk == 3: tim.rt(distance)
    else: tim.lt(distance)

def draw_random_walk():
    """Generates a real random walk."""
    tim.pensize(15)
    tim.speed(10)

    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(choice(directions))

draw_random_walk()


screen = Screen()
screen.exitonclick()
