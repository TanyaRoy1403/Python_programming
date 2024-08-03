# import random
# from turtle import Turtle

# tim = Turtle()
# colours = ["dark red","sea green","light sea green"]
# direction = []
# for _ in range(15):
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)
#   tim.pendown()
#   tim.right(90)
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)
#   tim.pendown()
#   tim.left(90)
#   tim.forward(10)
#   tim.penup()
#   tim.forward(10)
#   tim.pendown()
#   tim.right(90)
#   tim.color("red")

#
# def draw_shape(num_side):
#     angle = 360/ num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3,8):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)
from turtle import Turtle,Screen
import random
t = Turtle()
t.colormode(255)
screen = Screen()
screen.bgcolor("gray")
# t.pensize(8)
# t.speed("fastest")
# colors = ["aquamarine","chartreuse","DeepPink","DarkSlateGray","DeepSkyBlue","MediumOrchid"]
# directions = [0,90,180,270,360]
# for i in range(200):
#     t.forward(30)
#     t.color(random.choice(colors))
#     t.seth(random.choice(directions))
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def spirograph(size_gap):
    for _ in range(int(360/size_gap)):
        t.color(random_color())
        t.circle(100)
        t.seth(t.heading() + size_gap)
spirograph(5)
screen.exitonclick()













