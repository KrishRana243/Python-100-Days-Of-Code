import smtplib
myEmail = "YOUR EMAIL"
appPassword = "YOUR PASSWORD"

with smtplib.SMTP("smtp.gmail.com") as connection:         # location
    connection.starttls()                                  # makes connection secure
    connection.login(user=myEmail,password=appPassword)
    connection.sendmail(
        from_addr=myEmail,
        to_addrs="krishranaxi@gmail.com",
        msg="Subject:Day 32\n\nHello this is my code!"
    )

'''The smtplib module is a built-in Python library used to send emails 
   via the Simple Mail Transfer Protocol (SMTP). It handles the low-level connection to 
   mail servers and manages the transmission of email messages from your code.'''
