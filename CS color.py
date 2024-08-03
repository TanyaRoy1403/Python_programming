n=input("Enter your input")
a=[int(i) for i in n.split()]
count=0
for i in a:
    if i>=10:
        count+=1
print(count)     

