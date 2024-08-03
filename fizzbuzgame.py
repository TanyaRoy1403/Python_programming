# number%3==0-->fizz
#number%5==0-->buzz
#number%3==0 & number%5==0-->fizzbuzz
for number in range(1,101):
    if number%3==0 and number%5==0:
        print("fizz buzz")
    elif number%3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")  
    else:
        print(number)      