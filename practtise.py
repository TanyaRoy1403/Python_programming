# # length=0
# # for x in "banana":
# #     length+=1
# #     print(length)
# # # a="hello"
# # # print(a[0])
# # # print(len(a))
# # # print(len("hello"))
# # txt="the best things in life are free!"
# # if "free" in txt:
# #     print("yes,'free' is present.")
# number=10000
# print(f"{number:,}")
# name=input("enter your name")
# name=input("enter your name:")
# location=input("enter your locaion:")
# def greet_with_name(name ,location):
#     print(f"hello {name}")
#     print(f"you live at {location}")

# greet_with_name(name,location)
# age=35
# txt="my name is john and i am {}"
# print(f"my name is john and i am {age}")
# txt="my name is \bT\ba\bn\by\ba"
# print(txt.expandtabs(2))
# my_dict={83: 80}
# thislist=["apple","banana","cherry"]
# print(thislist)
# list2=list(("apple","banana","cherry"))
# print(list2)
# name=str(input('enter a name:'))
# print(name.upper())
# import main
# print(main.pi)
# a= int(input("ente value of a:"))
# b = int(input("enter value of b:"))
# def sum(a,b):
#     print(a+b)
# sum(a,b)    
# def sum(a,b):
#     c= a+b
#     return c
# var=sum(a,b)
# print(var)
class Student:
    def __init__(self,name,rollno):
        self.name= name
        self.rollno = rollno
    def show(self):
        print(self.name, self.rollno)


obj1 = Student("Tanya",8940)
obj2 = Student("Priya",54672)
obj1.show()




