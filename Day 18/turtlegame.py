import turtle
from turtle import Turtle , Screen
import random


t = Turtle()
screen = Screen()
t.speed('fastest')
t.penup()


t.shape('turtle')
colors = ['lavender', 'peachpuff', 'lightcoral', 'mintcream', 'powderblue', 'rosybrown', 'honeydew', 'thistle', 'seashell', 'lightsteelblue']
dark_aesthetic_colors = ['slateblue', 'darkolivegreen', 'midnightblue', 'sienna', 'teal', 'indigo', 'darkslategray', 'maroon', 'darkorchid', 'darkgoldenrod']





def spot_painting(row , col) :
    y = t.pos()[1]
    x = t.pos()[0]
    for line in range(col) :
        for dot in range(row):
            t.dot(20, random.choice(dark_aesthetic_colors))
            t.forward(50)
            print(t.pos())
        y += 50
        t.teleport(x, y)



t.setheading(225)
t.forward(300)
t.setheading(0)
print(t.pos())
spot_painting(10 , 10)








screen.exitonclick()