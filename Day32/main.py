import smtplib
import random

# Pull in quotes to a list
with open("quotes.txt") as quotes:
    quote_list = quotes.readlines()


# Get the current day of the week
import datetime as dt

now = dt.datetime.now()
dow = now.weekday()


# Pick a random quote from list
dow_quote = random.choice(quote_list)


# Send email to myself of the chosen quote
my_email = "EMAIL@gmail.com"
password = 'PASSWORD'

if dow == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="MYEMAIL@gmail.com",
            msg=f"Subject: Quote of the Day\n\n{dow_quote}"
        )