from turtle import Rabbit ,Screen
tinny = Rabbit()
print(tinny)
tinny.shape("rabbit")
tinny.color("blue")
tinny.fd(100)
tinny.right(90)

my_screen=Screen()
print(my_screen.canvheight)  # my_screen is object and canvheight is attribute
my_screen.exitonclick()
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("pokemon name",["pikachu","squirtle","charmander"])
# table.add_column("Type",["Electric","water","fire"])
# table.align = "c"   # object attribute -->attribute=align
# print(table)
