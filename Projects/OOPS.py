# class DemoClass:
#     a = 10
#
#     def sum(self):
#         print(10+30)
#
#
# demo = DemoClass()
# demo.sum()
class DemoClass:
    a = 50

    def sum(self):
        print(self.a)  # without self we cannot access a inside a class

    def sum1(self, a, b):
        print(a+b)


obj = DemoClass()
obj.sum()
obj.sum1(16, 5)