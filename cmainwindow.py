# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiCreator/mainwindow.ui'
#
# Created: Thu Jul  9 13:40:40 2015
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


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(692, 518)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 631, 29))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filename_field = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.filename_field.setObjectName(_fromUtf8("filename_field"))
        self.horizontalLayout.addWidget(self.filename_field)
        self.file_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.file_button.setObjectName(_fromUtf8("file_button"))
        self.horizontalLayout.addWidget(self.file_button)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 100, 631, 231))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.var2d_list = QtGui.QListWidget(self.gridLayoutWidget)
        self.var2d_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.var2d_list.setObjectName(_fromUtf8("var2d_list"))
        self.gridLayout.addWidget(self.var2d_list, 1, 1, 1, 1)
        self.var1d_list = QtGui.QListWidget(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.var1d_list.sizePolicy().hasHeightForWidth())
        self.var1d_list.setSizePolicy(sizePolicy)
        self.var1d_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.var1d_list.setObjectName(_fromUtf8("var1d_list"))
        self.gridLayout.addWidget(self.var1d_list, 1, 0, 1, 1)
        self.var3d_list = QtGui.QListWidget(self.gridLayoutWidget)
        self.var3d_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.var3d_list.setObjectName(_fromUtf8("var3d_list"))
        self.gridLayout.addWidget(self.var3d_list, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.plot_button = QtGui.QPushButton(self.centralWidget)
        self.plot_button.setGeometry(QtCore.QRect(300, 480, 99, 27))
        self.plot_button.setObjectName(_fromUtf8("plot_button"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 380, 631, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.specialvar_field = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.specialvar_field.setObjectName(_fromUtf8("specialvar_field"))
        self.horizontalLayout_3.addWidget(self.specialvar_field)
        self.specialvar_button = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.specialvar_button.setObjectName(_fromUtf8("specialvar_button"))
        self.horizontalLayout_3.addWidget(self.specialvar_button)
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(30, 360, 111, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.file_button.setText(_translate("MainWindow", "open", None))
        self.label.setText(_translate("MainWindow", "netCDF File", None))
        self.label_2.setText(_translate("MainWindow", "Values 1D", None))
        self.label_3.setText(_translate("MainWindow", "Values 2D", None))
        self.label_4.setText(_translate("MainWindow", "Values 3D", None))
        self.plot_button.setText(_translate("MainWindow", "show plot", None))
        self.specialvar_button.setText(_translate("MainWindow", "add", None))
        self.label_5.setText(_translate("MainWindow", "special variable", None))

