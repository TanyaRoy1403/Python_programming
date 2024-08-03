# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# final=add(2,9,8,4)
# print(final)

# def calculator(n, **kwargs):
#     # print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculator(2,add=6, multiply=7)


class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.make)





