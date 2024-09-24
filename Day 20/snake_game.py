from turtle import Screen
from snake import Snake
import time
import food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = food.Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=snake.up , key='Up')
screen.onkey(fun=snake.down , key='Down')
screen.onkey(fun=snake.left ,  key='Left')
screen.onkey(fun=snake.right , key='Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    #detect collision 
    if snake.head.distance(food) < 15 :
        food.refresh()




screen.exitonclick()