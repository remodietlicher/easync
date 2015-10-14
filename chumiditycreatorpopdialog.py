# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiCreator/humiditycreatorpopdialog.ui'
#
# Created: Mon Oct 12 12:10:03 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_HumidityCreatorPopDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(556, 146)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.dataname_field = QtGui.QLineEdit(Dialog)
        self.dataname_field.setGeometry(QtCore.QRect(10, 40, 411, 27))
        self.dataname_field.setObjectName(_fromUtf8("dataname_field"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.open_button = QtGui.QPushButton(Dialog)
        self.open_button.setGeometry(QtCore.QRect(440, 40, 99, 27))
        self.open_button.setObjectName(_fromUtf8("open_button"))
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(330, 100, 99, 27))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.load_button = QtGui.QPushButton(Dialog)
        self.load_button.setGeometry(QtCore.QRect(440, 100, 99, 27))
        self.load_button.setObjectName(_fromUtf8("load_button"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Open data file for pressure levels", None))
        self.open_button.setText(_translate("Dialog", "open", None))
        self.cancel_button.setText(_translate("Dialog", "cancel", None))
        self.load_button.setText(_translate("Dialog", "load", None))

