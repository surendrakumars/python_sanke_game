import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Score

is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score.reset()

    for i in snake.snakes[1:]:
        if snake.head.distance(i) < 10:
            snake.reset()
            score.reset()

screen.exitonclick()
