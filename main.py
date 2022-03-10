from turtle import Screen
import time

from paddle import Paddle
from score import Score
from ball import Ball
from extra_display import Display

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-383, 0))
right_paddle = Paddle((375, 0))
score = Score()
ball = Ball()
display = Display()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)


game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()
    ball.move()

    # Detect collision with wall up and down
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(x_bounce=False, y_bounce=True)

    # Detect Collision with paddle
    right_dist = ball.distance(right_paddle) < 50 and ball.xcor() > 340
    left_dist = ball.distance(left_paddle) < 50 and ball.xcor() < -350
    if right_dist or left_dist:
        ball.bounce(x_bounce=True, y_bounce=False)

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase(left=True, right=False)
        display.change_color()

    # Detect when left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        score.increase(left=False, right=True)
        display.change_color()

screen.exitonclick()
