# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiCreator/configdialog.ui'
#
# Created: Fri Jul 24 10:56:25 2015
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


class Ui_ConfigDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(276, 636)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.legend_layout_2 = QtGui.QVBoxLayout()
        self.legend_layout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.legend_layout_2.setObjectName(_fromUtf8("legend_layout_2"))
        self.onefig_cb = QtGui.QCheckBox(Dialog)
        self.onefig_cb.setObjectName(_fromUtf8("onefig_cb"))
        self.legend_layout_2.addWidget(self.onefig_cb)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.legend_layout_2.addWidget(self.line)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.legend_layout_2.addWidget(self.label)
        self.plot_comb = QtGui.QComboBox(Dialog)
        self.plot_comb.setEnabled(True)
        self.plot_comb.setObjectName(_fromUtf8("plot_comb"))
        self.legend_layout_2.addWidget(self.plot_comb)
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.legend_layout_2.addWidget(self.line_3)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.legend_layout_2.addWidget(self.label_2)
        self.legend_list = QtGui.QListWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.legend_list.sizePolicy().hasHeightForWidth())
        self.legend_list.setSizePolicy(sizePolicy)
        self.legend_list.setObjectName(_fromUtf8("legend_list"))
        self.legend_layout_2.addWidget(self.legend_list)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.legendedit_field = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.legendedit_field.sizePolicy().hasHeightForWidth())
        self.legendedit_field.setSizePolicy(sizePolicy)
        self.legendedit_field.setObjectName(_fromUtf8("legendedit_field"))
        self.horizontalLayout_2.addWidget(self.legendedit_field)
        self.legendedit_button = QtGui.QPushButton(Dialog)
        self.legendedit_button.setObjectName(_fromUtf8("legendedit_button"))
        self.horizontalLayout_2.addWidget(self.legendedit_button)
        self.legend_layout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.legend_layout_2.addWidget(self.line_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.legend_layout_2.addWidget(self.label_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.yaxis_label = QtGui.QLabel(Dialog)
        self.yaxis_label.setObjectName(_fromUtf8("yaxis_label"))
        self.gridLayout_2.addWidget(self.yaxis_label, 1, 1, 1, 1)
        self.xlabel_field = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xlabel_field.sizePolicy().hasHeightForWidth())
        self.xlabel_field.setSizePolicy(sizePolicy)
        self.xlabel_field.setObjectName(_fromUtf8("xlabel_field"))
        self.gridLayout_2.addWidget(self.xlabel_field, 0, 0, 1, 1)
        self.title_field = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_field.sizePolicy().hasHeightForWidth())
        self.title_field.setSizePolicy(sizePolicy)
        self.title_field.setObjectName(_fromUtf8("title_field"))
        self.gridLayout_2.addWidget(self.title_field, 3, 0, 1, 1)
        self.xaxis_label = QtGui.QLabel(Dialog)
        self.xaxis_label.setObjectName(_fromUtf8("xaxis_label"))
        self.gridLayout_2.addWidget(self.xaxis_label, 0, 1, 1, 1)
        self.ylabel_field = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ylabel_field.sizePolicy().hasHeightForWidth())
        self.ylabel_field.setSizePolicy(sizePolicy)
        self.ylabel_field.setObjectName(_fromUtf8("ylabel_field"))
        self.gridLayout_2.addWidget(self.ylabel_field, 1, 0, 1, 1)
        self.title_label = QtGui.QLabel(Dialog)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.gridLayout_2.addWidget(self.title_label, 3, 1, 1, 1)
        self.zlabel_field = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zlabel_field.sizePolicy().hasHeightForWidth())
        self.zlabel_field.setSizePolicy(sizePolicy)
        self.zlabel_field.setObjectName(_fromUtf8("zlabel_field"))
        self.gridLayout_2.addWidget(self.zlabel_field, 2, 0, 1, 1)
        self.zaxis_label = QtGui.QLabel(Dialog)
        self.zaxis_label.setObjectName(_fromUtf8("zaxis_label"))
        self.gridLayout_2.addWidget(self.zaxis_label, 2, 1, 1, 1)
        self.titleaxis_button = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleaxis_button.sizePolicy().hasHeightForWidth())
        self.titleaxis_button.setSizePolicy(sizePolicy)
        self.titleaxis_button.setObjectName(_fromUtf8("titleaxis_button"))
        self.gridLayout_2.addWidget(self.titleaxis_button, 4, 0, 1, 1)
        self.legend_layout_2.addLayout(self.gridLayout_2)
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.legend_layout_2.addWidget(self.line_4)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.legend_layout_2.addWidget(self.label_4)
        self.activeax_comb = QtGui.QComboBox(Dialog)
        self.activeax_comb.setObjectName(_fromUtf8("activeax_comb"))
        self.legend_layout_2.addWidget(self.activeax_comb)
        self.verticalLayout_3.addLayout(self.legend_layout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.onefig_cb.setText(_translate("Dialog", "one figure", None))
        self.label.setText(_translate("Dialog", "Plot Type", None))
        self.label_2.setText(_translate("Dialog", "Edit Labels", None))
        self.legendedit_button.setText(_translate("Dialog", "edit", None))
        self.label_3.setText(_translate("Dialog", "Edit Title/Axes", None))
        self.yaxis_label.setText(_translate("Dialog", "y Axis", None))
        self.xaxis_label.setText(_translate("Dialog", "x Axis", None))
        self.title_label.setText(_translate("Dialog", "Title", None))
        self.zaxis_label.setText(_translate("Dialog", "z Axis", None))
        self.titleaxis_button.setText(_translate("Dialog", "edit", None))
        self.label_4.setText(_translate("Dialog", "Choose Active Axis", None))

