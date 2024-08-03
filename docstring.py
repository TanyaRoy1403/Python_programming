# syntax--> def funtion():
#           #"""docstring name"""
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print(add(2,mul(5,div(8,4))))
def outer_fun(a,b):
    def inner_fun(c,d):
        return c+d
    return inner_fun(a,b)
result=outer_fun(5,10)
print(result)