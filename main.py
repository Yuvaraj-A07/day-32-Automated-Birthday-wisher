##################### Extra Hard Starting Project ######################
import random
import manager as mg
import pandas as pd
import datetime as dt
import smtplib

LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
my_mail = mg.mail
password = mg.password

# 1. Update the birthdays.csv
now = dt.datetime.now()
this_month = now.month
today = now.day
data = pd.read_csv("birthdays.csv")
today_birth = data[data["month"] == this_month]
wish_list = data.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
for person in wish_list:

    if (person["month"] == this_month and person["day"] == today):
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        rand_letter = random.choice(LETTERS)
        with open(f"letter_templates/{rand_letter}", "r") as letter_file:
            letter = letter_file.read()
            modified_letter = letter.replace("[NAME]", person["name"])
            print(modified_letter)

        # 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as send_quote:
            send_quote.starttls()
            send_quote.login(user=my_mail, password=password)
            send_quote.sendmail(from_addr=my_mail,
                                to_addrs=person["email"],
                                msg=f"Subject:Happy Birthday \n\n{modified_letter}")
