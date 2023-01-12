import random
from turtle import Turtle, Screen
import time
POS_STARTING = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in POS_STARTING:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.snake.append(tim)

    def extend(self):
        i = self.snake[-1].position()
        self.add_segment(i)

    def head_tail(self):
        for s in self.snake:
            if s == self.head:
                pass
            elif self.head.distance(s) < 10:
                return True
        return False

    def move(self):
        for s in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[s - 1].xcor()
            new_y = self.snake[s - 1].ycor()
            self.snake[s].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
          self.head.setheading(0)

    def reset(self):
        for s in self.snake:
            s.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
