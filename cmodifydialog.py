# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiCreator/modifydialog.ui'
#
# Created: Fri Oct  9 13:24:10 2015
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
        self.copy_button = QtGui.QPushButton(self.optionsWidget)
        self.copy_button.setObjectName(_fromUtf8("copy_button"))
        self.horizontalLayout.addWidget(self.copy_button)
        self.change_button = QtGui.QPushButton(self.optionsWidget)
        self.change_button.setEnabled(False)
        self.change_button.setObjectName(_fromUtf8("change_button"))
        self.horizontalLayout.addWidget(self.change_button)
        self.apply_selection_cb = QtGui.QCheckBox(self.optionsWidget)
        self.apply_selection_cb.setObjectName(_fromUtf8("apply_selection_cb"))
        self.horizontalLayout.addWidget(self.apply_selection_cb)
        self.line = QtGui.QFrame(self.optionsWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.select_all_checkbox = QtGui.QCheckBox(self.optionsWidget)
        self.select_all_checkbox.setObjectName(_fromUtf8("select_all_checkbox"))
        self.horizontalLayout.addWidget(self.select_all_checkbox)
        self.line_2 = QtGui.QFrame(self.optionsWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.tmst_spinbox = QtGui.QSpinBox(self.optionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tmst_spinbox.sizePolicy().hasHeightForWidth())
        self.tmst_spinbox.setSizePolicy(sizePolicy)
        self.tmst_spinbox.setMaximum(9999999)
        self.tmst_spinbox.setObjectName(_fromUtf8("tmst_spinbox"))
        self.horizontalLayout.addWidget(self.tmst_spinbox)
        self.line_3 = QtGui.QFrame(self.optionsWidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.save_button = QtGui.QPushButton(self.optionsWidget)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.horizontalLayout.addWidget(self.save_button)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.optionsWidget)
        self.plotWidget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.plotWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.plotLayout = QtGui.QHBoxLayout()
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.horizontalLayout_2.addLayout(self.plotLayout)
        self.verticalLayout.addWidget(self.plotWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.copy_button.setText(_translate("Dialog", "Copy", None))
        self.change_button.setText(_translate("Dialog", "Change", None))
        self.apply_selection_cb.setText(_translate("Dialog", "Apply to Selection", None))
        self.select_all_checkbox.setText(_translate("Dialog", "select all", None))
        self.save_button.setText(_translate("Dialog", "Save", None))

