from array import *

#todo--> create an array
my_array=array("i",[37,8,59,80,2,4,6,5])

#todo--> access each element using undex
# for i in range(len(my_array)):
#     print(my_array[i],[i])
#todo--> append any value to array using append() method
# number=int(input("Enter a value:"))
# my_array.append(number)
# print(my_array)
#todo--> insert value in array using insert() method
# number1=int(input("Enter a value1:"))
# indeces=int(input("Enter your index:"))
# my_array.insert(indeces,number1)
# print(my_array)

#todo-->extend array using extend() method
# my_array1=array("i",[46,7,39,50,8])
# my_array.extend(my_array1)
# print(my_array)

#todo--> add a list into a array using fromlist() method
li=[1,4,7,8,0,2]
my_array.fromlist(li)
print(my_array)

#todo-->remove an array element using remove() method
# my_array.remove(37)
# print(my_array)

#todo-->fetch any element through its index() method
print(my_array[0])

#todo-->reverse array
# my_array.reverse()
# print(my_array)

#todo-->get array buffer using buffer_info() method
print(my_array.buffer_info())

#todo-->count number of elements in array
count=0
for j in range(len(my_array)):
    count+=1
print(count)

#todo-->calculate occurence of element using count()
print(my_array.count(4))