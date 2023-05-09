import collections
import email
import imaplib
import re
import imap_tools
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPalette, QColor, QFont
from PyQt6.QtWidgets import QListWidgetItem, QDialog, QPushButton
from imap_tools import MailBox, AND
from RepeatTimer import *

from replyWin.ReplyWinUse import *
from PassWin.PassWinUse import *
from MainWin.MainWinD import *
from SendWin.SendWinUse import *
from Mail import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mailList = []
        self.sendetMailList = []
        self.unseenMailList = []
        self.uidWidget = []
        self.uidSendetWidget = []
        self.inboxbool = True
        self.sendetbool = False
        self.inboxUnseenbool = False
        self.refreshMailLists()
        self.btnSendEmail.setIcon(QIcon("Icons\\sendEmail.png"))
        self.setWindowIcon(QIcon("Icons\\emailIcon.png"))
        self.btnRefresh.setIcon(QIcon("Icons\\refresh.png"))
        self.btnUnseen.setIcon(QIcon("Icons\\unseen.png"))
        self.btnSendet.setIcon(QIcon("Icons\\sendet.png"))
        self.btnDelete.setIcon(QIcon("Icons\\del.png"))
        self.btnReply.setIcon(QIcon("Icons\\reply.png"))
        self.btnHandOff.setIcon(QIcon("Icons\\handoff.png"))
        self.setWindowTitle("Email Client")
        self.btnSendEmail.clicked.connect(self.showSendEmailWin)
        self.btnRefresh.clicked.connect(self.updateEmailWidget)
        self.btnUnseen.clicked.connect(self.updateEmailWidgetUnseen)
        self.btnSendet.clicked.connect(self.showSendetMails)
        self.btnDelete.clicked.connect(self.delEmail)
        self.listWidget.itemClicked.connect(self.showMail)
        self.btnReply.clicked.connect(self.replyMail)
        self.btnHandOff.clicked.connect(self.handoffMail)
        self.text = ""
        self.show()
        self.downloadMailsLoop = RepeatTimer(5, self.refreshMailLists)
        self.downloadMailsLoop.start()
        self.updateEmailWidget()


    def refreshMailLists(self):
        self.threadMailList = []
        self.threadSendetMailList = []
        self.uids = []
        self.sendetuids = []
        with MailBox('imap.gmx.net').login("TestEmailClient@gmx.at", "asQW1234") as self.mailbox:
            for msg in self.mailbox.fetch(reverse=True, mark_seen=False):
                self.uids.append(msg.uid)
                self.threadMailList.append(
                    Mail(msg.uid, msg.date.strftime('%d.%m.%Y %H:%M:%S'), msg.from_, msg.to, msg.cc, msg.bcc,
                         msg.subject, msg.text, msg.flags))
        with MailBox('imap.gmx.net').login("TestEmailClient@gmx.at", "asQW1234") as self.mailbox:
            self.mailbox.folder.set("Gesendet")
            for msg in self.mailbox.fetch(reverse=True):
                self.sendetuids.append(msg.uid)
                self.threadSendetMailList.append(
                    Mail(msg.uid, msg.date.strftime('%d.%m.%Y %H:%M:%S'), msg.from_, msg.to, msg.cc, msg.bcc,
                         msg.subject, msg.text,msg.flags))

        if self.uids == self.uidWidget:
            self.labelMainWin.setText(f"Letze Aktualisierung: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
        else:
            self.mailList = self.threadMailList
            if self.inboxbool == True:
                self.updateEmailWidget()

            elif self.inboxUnseenbool == True:
                self.updateEmailWidgetUnseen()


        if self.sendetuids == self.uidSendetWidget:
            self.labelMainWin.setText(f"Letze Aktualisierung: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
        else:
            self.sendetMailList = self.threadSendetMailList
            if self.sendetbool == True:
                self.showSendetMails()


    def handoffMail(self):
        list = self.listWidget.selectedItems()
        if len(list) > 0:
            index = self.listWidget.currentIndex().row()
            if self.inboxUnseenbool == True:
                mail = self.mailList[index]
                self.replyWin = ReplyEmailWin(mail, False,"handoff.png")
                self.replyWin.show()
            elif self.inboxbool == True:
                mail = self.mailList[index]
                self.replyWin = ReplyEmailWin(mail, False,"handoff.png")
                self.replyWin.show()

    def replyMail(self):
        list = self.listWidget.selectedItems()
        if len(list) > 0:
            index = self.listWidget.currentIndex().row()
            if self.inboxUnseenbool == True:
                mail = self.mailList[index]
                self.replyWin = ReplyEmailWin(mail,True,"reply.png")
                self.replyWin.show()
            elif self.inboxbool == True:
                mail = self.mailList[index]
                self.replyWin = ReplyEmailWin(mail,True,"reply.png")
                self.replyWin.show()

    def delEmail(self):
        list = self.listWidget.selectedItems()
        if len(list) > 0:
            index = self.listWidget.currentIndex().row()
            if self.sendetbool == True:
                mail = self.sendetMailList[index]
                mailServer = imaplib.IMAP4_SSL("imap.gmx.net")
                mailServer.login("TestEmailClient@gmx.at", "asQW1234")
                mailServer.select(mailbox="Gesendet", readonly=False)
                mailServer.uid('store', mail.uid, '+FLAGS', "\\Deleted")
                mailServer.close()
                del self.sendetMailList[index]
                self.showSendetMails()

            elif self.inboxbool == True:
                mail = self.mailList[index]
                mailServer = imaplib.IMAP4_SSL("imap.gmx.net")
                mailServer.login("TestEmailClient@gmx.at", "asQW1234")
                mailServer.select(mailbox="INBOX", readonly=False)
                mailServer.uid('store', mail.uid, '+FLAGS', "\\Deleted")
                mailServer.close()
                del self.mailList[index]
                self.updateEmailWidget()

            elif self.inboxUnseenbool == True:
                mail = self.mailList[index]
                mailServer = imaplib.IMAP4_SSL("imap.gmx.net")
                mailServer.login("TestEmailClient@gmx.at", "asQW1234")
                mailServer.select(mailbox="INBOX", readonly=False)
                mailServer.uid('store', mail.uid, '+FLAGS', "\\Deleted")
                mailServer.close()
                del self.mailList[index]
                self.updateEmailWidgetUnseen()

    def showSendetMails(self):
        self.label.setText("Gesendete Emails:")
        self.uidSendetWidget.clear()
        #self.textBrowser.clear()
        self.sendetbool = True
        self.inboxUnseenbool = False
        self.inboxbool = False
        self.listWidget.clear()
        for mail in self.sendetMailList:
            self.uidSendetWidget.append(mail.uid)
            self.listWidget.addItem(mail.returnStringForListWidget())
        self.label.setText(self.unseenEmailNumber(len(self.sendetMailList), "Gesendete Emails:", "", ""))
        self.labelMainWin.setText(f"Letze Aktualisierung: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

    def updateEmailWidgetUnseen(self):
        self.label.setText("Ungelesene Emails:")
        self.inboxUnseenbool = True
        self.inboxbool = False
        self.sendetbool = False
        self.unseenMailList.clear()
        self.listWidget.clear()
        x = 0
        for mail in self.mailList:

            if "Seen" in mail.flag.__str__():
                pass
            else:
                self.unseenMailList.append(mail)
                new = QListWidgetItem(mail.returnStringForListWidget())
                new.setForeground(QColor("#ff0000"))
                self.listWidget.addItem(new)
                x += 1
        self.label.setText(self.unseenEmailNumber(x, "Ungelesene Emails:", "", ""))
        self.labelMainWin.setText(f"Letze Aktualisierung: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

    def showMail(self):
        self.textBrowser.clear()
        list = self.listWidget.selectedItems()
        if len(list) > 0:
            index = self.listWidget.currentIndex().row()
            if self.sendetbool == True:
                mail = self.sendetMailList[index]
                self.textBrowser.setText(mail.returnStringforTextBrowserInbox())
            elif self.inboxbool == True:
                mail = self.mailList[index]
                self.textBrowser.setText(mail.returnStringforTextBrowserInbox())

                if "Seen" in mail.flag.__str__():
                    pass
                else:
                    mail.flag = '(\\Seen)'
                    # Add Seen Flag to Mail
                    mailTest = imaplib.IMAP4_SSL("imap.gmx.net")
                    mailTest.login("TestEmailClient@gmx.at", "asQW1234")
                    mailTest.select(mailbox="INBOX",readonly=False)
                    mailTest.uid('store', mail.uid, '+FLAGS', '(\\Seen)')
                    mailTest.close()
            elif self.inboxUnseenbool == True:
                mail = self.unseenMailList[index]
                self.textBrowser.setText(mail.returnStringforTextBrowserInbox())

                if "Seen" in mail.flag.__str__():
                    pass
                else:
                    mail.flag = '(\\Seen)'
                    # Add Seen Flag to Mail
                    mailTest = imaplib.IMAP4_SSL("imap.gmx.net")
                    mailTest.login("TestEmailClient@gmx.at", "asQW1234")
                    mailTest.select(mailbox="INBOX", readonly=False)
                    mailTest.uid('store', mail.uid, '+FLAGS', '(\\Seen)')
                    mailTest.close()


    def showSendEmailWin(self):
        #self.sendetbool = False
        self.sendEmailWin = SendEmailWin()
        self.sendEmailWin.show()

    def updateEmailWidget(self):
        self.uidWidget.clear()
        self.label.setText("Posteingang:")
        self.sendetbool = False
        self.inboxUnseenbool = False
        self.inboxbool = True
        self.listWidget.clear()
        self.x = 0
        for mail in self.mailList:
            self.uidWidget.append(mail.uid)
            if "Seen" in mail.flag.__str__():
                self.listWidget.addItem(mail.returnStringForListWidget())
            else:
                new = QListWidgetItem(mail.returnStringForListWidget())
                new.setForeground(QColor("#ff0000"))
                self.listWidget.addItem(new)
                self.x += 1
        self.label.setText(self.unseenEmailNumber(self.x, "Posteingang:", "neue Email", "neue Emails"))
        self.labelMainWin.setText(f"Letze Aktualisierung: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.downloadMailsLoop.cancel()

    def unseenEmailNumber(self,x,text,text2,text3):
        if x == 0:
            return ""
        elif x == 1:
            return f"{text} ({x}) {text2}"
        elif x > 1:
            return f"{text} ({x}) {text3}"


