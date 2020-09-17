# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mailsend.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Ui_SendMail(object):
    def setupUi(self, SendMail):
        SendMail.setObjectName("SendMail")
        SendMail.resize(565, 395)
        self.verticalLayoutWidget = QtWidgets.QWidget(SendMail)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 19, 281, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.froms = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.froms.setObjectName("from")
        self.verticalLayout.addWidget(self.froms)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.to = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.to.setObjectName("to")
        self.verticalLayout.addWidget(self.to)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.subject = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.subject.setObjectName("subject")
        self.verticalLayout.addWidget(self.subject)
        self.horizontalLayoutWidget = QtWidgets.QWidget(SendMail)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 60, 183, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.approveCheckbox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.approveCheckbox.setObjectName("approveCheckbox")
        self.horizontalLayout.addWidget(self.approveCheckbox)
        self.sendButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sendButton.setEnabled(False)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(SendMail)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 198, 541, 181))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.writeArea = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.writeArea.setObjectName("writeArea")
        self.horizontalLayout_2.addWidget(self.writeArea)

        self.retranslateUi(SendMail)
        QtCore.QMetaObject.connectSlotsByName(SendMail)

    def retranslateUi(self, SendMail):
        _translate = QtCore.QCoreApplication.translate
        SendMail.setWindowTitle(_translate("SendMail", "Send Mail"))
        self.label.setText(_translate("SendMail", "From"))
        self.label_2.setText(_translate("SendMail", "To"))
        self.label_3.setText(_translate("SendMail", "Subject"))
        self.approveCheckbox.setText(_translate("SendMail", "Approve"))
        self.sendButton.setText(_translate("SendMail", "Send"))

        self.approveCheckbox.clicked.connect(self.approve)
        self.sendButton.clicked.connect(self.send)
        self.mail = MIMEMultipart()

    def send(self):
        self.mail["From"] = self.froms.text()
        self.mail["To"] = self.to.text()
        self.mail["Subject"] = self.subject.text()
        message = self.writeArea.toPlainText()
        mssg = MIMEText(message, "plain")
        self.mail.attach(mssg)

        """
        
        You have to allow untrusted application for your gmail account. After send your email you can change your setting.
        
        """

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("your mail address", "Your password")
            mail.sendmail(self.mail["From"],self.mail["To"],self.mail.as_string())
            print("Mail başarıyla gönderildi.")
        except:
            print("Hata oluştu")

    def approve(self):
        self.sendButton.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SendMail = QtWidgets.QWidget()
    ui = Ui_SendMail()
    ui.setupUi(SendMail)
    SendMail.show()
    sys.exit(app.exec_())

