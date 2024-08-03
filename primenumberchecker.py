number=int(input("enter a number:"))
def prime_checker(number):
    for i in  range(2,number):
        if number%i==0:
            print(f"{number} is not prime")
            break
    else:
     print("number is  prime")
prime_checker(number)


