import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


login = 'dnovik01@googlemail.com'
password = '89265953872'
subject = 'Subject'
recipients = ['nelden@yandex.ru', 'dnovik@grundfos.com']
message = 'Hello, world!'
header = None


class Emailer:



    def __init__(self, login, password, subject, recipients, message, header):

        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"

    def get_creterion(header):
        if header:
            criterion = f'HEADER Subject {header}'
        else:
            criterion = 'HEADER Subject ALL'
        return criterion

    def send_message(self):

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)

        # identify ourselves to smtp gmail client
        ms.ehlo()

        # secure our email with tls encryption
        ms.starttls()

        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, self.message)
        ms.quit()

    def recieve_message(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = get_creterion(self.header)
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


emailer = Emailer(login, password, subject, recipients, message, header)

emailer.send_message()
emailer.recieve_message()