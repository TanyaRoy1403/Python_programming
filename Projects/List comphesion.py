# number =[1,3,4]
# new_list=[]
# for n in number:
#     add_1 = n+1
#     new_list.append(add_1)
# print(new_list)


#by list comprehension

number = [1,2,3,44]
new_list =[n+1 for n in number]
print(new_list)


#syntax
# new_list=[operation for item in old_list]

name = "tanya"
new_list_02=[letter+"s" for letter in name]
print(new_list_02)

range_list=[num*2 for num in range(1,5)]
print(range_list)

#conditional list comprehension
names=["alexa","tanya","beth","jhon","neha","dave"]
new_names=[name for name in names if len(name)<5]
print(name)

