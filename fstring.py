score =0
height =1.8
# print("your score"+str(score))
# we cantnot add string to a int datatype
#to avoid this problem we use fstring
print(f"your score is{score}")  #output-->your score is 0
age_as_int =input("age")
years_remaining =90-int(age_as_int)
days_remaining =years_remaining*365
weeks_remaining =years_remaining*52
months_remaining =years_remaining*12
print(f"your have{days_remaining}days,{weeks_remaining}weeks,{months_remaining}months")
