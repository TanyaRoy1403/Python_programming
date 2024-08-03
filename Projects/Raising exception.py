# height = float(input("enter your height"))
# weight = int(input("enter your weight"))
# EXCEPTION RAISE
# if height or weight is more than  a human

# if height >3:
#     raise ValueError("This is not a normal  height of human.")
#
# BMI  = weight/ height**2
# print(BMI)

fruits = ["apple", "pea", "orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + "pie")
        

make_pie(4)  # index error
