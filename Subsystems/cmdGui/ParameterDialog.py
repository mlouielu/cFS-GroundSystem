# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParameterDialog.ui'
#
# Created: Wed Mar 25 12:38:59 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(786, 466)
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(330, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_instructions = QtWidgets.QLabel(Dialog)
        self.label_instructions.setGeometry(QtCore.QRect(120, 90, 551, 31))
        self.label_instructions.setAlignment(QtCore.Qt.AlignCenter)
        self.label_instructions.setObjectName("label_instructions")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(670, 430, 101, 31))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.status_box = QtWidgets.QTextBrowser(Dialog)
        self.status_box.setGeometry(QtCore.QRect(480, 30, 201, 41))
        self.status_box.setAutoFillBackground(False)
        self.status_box.setObjectName("status_box")
        self.label_param_title_2 = QtWidgets.QLabel(Dialog)
        self.label_param_title_2.setGeometry(QtCore.QRect(480, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_param_title_2.setFont(font)
        self.label_param_title_2.setObjectName("label_param_title_2")
        self.SendButton_1 = QtWidgets.QPushButton(Dialog)
        self.SendButton_1.setGeometry(QtCore.QRect(690, 40, 71, 27))
        self.SendButton_1.setObjectName("SendButton_1")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(260, 10, 81, 20))
        self.label_5.setObjectName("label_5")
        self.subSystemCommandPageLabel = QtWidgets.QLabel(Dialog)
        self.subSystemCommandPageLabel.setGeometry(QtCore.QRect(30, 10, 91, 17))
        self.subSystemCommandPageLabel.setObjectName("subSystemCommandPageLabel")
        self.subSystemTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.subSystemTextBrowser.setGeometry(QtCore.QRect(30, 30, 221, 41))
        self.subSystemTextBrowser.setObjectName("subSystemTextBrowser")
        self.commandAddressTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.commandAddressTextBrowser.setGeometry(QtCore.QRect(260, 30, 211, 41))
        self.commandAddressTextBrowser.setObjectName("commandAddressTextBrowser")
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 120, 741, 301))
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setBaseSize(QtCore.QSize(0, 500))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 724, 1000))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 1000))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.input_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_2.setGeometry(QtCore.QRect(440, 80, 271, 41))
        self.input_2.setObjectName("input_2")
        self.descrip_1 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_1.setGeometry(QtCore.QRect(150, 30, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_1.setFont(font)
        self.descrip_1.setObjectName("descrip_1")
        self.label_input_title_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_input_title_2.setGeometry(QtCore.QRect(440, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_input_title_2.setFont(font)
        self.label_input_title_2.setObjectName("label_input_title_2")
        self.input_5 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_5.setGeometry(QtCore.QRect(440, 230, 271, 41))
        self.input_5.setObjectName("input_5")
        self.label_param_title_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_param_title_3.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_param_title_3.setFont(font)
        self.label_param_title_3.setObjectName("label_param_title_3")
        self.label_descrip_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_descrip_2.setGeometry(QtCore.QRect(150, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_descrip_2.setFont(font)
        self.label_descrip_2.setObjectName("label_descrip_2")
        self.input_1 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_1.setGeometry(QtCore.QRect(440, 30, 271, 41))
        self.input_1.setObjectName("input_1")
        self.paramName_1 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_1.setGeometry(QtCore.QRect(10, 30, 131, 41))
        self.paramName_1.setObjectName("paramName_1")
        self.input_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_3.setGeometry(QtCore.QRect(440, 130, 271, 41))
        self.input_3.setObjectName("input_3")
        self.input_4 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_4.setGeometry(QtCore.QRect(440, 180, 271, 41))
        self.input_4.setObjectName("input_4")
        self.input_6 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_6.setGeometry(QtCore.QRect(440, 280, 271, 41))
        self.input_6.setObjectName("input_6")
        self.input_7 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_7.setGeometry(QtCore.QRect(440, 330, 271, 41))
        self.input_7.setObjectName("input_7")
        self.input_8 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_8.setGeometry(QtCore.QRect(440, 380, 271, 41))
        self.input_8.setObjectName("input_8")
        self.input_9 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_9.setGeometry(QtCore.QRect(440, 430, 271, 41))
        self.input_9.setObjectName("input_9")
        self.paramName_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_2.setGeometry(QtCore.QRect(10, 80, 131, 41))
        self.paramName_2.setObjectName("paramName_2")
        self.descrip_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_2.setGeometry(QtCore.QRect(150, 80, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_2.setFont(font)
        self.descrip_2.setObjectName("descrip_2")
        self.descrip_3 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_3.setGeometry(QtCore.QRect(150, 130, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_3.setFont(font)
        self.descrip_3.setObjectName("descrip_3")
        self.paramName_3 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_3.setGeometry(QtCore.QRect(10, 130, 131, 41))
        self.paramName_3.setObjectName("paramName_3")
        self.paramName_4 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_4.setGeometry(QtCore.QRect(10, 180, 131, 41))
        self.paramName_4.setObjectName("paramName_4")
        self.descrip_4 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_4.setGeometry(QtCore.QRect(150, 180, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_4.setFont(font)
        self.descrip_4.setObjectName("descrip_4")
        self.descrip_5 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_5.setGeometry(QtCore.QRect(150, 230, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_5.setFont(font)
        self.descrip_5.setObjectName("descrip_5")
        self.paramName_5 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_5.setGeometry(QtCore.QRect(10, 230, 131, 41))
        self.paramName_5.setObjectName("paramName_5")
        self.descrip_6 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_6.setGeometry(QtCore.QRect(150, 280, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_6.setFont(font)
        self.descrip_6.setObjectName("descrip_6")
        self.paramName_6 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_6.setGeometry(QtCore.QRect(10, 280, 131, 41))
        self.paramName_6.setObjectName("paramName_6")
        self.descrip_7 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_7.setGeometry(QtCore.QRect(150, 330, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_7.setFont(font)
        self.descrip_7.setObjectName("descrip_7")
        self.paramName_7 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_7.setGeometry(QtCore.QRect(10, 330, 131, 41))
        self.paramName_7.setObjectName("paramName_7")
        self.paramName_8 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_8.setGeometry(QtCore.QRect(10, 380, 131, 41))
        self.paramName_8.setObjectName("paramName_8")
        self.descrip_8 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_8.setGeometry(QtCore.QRect(150, 380, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_8.setFont(font)
        self.descrip_8.setObjectName("descrip_8")
        self.paramName_9 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_9.setGeometry(QtCore.QRect(10, 430, 131, 41))
        self.paramName_9.setObjectName("paramName_9")
        self.descrip_9 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_9.setGeometry(QtCore.QRect(150, 430, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_9.setFont(font)
        self.descrip_9.setObjectName("descrip_9")
        self.descrip_10 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.descrip_10.setGeometry(QtCore.QRect(150, 480, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.descrip_10.setFont(font)
        self.descrip_10.setObjectName("descrip_10")
        self.paramName_10 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.paramName_10.setGeometry(QtCore.QRect(10, 480, 131, 41))
        self.paramName_10.setObjectName("paramName_10")
        self.input_10 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.input_10.setGeometry(QtCore.QRect(440, 480, 271, 41))
        self.input_10.setObjectName("input_10")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Dialog)
        self.buttonBox.clicked[QAbstractButton].connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_title.setText(_translate("Dialog", "Parameters", None))
        self.label_instructions.setText(_translate("Dialog", "Please enter the following parameters then click \'Send\':", None))
        self.label_param_title_2.setText(_translate("Dialog", "Status:", None))
        self.SendButton_1.setText(_translate("Dialog", "Send", None))
        self.label_5.setText(_translate("Dialog", "Command:", None))
        self.subSystemCommandPageLabel.setText(_translate("Dialog", "Subsystem:", None))
        self.label_input_title_2.setText(_translate("Dialog", "Input", None))
        self.label_param_title_3.setText(_translate("Dialog", "Parameter", None))
        self.label_descrip_2.setText(_translate("Dialog", "Description", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

