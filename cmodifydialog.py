# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiCreator/modifydialog.ui'
#
# Created: Fri Jul 24 08:20:14 2015
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


class Ui_ModifyDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(872, 621)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.optionsWidget = QtGui.QWidget(Dialog)
        self.optionsWidget.setObjectName(_fromUtf8("optionsWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.optionsWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.use_for_all_timesteps_checkbox = QtGui.QCheckBox(self.optionsWidget)
        self.use_for_all_timesteps_checkbox.setObjectName(_fromUtf8("use_for_all_timesteps_checkbox"))
        self.horizontalLayout.addWidget(self.use_for_all_timesteps_checkbox)
        self.shift_all_checkbox = QtGui.QCheckBox(self.optionsWidget)
        self.shift_all_checkbox.setObjectName(_fromUtf8("shift_all_checkbox"))
        self.horizontalLayout.addWidget(self.shift_all_checkbox)
        self.tmst_spinbox = QtGui.QSpinBox(self.optionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tmst_spinbox.sizePolicy().hasHeightForWidth())
        self.tmst_spinbox.setSizePolicy(sizePolicy)
        self.tmst_spinbox.setObjectName(_fromUtf8("tmst_spinbox"))
        self.horizontalLayout.addWidget(self.tmst_spinbox)
        self.saveButton = QtGui.QPushButton(self.optionsWidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.optionsWidget)
        self.plotWidget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.plotWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.verticalLayout_3.addLayout(self.plotLayout)
        self.verticalLayout.addWidget(self.plotWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.use_for_all_timesteps_checkbox.setText(_translate("Dialog", "Use for all Timesteps", None))
        self.shift_all_checkbox.setText(_translate("Dialog", "Shift all", None))
        self.saveButton.setText(_translate("Dialog", "Save", None))

