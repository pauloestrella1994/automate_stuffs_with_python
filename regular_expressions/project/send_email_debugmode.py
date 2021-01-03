import smtplib
from email.message import EmailMessage
from prettyconf import config

EMAIL_ADDRESS = config('EMAIL_USER')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'Just a test'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('This is the body of my test, sending email to myself!')

with smtplib.SMTP('localhost', 1025) as smtp:
    smtp.send_message(msg)