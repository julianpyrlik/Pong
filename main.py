import turtle
from turtle import Turtle, Screen
import random
import time
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
from line import Line

def pong():
    screen = Screen()
    screen.title("Pong")
    screen.setup(width=600, height=500)
    screen.bgcolor("black")
    screen.tracer(0)

    paddles = Paddles()
    ball = Ball()
    scoreboard = Scoreboard()
    line = Line()

    left_paddle = paddles.left_paddle_body
    right_paddle = paddles.right_paddle_body

    screen.listen()
    screen.onkey(fun=paddles.right_up, key="Up")
    screen.onkey(fun=paddles.right_down, key="Down")
    screen.onkey(fun=paddles.left_up, key="w")
    screen.onkey(fun=paddles.left_down, key="s")


    game_is_on = True
    start_sleep_time = 0.03

    while game_is_on:
        ball.set_start_heading()
        current_run = True
        while current_run:
            screen.update()
            time.sleep(start_sleep_time)
            ball.move()

            # Detect collision with paddle
            ball.bounce_back_right(right_paddle)
            ball.bounce_back_left(left_paddle)

            # Detect collision with wall
            ball.wall_collision()

            # Detect ball out, update points and start new run
            if ball.xcor() > 300:
                current_run = False
                scoreboard.increase_left()
                ball.speed_back_to_normal()
            elif ball.xcor() < -300:
                current_run = False
                scoreboard.increase_right()
                ball.speed_back_to_normal()
            scoreboard.current_score()


            # End game
            if scoreboard.score_right == 10:
                game_is_on = False
                print(scoreboard.score_right)
                winner = "right"
            elif scoreboard.score_left == 10:
                game_is_on = False
                print(scoreboard.score_left)
                winner = "left"

    again = screen.textinput(title="Again", prompt=f"{winner} wins! Wanna play again? y or n")
    if again == "y":
        screen.reset()
        pong()
    else:
        print("Goodbye")

    screen.exitonclick()

pong()