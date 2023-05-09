from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox
from SendWin.ReadAndWriteSignature import *

from SendingProcess.SendingProcess import *

from SendWin.SendWinD import *

class SendEmailWin(QtWidgets.QMainWindow, Ui_FormSendingEmail):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("Icons\\sendEmail.png"))
        self.btnSendEmail.setIcon(QIcon("Icons\\send.png"))
        self.btnCancel.setIcon(QIcon("Icons\\cancel.png"))
        self.btnSignatur.setIcon(QIcon("Icons\\Signatur.png"))
        self.btnMin.setIcon(QIcon("Icons\\Min.png"))
        self.btnDel.setIcon(QIcon("Icons\\del.png"))
        self.btnSave.setIcon(QIcon("Icons\\save.png"))
        self.btnCancel.clicked.connect(self.close)
        self.btnSendEmail.clicked.connect(self.sendEmail)
        self.signaturebool = True
        self.btnSignatur.clicked.connect(self.showSignatureOptions)
        self.hideSignatureOptions()
        self.btnMin.clicked.connect(self.hideSignatureOptions)
        self.btnSave.clicked.connect(self.saveSiganture)
        self.btnDel.clicked.connect(self.delSignature)
        self.reader = ReadSignature()
        self.textEditSignatur.setText(self.reader.returnSomething())
        if self.textEditSignatur.toPlainText() != "":
            self.labelSigaktiv.setText("Email Signatur aktiviert.")
        else:
            self.labelSigaktiv.hide()

    def saveSiganture(self):
        write = WriteSignature(self.textEditSignatur.toPlainText())

    def delSignature(self):
        self.textEditSignatur.clear()
        self.saveSiganture()

    def hideSignatureOptions(self):
        self.signaturebool = True
        self.textEditSignatur.hide()
        self.label_4.hide()
        self.btnMin.hide()
        self.btnDel.hide()
        self.btnSave.hide()
        if self.textEditSignatur.toPlainText() != "":
            self.labelSigaktiv.show()

    def showSignatureOptions(self):
        if self.signaturebool == True:
            self.textEditSignatur.show()
            self.label_4.show()
            self.btnMin.show()
            self.btnDel.show()
            self.btnSave.show()
            self.labelSigaktiv.hide()
            self.textEditSignatur.setFocus()
            self.signaturebool = False
        elif self.signaturebool == False:
            self.hideSignatureOptions()

    def sendEmail(self):
        try:
            self.sendMail = Sending(self.textEdit.toPlainText(),self.lineEditTo.text(),self.lineEditSubject.text(),self.textEditSignatur.toPlainText(),self.lineEditCC.text(),self.lineEditBCC.text())
            self.sendMail.sendEmail()
            self.close()

        except:
            self.msg = QMessageBox()
            self.msg.setWindowIcon(QIcon("Icons\\caution.png"))
            self.msg.setText("Die Email konnte nicht gesendet werden!")
            self.msg.setWindowTitle("Fehler aufgetreten")
            self.msg.show()
            self.close()



