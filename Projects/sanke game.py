import time
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=680, height=680)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# segment_1 = Turtle("square")     #first box
# segment_1.color("white")
#
# segment_2 = Turtle("square")    #second box added behind the first
# segment_2.color("white")
# segment_2.goto(-20, 0)          #distance measure from centre
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []


for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
     for seg in segments:
         seg.forward(20)
         screen.update()
         time.sleep(1)

screen.exitonclick()




