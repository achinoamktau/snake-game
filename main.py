import random
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

# create a snake body
snake = Snake()
food = Food()
my_score = ScoreBoard()
screen.update()
# start game
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        my_score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        my_score.reset()
        snake.reset()

    # detect collision with tail
    if snake.head_tail():
        my_score.reset()
        snake.reset()


# להבין מה זה הטיים הזה וגם מה המשמעות של האפדייט ודיליי כי זה לא ברור לי במאה אחוז :)







screen.exitonclick()