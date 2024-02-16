from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(4): #Create a square
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
