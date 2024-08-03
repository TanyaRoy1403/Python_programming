enemies=1   #global scope
def increase_enemies():
    enemies=2 #local scope
    print(f"enemies inside function :{enemies}")
increase_enemies()
print(f"enemies outside  function:{enemies}")
i=50
def foo():
   i=100
   return i
foo()
print(i)
x=200
def my_fun():
    x=300
    print(x)
my_fun()
print(x)

#function inside fun
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# global keyword--> to change the value of global variable inside the fun

x=300
def my_fun():
  global x
  x=200
my_fun()
print(x)  


