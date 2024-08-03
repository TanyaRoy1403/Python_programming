from turtle import Turtle,Screen
import random
import turtle as t
tim = t.Turtle()
t.colormode(255)
t.speed("fastest")
screen = Screen()
screen.bgcolor ("gray")

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
    color = r,g,b
    return color

def spirograph(size_gap):
    for _ in range(int(360/size_gap)):
        t.color(random_color())
        t.circle(100)
        t.seth(t.heading() + size_gap)
spirograph(5)        
screen.exitonclick()