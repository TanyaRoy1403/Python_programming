print("welcome to the pizza hut!!")
size =input("what will be the size of your piza? S,M,L :")
add_pepperoni =input("do want pepperoni? Y or N :")
extra_cheese=input("do want extra cheese? Y or N :")
bill = 0
if size == "S":
    bill +=15
elif size =="M":
    bill +=2
else:
    bill +=25
if add_pepperoni =="Y":
    if size =="S":
        bill+=2
    else:
        bill+=3
if extra_cheese =="Y":
    bill+=1


print(f"your final bill is {bill}")





