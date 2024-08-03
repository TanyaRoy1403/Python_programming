import array as arr
my_array=arr.array("i",[2,45,6,8,9,10,56])
number=int(input("Enter a value: "))
# def sear(array,number):
#     for i in range(len(array)):
#         if(array[i]==number):
#             print("YES")
#             break
#     else:
#         print("NO")
#
# sear(my_array,number)

# def linear_sar(array,target):
#     for i in range(len(array)):
#         if(array[i]==target):
#             print("YES")
#             break
#     else:
#         print("NO")
# linear_sar(my_array,45)
my_array.append(number)
print(my_array)



