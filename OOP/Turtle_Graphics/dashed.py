from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")

for i in range(15):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

screen = Screen()
screen.exitonclick()
