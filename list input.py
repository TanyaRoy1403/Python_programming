li=[]
n=int(input("Enter a number:"))
for j in range(0,n):
    ele=int(input())
    li.append(ele)
    li.sort()
var=li.pop()
print(var)    