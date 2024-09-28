from turtle import Screen ,Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)

paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_len=1,stretch_wid=5)


screen.exitonclick()