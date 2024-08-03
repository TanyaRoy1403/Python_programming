from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
y_position = [-70,-40,-10,20,50,80]
# user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter the color:")
color_list = ["red","blue","yellow","purple","green","orange"]
for turtle_index in range(0,6):
    tur = Turtle(shape="turtle")
    tur.penup()
    tur.goto(-230,y=y_position[turtle_index])
    # tur.color(random.choice(color_list))  #it will give same color to one or moree turtle
    tur.color(color_list[turtle_index])
screen.exitonclick()
 