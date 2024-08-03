import datetime as dt
import smtplib
import random
import smtplib

# day = now.weekday()  # todo--> it gives weekday name ex--> 0= monday and so on
# month = now.month
# year = now.year
# date_birth = dt.datetime(year=2000, month=4, day=3)
# print(date_birth)
my_email = "tanyaroynitp9153@gmail.com"
password = ""
now=dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:monday motivation\n\n{quote}")






