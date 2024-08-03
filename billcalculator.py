#greet to the user
print("welcome to the tip calculator")
#ask for the total bill
total_bill =input("what was the total bill?:")
#ask for number of person
number_persons =input("how many people to split the bill?:")
tip_given =input("what percentage tip would you like to give?10,12,15?:")
bill_with_tip =int(tip_given/100*total_bill +total_bill)
print(bill_with_tip)
bill_per_person =float(bill_with_tip/number_persons)
print(bill_per_person) 

