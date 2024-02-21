from turtle import Turtle, colormode

tim = Turtle()

def draw_square():
    """Draw a square."""
    for _ in range(4):
        tim.forward(100)
        tim.right(90)