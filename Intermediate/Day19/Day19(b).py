from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height=600, width=800 )
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","darkviolet"]
y_positions = [-150, -100, -50, 0, 50, 100]
all_turtle = []

for turtle_index in range(0,6):
    blastoise = Turtle(shape = "turtle")
    blastoise.penup()
    blastoise.color(colors[turtle_index])
    blastoise.goto(x=-300,y=y_positions[turtle_index])
    all_turtle.append(blastoise)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")   

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        
screen.exitonclick()