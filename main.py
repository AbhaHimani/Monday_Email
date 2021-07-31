import smtplib
import datetime as dt
import random
my_email= "xyz@gmail.com" #Enter your email id
password="abcd" #Enter Password
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_be_sent_email ,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
