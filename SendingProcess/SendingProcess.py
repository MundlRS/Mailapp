import imaplib
import smtplib
from datetime import datetime, time
from datetime import date
from email import utils
from email.mime.text import MIMEText
import pytz

import imap_tools
import pytz
from imap_tools import MailBox


class Sending:
    def __init__(self,text,to,  subject,signatur,cc,bcc ):
        self.text = text
        self.to = to
        self.subject = subject
        self.signatur = signatur
        self.cc = cc
        self.bcc = bcc

    def sendEmail(self):
        user = "TestEmailClient@gmx.at"
        pwd = "asQW1234"
        text = f"{self.text}\n\n{self.signatur}"
        tz = pytz.timezone("America/New_York")

        message = MIMEText(text, 'plain')
        message['Subject'] = self.subject
        message['From'] = user
        message['To'] = self.to
        message['CC'] = self.cc
        message['BCC'] = self.bcc

        with smtplib.SMTP("mail.gmx.net", 587) as s:
            s.connect("mail.gmx.net", 587)
            s.starttls()
            s.login(user, pwd)
            to = self.to.split(",")
            to += self.cc.split(",") + self.bcc.split(",")
            s.sendmail(user, to, message.as_string())
            s.quit()

        with MailBox('imap.gmx.net').login("TestEmailClient@gmx.at", "asQW1234") as mailbox:
            mailbox.append(message.as_bytes(), 'Gesendet', dt=datetime.now(tz=tz), flag_set=[imap_tools.MailMessageFlags.SEEN])


