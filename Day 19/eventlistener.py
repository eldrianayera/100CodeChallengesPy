import turtle

t1 = turtle.Turtle()
screen = turtle.Screen()



def move():
    t1.forward(10)
def back():
    t1.backward(10)
def counter():
    t1.setheading(t1.heading() - 10)
def clock():
    t1.setheading(t1.heading() + 10)
def clear() :
    t1.penup()
    t1.clear()
    t1.home()
    t1.pendown()


screen.listen()
screen.onkey(move , key='w')
screen.onkey(back , key='s')
screen.onkey(clock , key='a')
screen.onkey(counter , key='d')
screen.onkey(clear , key='c')

screen.exitonclick()