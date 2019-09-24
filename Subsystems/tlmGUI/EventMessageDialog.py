# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EventMessageDialog.ui'
#
# Created: Thu Mar 26 11:45:17 2015
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

class Ui_EventMessageDialog(object):
    def setupUi(self, EventMessageDialog):
        EventMessageDialog.setObjectName("EventMessageDialog")
        EventMessageDialog.resize(591, 277)
        self.verticalLayout = QtWidgets.QVBoxLayout(EventMessageDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(EventMessageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(91, 17))
        self.label_2.setMaximumSize(QtCore.QSize(91, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.sequenceCount = QtWidgets.QTextBrowser(EventMessageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sequenceCount.sizePolicy().hasHeightForWidth())
        self.sequenceCount.setSizePolicy(sizePolicy)
        self.sequenceCount.setMinimumSize(QtCore.QSize(81, 31))
        self.sequenceCount.setMaximumSize(QtCore.QSize(81, 31))
        self.sequenceCount.setObjectName("sequenceCount")
        self.horizontalLayout.addWidget(self.sequenceCount)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(EventMessageDialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label = QtWidgets.QLabel(EventMessageDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(EventMessageDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(81, 31, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(EventMessageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(91, 32))
        self.buttonBox.setMaximumSize(QtCore.QSize(91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.eventOutput = QtWidgets.QTextBrowser(EventMessageDialog)
        self.eventOutput.setObjectName("eventOutput")
        self.verticalLayout.addWidget(self.eventOutput)

        self.retranslateUi(EventMessageDialog)
        self.buttonBox.accepted.connect(EventMessageDialog.accept)
        self.buttonBox.rejected.connect(EventMessageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EventMessageDialog)

    def retranslateUi(self, EventMessageDialog):
        EventMessageDialog.setWindowTitle(_translate("EventMessageDialog", "Event Messages", None))
        self.label_2.setText(_translate("EventMessageDialog", "Packet Count", None))
        self.label.setText(_translate("EventMessageDialog", "Events", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EventMessageDialog = QtWidgets.QDialog()
    ui = Ui_EventMessageDialog()
    ui.setupUi(EventMessageDialog)
    EventMessageDialog.show()
    sys.exit(app.exec_())

