import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


login = 'login@gmail.com'
password = 'qwerty'
subject = 'Subject'
recipients = ['vasya@email.com', 'petya@email.com']
message = 'Hello, world!'
header = None

if __name__ == '__main__':

    class Emailer:

        def __init__(self, login, password):

            self.login = login
            self.password = password
            self.GMAIL_SMTP = "smtp.gmail.com"
            self.GMAIL_IMAP = "imap.gmail.com"

        def get_creterion(self, header):
            if header:
                criterion = f'HEADER Subject {header}'
            else:
                criterion = 'HEADER Subject ALL'
            return criterion

        def send_message(self, recipients, subject, message):

            msg = MIMEMultipart()
            msg['From'] = self.login
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(message))

            post_box = smtplib.SMTP(self.GMAIL_SMTP, 587)

            # identify ourselves to smtp gmail client
            post_box.ehlo()

            # secure our email with tls encryption
            post_box.starttls()

            # re-identify ourselves as an encrypted connection
            post_box.ehlo()
            post_box.login(self.login, self.password)
            post_box.sendmail(self.login, recipients, message)
            post_box.quit()

        def recieve_message(self, header):

            post_box = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
            post_box.login(self.login, self.password)
            post_box.list()
            post_box.select("inbox")
            criterion = self.get_creterion(header)
            result, data = post_box.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = post_box.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            post_box.logout()

            return email_message


emailer = Emailer(login, password)
emailer.send_message(recipients, subject, message)
emailer.recieve_message(header)
