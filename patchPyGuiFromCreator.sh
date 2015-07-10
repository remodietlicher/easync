#!/bin/bash

MAIN='mainwindow'
PLOT='plotdialog'
PRE='c'

pyuic4 guiCreator/$MAIN.ui > $PRE$MAIN.py
pyuic4 guiCreator/$PLOT.ui > $PRE$PLOT.py
sed -i 's/class.*(object)*./\nclass Ui_MainWindow(QtGui.QMainWindow):\n    def __init__(self):\n        QtGui.QMainWindow.__init__(self)\n        self.setupUi(self)/' $PRE$MAIN.py
sed -i 's/class.*(object)*./\nclass Ui_PlotDialog(QtGui.QDialog):\n    def __init__(self):\n        QtGui.QDialog.__init__(self)\n        self.setupUi(self)/' $PRE$PLOT.py
