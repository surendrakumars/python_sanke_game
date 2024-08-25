import time
from  turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake :-)")
screen.tracer(0)

#creation of the snake

snake = Snake()#moving the snake#control the snake
food = Food()#postioning the food at random position
score = Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_move = True
while is_move:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

#detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_move = False
        score.game_over()

#detect collision with tail
    for segement in snake.segments[1:]:
        if snake.head.distance(segement) < 10:
            is_move = False
            score.game_over()
screen.exitonclick()



