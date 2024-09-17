import random
from random import randint
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
finish_x = 220

for turtle in turtle_member :
    turtle.color(colors[index])
    index += 1
    turtle.shape('turtle')
    turtle.penup()
    turtle.teleport(start_x , start_y)
    start_y += 50

def check_finish():
    for turtle in turtle_member :
        print(turtle.pos()[0])
        if turtle.pos()[0] > 220 :
            return True

def start_the_race() :
    race_on = True
    while race_on :
        if check_finish() :
            race_on = False

        else :
            for turtle in turtle_member :
                screen.ontimer(turtle.forward(random.randint(10,30)) , 100)






screen.listen()
screen.onkey(fun=start_the_race , key='space')


screen.exitonclick()

