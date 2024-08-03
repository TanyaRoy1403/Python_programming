print("welcome to the rollercoater !!")
height = int(input("what is your height in cm?"))
if height >=120:
    print("you can ride")
    age =int(input("what is the age of person?"))
    if age<12:
        bill =5
        print("child tickets are $5.")
    elif age<=18:
        bill =7
        print("youth tickets are $7.")
    else :
        bill =12
        print("adult tickets are $12.")    
        wants_photo =input("do u want photo? Y or N :")    

    if wants_photo =="Y":
        bill +=3
        print(f"your final bill is :{bill}")
else:
    print("you can not ride.")  