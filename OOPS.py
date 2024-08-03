class DemoClass: #class
      a = 10  # inside class a variable define
      def sum(self):  # fun inside a class --> must contain  a argument 
          print(self.a)
                  
demo=DemoClass()   #object
print(demo.a)   #calling variable through object
demo.sum()    #callin sum function

class DemoClass:  # class
    a = 10        # inside a class a variable define
    
    def sum(self):  #fun inside class--> must have a argument
        print(10+30)


demo = DemoClass()  # object
demo.sum()          # calling  fun by object


# use of self
class DemoClass:
    a= 50
    
    def sum(self):
        print(self.a)  # without self we cannot access a inside a class
    def sum1(self,a,b):
        print(a+b)
 
obj = DemoClass()
obj.sum()        
obj.sum1(16,5)

# constructor--> def __init(self):


