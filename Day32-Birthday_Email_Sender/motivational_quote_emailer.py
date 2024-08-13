import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""
SEND_TO_EMAIL = ""

#Check the day. It if matches today's weekday -> send a random quote

if dt.datetime.now().weekday() == 1:
    print("Yay it's Tuesday!")

    with open('quotes.txt') as file:
        quotes = [line.rstrip('\n') for line in file]

    random_quote = random.choice(quotes)
    email_subject = "Tuesday Motivation"
    email_message = f"Subject:{email_subject}\n\n{random_quote}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # makes connection secure
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=SEND_TO_EMAIL,
                            msg=email_message)