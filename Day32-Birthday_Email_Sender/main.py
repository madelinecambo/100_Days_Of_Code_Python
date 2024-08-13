import smtplib

my_email = "madelinecambo314@gmail.com"
password = "xyoikzxoajrtfesn"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # makes connection secure
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="madelineann11@gmail.com",
                        # add the \n\n to seperate the subject from the body of the email
                        msg="Subject:Hello\n\nThis is the body of my email")

