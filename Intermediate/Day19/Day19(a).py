from turtle import Turtle, Screen

blastoise = Turtle()
screen = Screen()

def move_forwards():
    blastoise.forward(20)

def move_backwards():
    blastoise.backward(20)

def left():
    new_heading = blastoise.heading() + 10
    blastoise.setheading(new_heading)

def right():
    new_heading = blastoise.heading() - 10
    blastoise.setheading(new_heading)

def clear():
    blastoise.clear()
    blastoise.penup()
    blastoise.home()
    blastoise.pendown()

screen.listen()
screen.onkey(key = "w",fun = move_forwards)
screen.onkey(key = "s",fun = move_backwards)
screen.onkey(key = "a",fun = left)
screen.onkey(key = "d",fun = right)
screen.onkey(key = "space",fun = clear)

screen.exitonclick()