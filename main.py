import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")

screen = Screen()
screen.bgcolor("aquamarine4")
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        score.game_over()

    # Detect collision with tail / any segment in the tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            score.game_over()


screen.listen()
screen.exitonclick()
