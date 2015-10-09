# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiCreator/mainwindow.ui'
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


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(692, 518)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filename_field = QtGui.QLineEdit(self.centralWidget)
        self.filename_field.setObjectName(_fromUtf8("filename_field"))
        self.horizontalLayout.addWidget(self.filename_field)
        self.file_button = QtGui.QPushButton(self.centralWidget)
        self.file_button.setObjectName(_fromUtf8("file_button"))
        self.horizontalLayout.addWidget(self.file_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.var2d_list = QtGui.QListWidget(self.centralWidget)
        self.var2d_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.var2d_list.setObjectName(_fromUtf8("var2d_list"))
        self.gridLayout.addWidget(self.var2d_list, 1, 1, 1, 1)
        self.var1d_list = QtGui.QListWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.var1d_list.sizePolicy().hasHeightForWidth())
        self.var1d_list.setSizePolicy(sizePolicy)
        self.var1d_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.var1d_list.setObjectName(_fromUtf8("var1d_list"))
        self.gridLayout.addWidget(self.var1d_list, 1, 0, 1, 1)
        self.var3d_list = QtGui.QListWidget(self.centralWidget)
        self.var3d_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.var3d_list.setObjectName(_fromUtf8("var3d_list"))
        self.gridLayout.addWidget(self.var3d_list, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.specialvar_field = QtGui.QLineEdit(self.centralWidget)
        self.specialvar_field.setObjectName(_fromUtf8("specialvar_field"))
        self.horizontalLayout_3.addWidget(self.specialvar_field)
        self.specialvar_button = QtGui.QPushButton(self.centralWidget)
        self.specialvar_button.setObjectName(_fromUtf8("specialvar_button"))
        self.horizontalLayout_3.addWidget(self.specialvar_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(self.centralWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.mod_data_button = QtGui.QPushButton(self.centralWidget)
        self.mod_data_button.setObjectName(_fromUtf8("mod_data_button"))
        self.gridLayout_2.addWidget(self.mod_data_button, 1, 0, 1, 1)
        self.plot_button = QtGui.QPushButton(self.centralWidget)
        self.plot_button.setObjectName(_fromUtf8("plot_button"))
        self.gridLayout_2.addWidget(self.plot_button, 1, 1, 1, 1)
        self.humidity_button = QtGui.QPushButton(self.centralWidget)
        self.humidity_button.setObjectName(_fromUtf8("humidity_button"))
        self.gridLayout_2.addWidget(self.humidity_button, 2, 0, 1, 1)
        self.timescan_button = QtGui.QPushButton(self.centralWidget)
        self.timescan_button.setEnabled(False)
        self.timescan_button.setObjectName(_fromUtf8("timescan_button"))
        self.gridLayout_2.addWidget(self.timescan_button, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "netCDF File", None))
        self.file_button.setText(_translate("MainWindow", "open", None))
        self.label_2.setText(_translate("MainWindow", "Values 1D", None))
        self.label_3.setText(_translate("MainWindow", "Values 2D", None))
        self.label_4.setText(_translate("MainWindow", "Values 3D", None))
        self.label_5.setText(_translate("MainWindow", "special variable", None))
        self.specialvar_button.setText(_translate("MainWindow", "add", None))
        self.label_7.setText(_translate("MainWindow", "Data Files", None))
        self.label_6.setText(_translate("MainWindow", "Forcing Files", None))
        self.mod_data_button.setText(_translate("MainWindow", "modify data", None))
        self.plot_button.setText(_translate("MainWindow", "show plot", None))
        self.humidity_button.setText(_translate("MainWindow", "humidity creator", None))
        self.timescan_button.setText(_translate("MainWindow", "time scan", None))

