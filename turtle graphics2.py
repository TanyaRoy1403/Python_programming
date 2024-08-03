import turtle 

import random
from turtle import Screen
tur = turtle.Turtle()
screen = Screen()
screen.bgcolor("black ")
# screen.bgpic("C:\\Users\\Asus\\Desktop\\Tomato2.gif")
# tur.color("aquamarine")
colors = ["aquamarine","chartreuse","DeepPink","DarkSlateGray","DeepSkyBlue","MediumOrchid"]
def draw_shape(number_of_side):
    angle = 360/number_of_side
    for i in range(number_of_side):
           tur.fd(100)
           tur.right(angle)
for shape_side in range(3,11):
      tur.color(random.choice(colors))
      draw_shape(shape_side)
      
      

       





screen.exitonclick()