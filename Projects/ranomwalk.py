import turtle as t
import random
tim = t.Turtle()
tim.shape("turtle")
tim.pensize(15)
tim.speed("fastest")
colours = ["CornflowerBlue","DarkOrchid","DeepSkyBlue","Wheat","SeaGreen"]
direction = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colours))

    tim.forward(30)
    tim.setheading(random.choice(direction))


