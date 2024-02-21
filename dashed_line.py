from turtle import Turtle

tim = Turtle()

def draw_a_dashed_line():
    """Draw a dashed line."""
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()