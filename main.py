from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()
# paddle.create_paddle()
# paddle.go_up()
# paddle.go_down()


r_paddle = Paddle((-350, 0))
l_paddle = Paddle((350, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, 'w')
screen.onkeypress(r_paddle.go_down, 's')
screen.onkeypress(l_paddle.go_up, 'Up')
screen.onkeypress(l_paddle.go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
#Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.rewrite_b()
    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rewrite_a()

screen.exitonclick()

