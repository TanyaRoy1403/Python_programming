# import turtle
# tinny = turtle.Turtle()
# print(tinny)


# second method
# from turtle import Turtle ,Screen
# tinny = Turtle()
# print(tinny)
# tinny.shape("turtle")
# tinny.color("blue")
# tinny.fd(100)
# tinny.bk(300)
# my_screen=Screen()
# print(my_screen.canvheight)  # my_screen is object and canvheight is attribute
# my_screen.exitonclick()
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("name",["tanya","roy"])
# class User:
    
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username


# user_1 = User("505", "tanya")
# user_1.id = "801"
# user_1.username = "tanya"
# print(user_1.username)
# print(user_1.id)

# Change the 'custom inputs' below and click 'run'
# Click on 'Submit' once you have tried out to proceed to the next problem

# t = int(input("enter value of t:"))
# for i in range(t):
#     n = int(input("entter the vlaue n:"))
# print(n+1)
# Debug the following code to solve the problem

# t = int(input())
# for i in range(t):
#     N = int(input())
#     print(2*N)
# var = int(input("enter a number:"))
# def checker(var):
#     if var%2==0 or var==0:
#         print("even")
#     else:
#         print("odd")

# checker(var)
# def foo(a, b=4, c=6): 
#     print(a, b, c)
 
# foo(1)
# def fun(x, y=80):
#     print("hello")
# fun(10)   
# def my_fun(*args):
#     print(args)
# my_fun(1,3,5,6)  
# def add(*args):
#     print(args[0])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# var = add(1,2,3,4)
# print(var)
# def my_fun(**kwargs):
#     print(kwargs)
#     # print(kwargs["key1"])
# my_fun(key1=3,key2=4,key3=8)   
# def cal(**kwargs):
#     print(kwargs)
#     result =1
#     for value in kwargs.values():
#         result *= value
#     # return result    
# var=cal(a=2,b=4,c=5)    
# print(var)  
# class Computer:
#     def config(self):
#         print("15,16,17")
# obj1 = Computer()
# obj2 = Computer()
# Computer.config(obj1)          
# class Computer:
#     def __init__(self, cpu,ram) -> None:
#         self.cpu=cpu
#         self.ram=ram
#     def config(self):
#         print("config :", self.cpu,self.ram)
# obj1 = Computer(14,45)
# obj2 = Computer(23,67)
# obj1.config()
# class Car:
#     def __init__(self) -> None:
#         self.mil = 10
#         self.com = "toyota"
        
# c1 = Car()
# c2 = Car()       
# c1.mil = 3  #this will change the value of mil for object c1 only
# print(c1.mil, c2.mil,c1.com,c2.com)


class Student:
    school= "PMS" #class variable
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):   #this  is the instance method
        # return (self.m1+self.m2+self.m3)/3
        result =int((self.m1+self.m2+self.m3)/3) 
        print(result)
    # def get_m1(self):
    #     self.m1
    # def set_m1(self, value):
    #     self.m1 = value 
    @classmethod    #to call class method without using cls argument(decorator)
    def shool_name(cls):     #class method
        return cls.school  
    def info():   #static methhod it run automatically
        print("True")  

obj1 = Student(10,49,80)
obj2 = Student(34,67,87)
obj1.avg()
obj2.avg()
Student.shool_name()
print(Student.shool_name())
Student.info() 




 
