from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("At and Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
score.game_edge()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

end = True
while end:

    screen.update()
    if score.score < 5:
        time.sleep(0.2)
    elif score.score < 10:
        time.sleep(0.175)
    elif score.score < 25:
        time.sleep(0.15)
    elif score.score < 50:
        time.sleep(0.1)
    elif score.score < 75:
        time.sleep(0.08)
    elif score.score < 100:
        time.sleep(0.05)

    snake.s_move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_up()
        score.game_edge()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        score.game_edge()
        snake.reset_snake()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset_score()
            score.game_edge()
            snake.reset_snake()

screen.exitonclick()