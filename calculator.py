def add(n1 , n2):
    return n1+n2
def sub(n1 , n2):
    return n1-n2
def mul(n1 , n2):
    return n1*n2
def div(n1 , n2):
    return n1/n2
operators={"+":add,"-":sub,"*":mul,"/":div}
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
for symbol in operators:
    print(symbol)
choose_operators=input("enter the operator:")
cal_fun=operators[choose_operators]
answer=cal_fun(n1,n2)
print(f"{n1}{choose_operators}{n2}={answer}")




