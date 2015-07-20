#!/usr/bin/env python

import sys
import os
from cmainwindow import Ui_MainWindow
from plotdialog import plotDialog
from configdialog import configDialog
from datahandler import dataHandler
from str2eq import evalEq, getVars

from netCDF4 import Dataset
import numpy as np

from PyQt4 import QtCore, QtGui

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

class mainWindow(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.filename = ''
        self.varnames = []
        self.data = None

        self.file_button.clicked.connect(self.getFilename)
        self.file_button.clicked.connect(self.setFilename)
        self.file_button.clicked.connect(self.setupVariables)
        self.plot_button.clicked.connect(self.popPlotDialog)
        self.specialvar_button.clicked.connect(self.addSpecialVar)

    def getFilename(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'File Browser', '/home/remo/data/SCMmpace/cloud/')

    def setFilename(self):
        self.filename_field.setText(self.filename)

    def addSpecialVar(self):
        eq = str(self.specialvar_field.text())
        eqVars = getVars(eq)
        if(not (eq.count('(') == eq.count(')'))):
            print 'invalid equation'
            return
        contains = np.product([var in self.data.variables for var in eqVars])
        if(not contains):
            print 'invalid variable'
            return
        ndims = [len(np.squeeze(self.data.variables[key]).shape) for key in eqVars]
        samedims = ndims[1:] == ndims[:-1]
        if(not samedims):
            print 'evaluating variables of different dimension'
            return
        if(not self.data):
            print 'no data'
        else:
            varnames1d = self.textFromListWidget(self.var1d_list, allNames=True)
            varnames2d = self.textFromListWidget(self.var2d_list, allNames=True)
            varnames3d = self.textFromListWidget(self.var3d_list, allNames=True)
            dim = ndims[0]
            if(dim == 1 and not eq in varnames1d):
                self.var1d_list.addItem(eq)
            elif(dim == 2 and not eq in varnames2d):
                self.var2d_list.addItem(eq)
            elif(dim == 3 and not eq in varnames3d):
                self.var3d_list.addItem(eq)
            else:
                print 'unknown dimension:', eq, dim
        

    def setupVariables(self):
        self.var1d_list.clear()
        self.var2d_list.clear()
        self.var3d_list.clear()
        if(self.data):
            self.data.close()
        self.data = Dataset(str(self.filename), mode='r')
        for key in self.data.variables:
            dim = len(np.squeeze(self.data.variables[key]).shape)
            if(dim == 1):
                self.var1d_list.addItem(key)
            elif(dim == 2):
                self.var2d_list.addItem(key)
            elif(dim == 3):
                self.var3d_list.addItem(key)
            else:
                print 'unknown dimension:', key, dim

    def popPlotDialog(self):
        varnames1d = self.textFromListWidget(self.var1d_list)
        varnames2d = self.textFromListWidget(self.var2d_list)
        varnames3d = self.textFromListWidget(self.var3d_list)
        varnames = varnames1d + varnames2d + varnames3d
        if(len(varnames) > 0):
            self.makeDialog(varnames)
        #if(len(varnames1d) > 0):
        #    self.makeDialog(varnames1d)
        #if(len(varnames2d) > 0):
        #    self.makeDialog(varnames2d)
        #if(len(varnames3d) > 0):
        #    self.makeDialog(varnames3d)

    def textFromListWidget(self, lwidget, allNames=False):
        varnames = []
        for i in range(lwidget.count()):
            item = lwidget.item(i)
            text = item.text()
            if item.isSelected() or allNames:
                varnames.append(text)
        return varnames

    def makeDialog(self, varnames):
        data = []
        for name in varnames:
            dh = dataHandler(self.data, str(name))
            data.append(dh)
        pdialog = plotDialog(data)
        pdialog.setWindowTitle('Matplotlib Plot')
        pdialog.show()

        cdialog = configDialog(pdialog)
        cdialog.setWindowTitle('Configure')
        cdialog.show()


if __name__ == '__main__':
    qApp = QtGui.QApplication(sys.argv)
    
    aw = mainWindow()
    aw.setWindowTitle("%s" % progname)
    aw.show()
    sys.exit(qApp.exec_())
    #qApp.exec_()
