import smtplib
from prettyconf import config

EMAIL_ADDRESS = config('EMAIL_USER')
EMAIL_PASSWORD = config('EMAIL_PASSWORD')

with smtplib.SMTP('localhost', 1025) as smtp:
    subject = 'Just a test'
    body = 'This is the body of my test'

    msg = f'Subject: {subject}\n\n {body}'

    smtp.sendmail(EMAIL_ADDRESS, 'example@gmail.com', msg)