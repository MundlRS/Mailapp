from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox
from SendWin.ReadAndWriteSignature import *

from SendingProcess.SendingProcess import *

from replyWin.repyWinD import *

class ReplyEmailWin(QtWidgets.QMainWindow, Ui_FormSendingEmail):
    def __init__(self,mail,bool,png):
        super().__init__()
        self.setupUi(self)
        self.mail = mail
        self.bool = bool
        self.setWindowIcon(QIcon(f"Icons\\{png}"))
        self.btnSendEmail.setIcon(QIcon("Icons\\send.png"))
        self.btnCancel.setIcon(QIcon("Icons\\cancel.png"))
        self.btnCancel.clicked.connect(self.close)
        self.btnSendEmail.clicked.connect(self.sendEmail)
        self.reader = ReadSignature()
        self.setWindowTitle("Email weiterleiten")
        if self.bool == True:
            self.lineEditTo.setText(', '.join(self.mail.to))
            self.lineEditCC.setText(', '.join(self.mail.cc))
            self.lineEditBCC.setText(', '.join(self.mail.bcc))
            self.setWindowTitle("Email antworten")
        self.lineEditSubject.setText(f"AW: {self.mail.subject}")
        self.textEdit.setText(self.mail.originallyMessage())

    def sendEmail(self):
        try:
            self.sendMail = Sending(self.textEdit.toPlainText(),self.lineEditTo.text(),self.lineEditSubject.text(),"",self.lineEditCC.text(),self.lineEditBCC.text())
            self.sendMail.sendEmail()
            self.close()

        except:
            self.msg = QMessageBox()
            self.msg.setWindowIcon(QIcon("SendWin\\caution.png"))
            self.msg.setText("Die Email konnte nicht gesendet werden!")
            self.msg.setWindowTitle("Fehler aufgetreten")
            self.msg.show()
            self.close()



