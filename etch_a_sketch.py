"""
100 days of Python course
DAY 19
"""

# instructions: build Etch A Sketch with ---
# w = forwards, s = backwards, a = counterclock-, d = clockwise
# c = clear drawing and put turtle back in centre
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# using a usdf in conjunction with screen.listen() to determine
# user input
def move_forwards():
    tim.fd(10)
    
def move_backwards():
    tim.bk(10)
    
def move_counterclockwise():
    tim.lt(10)
    
def move_clockwise():
    tim.rt(10)
    
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

# using a function as an input
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counterclockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
