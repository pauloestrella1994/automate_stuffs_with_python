import smtplib
from prettyconf import config
from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


class SendEmail:

    def __init__(self):
        self.conn = smtplib.SMTP('smtp.gmail.com', 587)
        self.email = config('EMAIL_USER')
        self.password = config('EMAIL_PASSWORD')
        self.receiver_email = input('Type email that will receive the email data: ')
    
    def attach_template_to_email(self):
        with open('regular_expressions/project/template_email.html', 'r') as html:
            template = Template(html.read())
            date = datetime.now().strftime('%d/%m/%Y')
            body_msg = template.substitute(name='Paulo', datetime=date)
        
        self.msg = MIMEMultipart()
        self.msg['from'] = 'Paulo'
        self.msg['to'] = self.receiver_email
        self.msg['subject'] = 'CSV file attached...'

        body = MIMEText(body_msg, 'html')
        self.msg.attach(body)

    def attach_csv_file_to_email(self):
        with open('email_phone.csv', 'rb') as csv_file:
            self.msg.attach(MIMEApplication(csv_file.read(), name='emails_and_phones.csv'))

    def send_email(self):
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.login(self.email, self.password)
        self.conn.send_message(self.msg)
        self.conn.quit()

mail_test = SendEmail()
mail_test.attach_template_to_email()
mail_test.attach_csv_file_to_email()
mail_test.send_email()