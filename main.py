from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("#BBC606")
screen.title("The Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for square in snake.segments[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()

    snake.move()
    time.sleep(0.1)


screen.exitonclick()