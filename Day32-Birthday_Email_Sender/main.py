##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas as pd
import os

MY_EMAIL = ""
MY_PASSWORD = ""

today = dt.datetime.now()
today_day = today.day
today_month = today.month

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
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_email,
                                msg=email_message)





