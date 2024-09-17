import random
from turtle import Turtle , Screen
screen = Screen()
screen.setup(width=500 , height=400)
colors = ['slateblue', 'darkolivegreen', 'midnightblue', 'sienna', 'teal', 'indigo', 'darkslategray', 'maroon', 'darkorchid', 'darkgoldenrod']

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

turtle_member = [t1 , t2, t3, t4, t5, t6]

index = 0
start_x = -220
start_y = -120
for turtle in turtle_member :
    turtle.color(colors[index])
    index += 1
    turtle.shape('turtle')
    turtle.penup()
    turtle.teleport(start_x , start_y)
    start_y += 50

def back() :
    t1.backward(10)
    print(t1.pos())

screen.listen()
screen.onkey(fun=back , key='s')


screen.exitonclick()