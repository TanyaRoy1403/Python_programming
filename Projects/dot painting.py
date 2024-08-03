import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(244, 43, 244), (190, 15, 190), (238, 238, 238), (3, 180, 3), (20, 145, 20), (233, 239, 233), (241, 233, 241), (152, 80, 152), (220, 223, 220), (197, 38, 197), (229, 59, 229), (175, 19, 175), (220, 126, 220), (241, 161, 241), (214, 128, 214), (115, 189, 115), (238, 168, 238), (7, 113, 7), (149, 217, 149), (118, 8, 118), (122, 0, 122), (126, 136, 126), (62, 80, 62)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots = 25
for dot_count in range(1, num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()