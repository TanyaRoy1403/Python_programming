import array as arr
my_array = arr.array("i",[1,9,6,10,3])
my_array.insert(0,7)
print(my_array)
# for i in range(0,len(my_array)):
#     print(my_array[i],i)

# def travese(array):
#     for i in array:
#         print(i)
# travese(my_array)

def accs(array,index):
    if index >= len(array):
        print("no")
    else:
        print(array[index])
accs(my_array,6 )
