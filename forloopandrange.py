# syntax--> for number in range(a,b):
#print(number)
# for number in range(1, 11, 3):  #not include 11
#      print(number)
     # range(a,b)--> implies b inncrease every timme by a
     #range(a,b,c)-->implies a inncrease every timme by c
# total=0
# for number in range(1,101):
#     total+=number
#     print(total)
    #sum of all even numbers
total=0
for even_number in range(1,101):
         if even_number%2==0:
           total+=even_number
print(total)