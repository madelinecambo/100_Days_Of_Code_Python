##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas as pd
import os

MY_EMAIL = ""
MY_PASSWORD = ""

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today_day = dt.datetime.now().day
today_month = dt.datetime.now().month

letters_list = os.listdir("letter_templates")

birthdays = pd.read_csv('birthdays.csv')
today_birthdays = birthdays[(birthdays.day == today_day) & (birthdays.month == today_month)]

if len(today_birthdays) > 0:
    random_letter_template = random.choice(letters_list)
    print("There are Birthdays Today!")

    for row in today_birthdays.iterrows():
        name = row[1]['name']
        birthday_email = row[1]['email']

        with open(f'letter_templates/{random_letter_template}', 'r') as file:
            letter_message = file.read()
            birthday_message = letter_message.replace('[NAME]', name)

        email_subject = f"Happy Birthday {name}!"
        email_message = f"Subject:{email_subject}\n\n{birthday_message}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # makes connection secure
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_email,
                                msg=email_message)
















# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




