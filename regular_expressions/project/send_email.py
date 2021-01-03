import smtplib


class SendEmail:

    def __init__(self):
        self.conn = smtplib.SMTP('smtp.gmail.com', 587)
        self.email = input('Type your email: ')
        self.password = input('Type your password: ')
        self.receiver_email = input('Type email that will receive the email data: ')

    def send_email(self):
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.login(self.email, self.password)
        self.conn.sendmail(self.email, self.receiver_email, 'Subject: Testing\n\n <h1>Testing</h1>')
        self.conn.quit()

mail_test = SendEmail()
mail_test.send_email()