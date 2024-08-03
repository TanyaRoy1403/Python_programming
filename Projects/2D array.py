import numpy as np
my_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(my_array)

#todo-->insertion into 2d array
# new_array= np.insert(my_array,0,[[1,2,3,4]],axis=1)
# print(new_array)     #axis=0 -->addition to row, axis=1--> addition to column

#todo--> access element of array
for i in range(len(my_array)):
    for j in range(len(my_array)):
        print(my_array[i][j])
        
