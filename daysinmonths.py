year=int(input("enter the year:"))
month=int(input("enter the month:"))
def is_leap(year):
    if year%4==0:
        if year%100==0:
             if year%400==0:
              return True
    else:
        return False
def days_in_month(year,month):
      month_days=[31,28,31,30,31,30,31,30,31,30,31,30]
      if is_leap(year) and  month==2:
           return 29
      else:
       return month_days[month-1]
calling_function=days_in_month(year,month)
print(calling_function)
