"""
100 days of Python course
DAY 19
"""

# learning about concepts of states and instances

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# use positional inputs to enable next person to quickly
# understand measurements:
screen.setup(width=500, height=400)

# use a turtle method to allow for user to type input:
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "green", "blue", "orange", "purple", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # each turtle moves a random amount of steps(distance)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# use the goto method which uses x and y value co-ordinates
# centre is 0,0 so where height (y) = 400 the distance from 0 to
# top edge is 200 i.e. 0 is in the middle of the height measurement
# using this logic the bottom is -200

screen.exitonclick()
