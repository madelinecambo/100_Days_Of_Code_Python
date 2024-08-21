import smtplib
from dotenv import load_dotenv
load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")
import os

class NotificationManager:

    def __init__(self):
        self.from_email = os.getenv("MyEmail2")
        self.to_email = os.getenv("MyEmail1")
        self.email_password = os.getenv("Email2AppPassword")

    def send_email(self, email_subject, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        Returns:
        None
        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """

        email_message = f"Subject:{email_subject}\n\n{message_body}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.email_password)
            connection.sendmail(from_addr=self.from_email,
                                to_addrs=self.to_email,
                                msg=email_message)
            print("Email Sent!")

