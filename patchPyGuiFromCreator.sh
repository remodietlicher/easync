#!/bin/bash

MAIN='mainwindow'
PLOT='plotdialog'
CONF='configdialog'
MOD='modifydialog'
RHPOP='humiditycreatorpopdialog'
PRE='c'

pyuic4 guiCreator/$MAIN.ui > $PRE$MAIN.py
pyuic4 guiCreator/$PLOT.ui > $PRE$PLOT.py
pyuic4 guiCreator/$CONF.ui > $PRE$CONF.py
pyuic4 guiCreator/$MOD.ui > $PRE$MOD.py
pyuic4 guiCreator/$RHPOP.ui > $PRE$RHPOP.py
sed -i 's/class.*(object)*./\nclass Ui_MainWindow(QtGui.QMainWindow):\n    def __init__(self):\n        QtGui.QMainWindow.__init__(self)\n        self.setupUi(self)/' $PRE$MAIN.py
sed -i 's/class.*(object)*./\nclass Ui_PlotDialog(QtGui.QDialog):\n    def __init__(self):\n        QtGui.QDialog.__init__(self)\n        self.setupUi(self)/' $PRE$PLOT.py
sed -i 's/class.*(object)*./\nclass Ui_ConfigDialog(QtGui.QDialog):\n    def __init__(self):\n        QtGui.QDialog.__init__(self)\n        self.setupUi(self)/' $PRE$CONF.py
sed -i 's/class.*(object)*./\nclass Ui_ModifyDialog(QtGui.QDialog):\n    def __init__(self):\n        QtGui.QDialog.__init__(self)\n        self.setupUi(self)/' $PRE$MOD.py
sed -i 's/class.*(object)*./\nclass Ui_HumidityCreatorPopDialog(QtGui.QDialog):\n    def __init__(self):\n        QtGui.QDialog.__init__(self)\n        self.setupUi(self)/' $PRE$RHPOP.py
