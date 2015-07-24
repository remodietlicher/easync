# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiCreator/plotdialog.ui'
#
# Created: Fri Jul 24 16:13:11 2015
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


class Ui_PlotDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, plotWidget):
        plotWidget.setObjectName(_fromUtf8("plotWidget"))
        plotWidget.resize(740, 623)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(plotWidget.sizePolicy().hasHeightForWidth())
        plotWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtGui.QVBoxLayout(plotWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plotLayout = QtGui.QVBoxLayout()
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.verticalLayout_2.addLayout(self.plotLayout)

        self.retranslateUi(plotWidget)
        QtCore.QMetaObject.connectSlotsByName(plotWidget)

    def retranslateUi(self, plotWidget):
        plotWidget.setWindowTitle(_translate("plotWidget", "Dialog", None))

