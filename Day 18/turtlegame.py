import turtle
from turtle import Turtle , Screen


t = Turtle()
screen = Screen()

t.color('cyan3')
t.shape('turtle')



for go in range(10) :
    t.forward(100)
    t.right(72)

screen.exitonclick()