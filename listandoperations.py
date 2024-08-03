# satates_of_America=["delaware","pennsylvania","new jersy"]
# print(satates_of_America[0])
# #to edit any element of list
# satates_of_America[1]="pencilvania"
# print(satates_of_America)
# #to add extra element
# satates_of_America.append("Angelaland")
# print(satates_of_America)
# #to extend number of element 
# satates_of_America.extend(["jack bauer land","patna"])
# print(satates_of_America)
#to take many inputs of string datatype-->use split
import random
name_string=input("give me everybody's name,seperated by comma.")
names=name_string.split(",")
num_items=len(names)
random_choice=random.randint(0,num_items-1)
person_who_will_pay_bill=names[random_choice]
print(person_who_will_pay_bill+"is going buy meal today .")
