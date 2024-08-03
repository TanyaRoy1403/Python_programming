import turtle as t



tim = t.Turtle()
t.colormode(255)



tim.speed("fastest")

def draw_spirograph(sizeof_gap):
    for _ in range(int(360/sizeof_gap)):
        tim.color("pink")
        tim.pensize(2)
        tim.circle(100)
        tim.setheading(tim.heading()+ sizeof_gap)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()