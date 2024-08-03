import colorgram
import turtle as tur
import random
tur.colormode(255)
# tur.Turtle()
screen = tur.Screen()

tur.speed("fastest")
tur.penup()
tur.hideturtle()

color_list = [(244, 43, 244), (190, 15, 190), (238, 238, 238), (3, 180, 3), (20, 145, 20), (233, 239, 233), (241, 233, 241), (152, 80, 152), (220, 223, 220), (197, 38, 197), (229, 59, 229), (175, 19, 175), (220, 126, 220), (241, 161, 241), (214, 128, 214), (115, 189, 115), (238, 168, 238), (7, 113, 7), (149, 217, 149), (118, 8, 118), (122, 0, 122), (126, 136, 126), (62, 80, 62)]

tur.setheading(225)
tur.forward(250)
tur.setheading(0)
num_of_dots = 100
for dot_count in range(1, num_of_dots+1):
    tur.dot(20, random.choice(color_list))
    tur.forward(50)

    if dot_count % 10 ==0:
        tur.setheading(90)
        tur.forward(50)
        tur.setheading(180)
        tur.forward(500)
        tur.setheading(0)











screen.exitonclick()