#The Pong Game

from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height= 600, width= 800)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()

r_paddle = Turtle()
r_paddle.shape("square")
r_paddle.color("blue")
r_paddle.shapesize(stretch_wid=5, stretch_len=1)
r_paddle.penup()
r_paddle.goto(350,0)

l_paddle = Turtle()
l_paddle.shape("square")
l_paddle.color("red")
l_paddle.shapesize(stretch_wid=5, stretch_len=1)
l_paddle.penup()
l_paddle.goto(-350,0)

def go_up1():
    new_y = r_paddle.ycor() + 30
    r_paddle.goto(r_paddle.xcor(),new_y)

def go_down1():
    new_y = r_paddle.ycor() - 30
    r_paddle.goto(r_paddle.xcor(),new_y)

def go_up2():
    new_y = l_paddle.ycor() + 30
    l_paddle.goto(l_paddle.xcor(),new_y)

def go_down2():
    new_y = l_paddle.ycor() - 30
    l_paddle.goto(l_paddle.xcor(),new_y)

screen.listen()
screen.onkey(go_up1,"Up")
screen.onkey(go_down1,"Down")
screen.onkey(go_up2,"w")
screen.onkey(go_down2,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor()>320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()
    
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
    

screen.exitonclick() 
 