import smtplib, ssl

smtp_server = "mail.example.de"
port = 587  # 465  # For SSL
password = input("Type your password and press enter: ")
sender_email = 'superlists@example.com'
receiver_email = 'foo@bar.baz'
message = """\
Subject: hi there

This message is sent from python.
"""

# Create a secure SSL context
context = ssl.create_default_context()

# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
