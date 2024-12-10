import smtplib

sender = "sender"
reciever = "reciever"
password = "password"
subject = "python email test"
body = "I wrote an email from prison: :0"

# header
message = f"""From: Sender Name {sender}
To: {reciever}
Subject: Reciever Name{subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,reciever,message)
    print("Email has been sent")
    
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
