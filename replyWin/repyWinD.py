# Form implementation generated from reading ui file 'replyWinD.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FormSendingEmail(object):
    def setupUi(self, FormSendingEmail):
        FormSendingEmail.setObjectName("FormSendingEmail")
        FormSendingEmail.resize(642, 562)
        self.btnSendEmail = QtWidgets.QPushButton(FormSendingEmail)
        self.btnSendEmail.setGeometry(QtCore.QRect(90, 20, 41, 41))
        self.btnSendEmail.setText("")
        self.btnSendEmail.setIconSize(QtCore.QSize(30, 30))
        self.btnSendEmail.setObjectName("btnSendEmail")
        self.label = QtWidgets.QLabel(FormSendingEmail)
        self.label.setGeometry(QtCore.QRect(20, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormSendingEmail)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FormSendingEmail)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEditTo = QtWidgets.QLineEdit(FormSendingEmail)
        self.lineEditTo.setGeometry(QtCore.QRect(90, 70, 511, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditTo.setFont(font)
        self.lineEditTo.setObjectName("lineEditTo")
        self.lineEditSubject = QtWidgets.QLineEdit(FormSendingEmail)
        self.lineEditSubject.setGeometry(QtCore.QRect(90, 160, 511, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditSubject.setFont(font)
        self.lineEditSubject.setObjectName("lineEditSubject")
        self.btnCancel = QtWidgets.QPushButton(FormSendingEmail)
        self.btnCancel.setGeometry(QtCore.QRect(140, 20, 41, 41))
        self.btnCancel.setText("")
        self.btnCancel.setIconSize(QtCore.QSize(30, 30))
        self.btnCancel.setObjectName("btnCancel")
        self.textEdit = QtWidgets.QTextEdit(FormSendingEmail)
        self.textEdit.setGeometry(QtCore.QRect(90, 190, 511, 361))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(FormSendingEmail)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEditCC = QtWidgets.QLineEdit(FormSendingEmail)
        self.lineEditCC.setGeometry(QtCore.QRect(90, 100, 511, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditCC.setFont(font)
        self.lineEditCC.setObjectName("lineEditCC")
        self.lineEditBCC = QtWidgets.QLineEdit(FormSendingEmail)
        self.lineEditBCC.setGeometry(QtCore.QRect(90, 130, 511, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditBCC.setFont(font)
        self.lineEditBCC.setText("")
        self.lineEditBCC.setObjectName("lineEditBCC")
        self.label_6 = QtWidgets.QLabel(FormSendingEmail)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(FormSendingEmail)
        QtCore.QMetaObject.connectSlotsByName(FormSendingEmail)
        FormSendingEmail.setTabOrder(self.lineEditTo, self.lineEditCC)
        FormSendingEmail.setTabOrder(self.lineEditCC, self.lineEditBCC)
        FormSendingEmail.setTabOrder(self.lineEditBCC, self.lineEditSubject)
        FormSendingEmail.setTabOrder(self.lineEditSubject, self.textEdit)
        FormSendingEmail.setTabOrder(self.textEdit, self.btnSendEmail)
        FormSendingEmail.setTabOrder(self.btnSendEmail, self.btnCancel)

    def retranslateUi(self, FormSendingEmail):
        _translate = QtCore.QCoreApplication.translate
        FormSendingEmail.setWindowTitle(_translate("FormSendingEmail", "Email senden"))
        self.label.setText(_translate("FormSendingEmail", "An:"))
        self.label_2.setText(_translate("FormSendingEmail", "Betreff:"))
        self.label_3.setText(_translate("FormSendingEmail", "Text:"))
        self.textEdit.setHtml(_translate("FormSendingEmail", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("FormSendingEmail", "cc:"))
        self.label_6.setText(_translate("FormSendingEmail", "bcc:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSendingEmail = QtWidgets.QWidget()
    ui = Ui_FormSendingEmail()
    ui.setupUi(FormSendingEmail)
    FormSendingEmail.show()
    sys.exit(app.exec())
