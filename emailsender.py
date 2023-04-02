import smtplib, ssl
from email.message import EmailMessage

def sendEmail(person):
    port = 465  # For SSL
    smtp_server = "smtp.gmx.com"

    #read the email and password
    sender_email = ""
    password = ""
    with open('credentials.txt', 'r') as file:
        sender_email = file.readline().strip('\n')
        password = file.readline().strip('\n')

    msg = EmailMessage()
    msg.set_content("Hello " + person.name + "!")
    msg['Subject'] = "Hello from Python Gmail!"
    msg['From'] = sender_email
    msg['To'] = person.email

    #context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=person.email)
        print("Send an email to " + person.name)

sendEmail({})
