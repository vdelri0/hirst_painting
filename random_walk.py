from turtle import Turtle, Screen, colormode
from random import choice, randint

tim = Turtle()
colormode(255)

directions = [0, 90, 180, 270]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)

def draw_random_walk():
    """Generates a real random walk."""
    tim.pensize(15)
    tim.speed(10)

    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(choice(directions))