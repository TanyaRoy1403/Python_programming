import turtle as t
import random


tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(sizeof_gap):
    for _ in range(int(360/sizeof_gap)):
        tim.color(random_color())

        tim.circle(100)
        tim.setheading(tim.heading()+ sizeof_gap)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()



