import smtplib

my_email = "tanyaroynitp9153@gmail.com"
password = "mejygxvhmahdgsah"


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="roytanya24@gmail.com", msg="subject:hello roy\n\nthis is the body")
connection.close()


# TODO we can not use close() with this syntax
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="roytanya24@gmail.com",
                        msg="subject:hello roy\n\nthis is the body")
