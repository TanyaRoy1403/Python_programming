# import main
# print(main.sum(4,5))

# import main as M
# print(M.sum(4,6))  # aliens 
 
# from main import sum
# print(sum(4,4)) 

# from main import *  #it will import all function
# print(sum(5,5))
# print(mul(4,6))

# MATH.CEIL(X) module
import math
import random
# x=11.3
# print(math.ceil(x))  #it will return integer value of x after round off
# # MATH.FABS(X)
# x= -10
# print(math.fabs(x))  #it convert neegative value into positive

# # MATH.FACTORIAL(X)
# x= 6
# print(math.factorial(x))
# #MATH.FLOOR(X)
# x=10.5
# print(math.floor(x))   #it will retur integer value without round off


#random module
#random.randint(a,b) --> a and b both included
#random.randrange(a,b)--> not  include b
# random choice(data type)
# var = [10,30,90,48]
# print(random.choice(var))
computer_number=random.randrange(1,101)
print(computer_number)
user_number = int(input("enter your number: "))
if user_number> computer_number:
    print("too high")
elif computer_number==user_number:
    print("equal")
else:
    print("too low")



  




