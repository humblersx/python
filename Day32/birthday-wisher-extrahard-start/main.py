##################### Extra Hard Starting Project ######################


# 2. Check if today matches a birthday in the birthdays.csv
import pandas
import datetime as dt
import random
import smtplib

# Email info
my_email = "EMAIL@gmail.com"
password = 'PASSWORD'

# Get todays day and month
now = dt.datetime.now()

month = now.month
day = now.day



# Create a dictionary
bdays = pandas.read_csv("birthdays.csv")

for index, row in bdays.iterrows():
    if month == row["month"] and day == row["day"]:
        # randomly choose a letter number
        random_number = random.randint(1, 3)

        # compose chosen letter
        with open(f"letter_templates/letter_{random_number}.txt") as bday_letter:
            letter = bday_letter.readlines()

        letter[0] = letter[0].replace("[NAME]", row["name"])

        new_letter = ""
        for each in letter:
            new_letter += each


        # # Send letter
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="MYEMAIL@gmail.com",
                msg=f"Subject: Happy Birthday!\n\n{new_letter}"
            )







