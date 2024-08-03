import datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()
if weekday==1:
    with open("quote.txt") as data_file:
        all_quotes = data_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)    