from turtle import Screen
from snake import Snake
from scoreboard import Scorboard
from food import Food
import time

screen = Screen()


screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
scoreboard = Scorboard()
food = Food()
screen.listen()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "Up")
screen.title("My Snake Game")

game_on = True
while game_on:
    screen.update()
    time.sleep(scoreboard.speed)
    snake.move()

    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        snake.game_reset()
        scoreboard.restart()
        # scoreboard.game_over()
        # game_on = False

    if snake.head.distance(food) < 20:
        scoreboard.increase_score()
        food.reset_pos()
        snake.extend_seg()
        if scoreboard.score % 5 == 1:
            scoreboard.increase_speed()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake.game_reset()
            scoreboard.restart()
            # scoreboard.game_over()
            # game_on = False


screen.exitonclick()
