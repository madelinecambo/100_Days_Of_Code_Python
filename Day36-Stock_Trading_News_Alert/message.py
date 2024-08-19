import smtplib
import os
MY_EMAIL = os.getenv("MyEmail2")
MY_PASSWORD = os.getenv("Email2AppPassword")
# TO_EMAIL = os.getenv("MOM_EMAIL")
TO_EMAIL = os.getenv("MyEmail1")


def percent_difference(value1, value2):
    try:
        # Calculate the percent difference
        percent_diff = round(abs((value1 - value2) / value1 * 100))
        return percent_diff
    except ZeroDivisionError:
        # Handle the case where the denominator is zero
        return "Error: Division by zero"


def generate_header(symbol, stock_name, stock_percent_diff):
    first_line = f"Stock News Update {stock_name}: {symbol}{stock_percent_diff}%\n\n"
    return first_line


def send_email(headline, email_message):
    email_subject = headline
    email_message = f"Subject:{email_subject}\n\n{email_message}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=email_message)
    print("Email Sent!")
