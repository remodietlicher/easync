#!/usr/bin/env python

import sys
import os
from cmainwindow import Ui_MainWindow
from humiditycreatorpopdialog import humidityCreatorPopDialog
from plotdialog import plotDialog
from configdialog import configDialog
from modifydialog import modifyDialog
from datahandler import dataHandler
from str2eq import evalEq, getVars
from util import HumidityConverter

from netCDF4 import Dataset
import numpy as np

from PyQt4 import QtCore, QtGui

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

hyam31 = np.array([1000, 3000, 5000, 7000, 8988.068359375, 10898.337890625, 
                   12625.966796875, 14083.875, 15212.78125, 15977.908203125, 
                   16365.806640625, 16381.3125, 16044.609375, 15388.43359375, 
                   14455.39453125, 13295.40625, 11963.26171875, 10516.318359375, 
                   9012.30859375, 7507.275390625, 6053.626953125, 4698.31591796875, 
                   3481.1435546875, 2433.18725585938, 1575.34753417969, 917.019409179688, 
                   454.8876953125, 171.845024108887, 36.0317916870117, 0, 0])
hybm31 = np.array([0, 0, 0, 0, 0.000195429078303275, 0.00165527942590415, 
                   0.0060569163179025, 0.0147566441446543, 0.0286470074206591, 
                   0.0482312496751547, 0.0736913084983826, 0.104949295520782, 
                   0.141722559928894, 0.183572381734848, 0.229945927858353, 
                   0.280211985111237, 0.333690196275711, 0.38967365026474, 
                   0.447445213794708, 0.50628736615181, 0.565485417842865, 
                   0.624324411153793, 0.682079493999481, 0.737999826669693, 
                   0.791286110877991, 0.841061413288116, 0.886335849761963, 
                   0.925964534282684, 0.958599209785461, 0.982633352279663, 0.996140748262405])
hyam47 = np.array([1000, 3000, 5000, 7000, 8988.068359375, 10898.337890625, 
                   12625.966796875, 14083.875, 15212.78125, 15977.908203125, 
                   16365.806640625, 16381.3125, 16044.609375, 15388.43359375, 
                   14455.39453125, 13295.40625, 11963.26171875, 10516.318359375, 
                   9012.30859375, 7507.275390625, 6053.626953125, 4698.31591796875, 
                   3481.1435546875, 2433.18725585938, 1575.34753417969, 917.019409179688, 
                   454.8876953125, 171.845024108887, 36.0317916870117, 0, 0])
hybm47 = np.array([0, 0, 0, 0, 0.000195429078303275, 0.00165527942590415, 
                   0.0060569163179025, 0.0147566441446543, 0.0286470074206591, 
                   0.0482312496751547, 0.0736913084983826, 0.104949295520782, 
                   0.141722559928894, 0.183572381734848, 0.229945927858353, 
                   0.280211985111237, 0.333690196275711, 0.38967365026474, 
                   0.447445213794708, 0.50628736615181, 0.565485417842865, 
                   0.624324411153793, 0.682079493999481, 0.737999826669693, 
                   0.791286110877991, 0.841061413288116, 0.886335849761963, 
                   0.925964534282684, 0.958599209785461, 0.982633352279663, 0.996140748262405])

class mainWindow(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.filename = ''
        self.datapath = ''
        self.varnames = []
        self.data = None

        self.file_button.clicked.connect(self.getFilename)
        self.filename_field.returnPressed.connect(self.reloadFile)
        self.plot_button.clicked.connect(self.popPlotDialog)
        self.mod_data_button.clicked.connect(self.popModDialog)
        self.specialvar_button.clicked.connect(self.addSpecialVar)
        self.humidity_button.clicked.connect(self.popHumCreatorDialog)

    def getFilename(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'File Browser')
        print name
        if(name == '' and self.filename == ''):
            print 'please open a file'
        elif(str(name).endswith('.nc')):
            self.setFilename(name)
            self.setupVariables()
        elif(str(self.filename).endswith('.nc')):
            self.setupVariables()

    def reloadFile(self):
        if(str(self.filename).endswith('.nc')):
            self.setupVariables()
        else:
            print 'please enter a valid netCDF filename'

    def setFilename(self, name):
        self.filename = name
        self.filename_field.setText(name)

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
        try:
            self.data = Dataset(str(self.filename), mode='a')
        except:
            print 'please enter a valid netCDF filename'
            return
        keys = [key for key in self.data.variables]
        keys = sorted(keys)
        for key in keys:
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

    def popModDialog(self):
        varnames1d = self.textFromListWidget(self.var1d_list)
        varnames2d = self.textFromListWidget(self.var2d_list)
        varnames3d = self.textFromListWidget(self.var3d_list)
        varnames = varnames1d + varnames2d + varnames3d
        if(len(varnames) <= 0):
            print 'invalid number of variables chosen: %s, must be >=1'%(len(varnames))
            return
        else:
            self.makeModDialog(varnames)

    def popHumCreatorDialog(self):
        varnames1d = self.textFromListWidget(self.var1d_list)
        varnames2d = self.textFromListWidget(self.var2d_list)
        varnames3d = self.textFromListWidget(self.var3d_list)
        varnames = varnames1d + varnames2d + varnames3d
        self.makeHumCreatorDialog(varnames)

    def textFromListWidget(self, lwidget, allNames=False):
        varnames = []
        for i in range(lwidget.count()):
            item = lwidget.item(i)
            text = item.text()
            if item.isSelected() or allNames:
                varnames.append(text)
        return varnames

    def makeDialog(self, varnames):
        datahandlers = []
        for name in varnames:
            dh = dataHandler(self.data, str(name))
            datahandlers.append(dh)
        pdialog = plotDialog(datahandlers)
        pdialog.setWindowTitle('Matplotlib Plot')
        pdialog.show()

        cdialog = configDialog(pdialog)
        cdialog.setWindowTitle('Configure')
        cdialog.show()

    def makeModDialog(self, varnames):
        datahandlers = []
        for name in varnames:
            dh = dataHandler(self.data, str(name))
            datahandlers.append(dh)

        moddialog = modifyDialog(datahandlers, self)
        moddialog.setWindowTitle('Modify netCDF data')
        moddialog.show()

    def makeHumCreatorDialog(self, varnames):
        datahandlers = []
        
        # read in temperature and specific humidity from forcing file
        temperature = self.data.variables['t'][0,:]
        spechum = self.data.variables['q'][0,:]

        varnames = list(set().union(varnames, ['q', 't']))
        print varnames
        nlvl = 0
        for name in varnames:
            dh = dataHandler(self.data, str(name))
            datahandlers.append(dh)
            nlvl = dh.nlvl

        if('vct_a' in self.data.variables.keys() and 'vct_b' in self.data.variables.keys()):
            print 'vct_a', self.data.variables['vct_a'][:].shape
            hyam = self.data.variables['vct_a'][:]
            hybm = self.data.variables['vct_b'][:]
            print 'vct_a taken from file:'
            print hyam
            print 'vct_b taken from file:'
            print hybm
        if(nlvl == 31):
            hyam = hyam31
            hybm = hybm31
        elif(nlvl == 47):
            hyam = hyam47
            hybm = hybm47
        else:
            print 'cannot handle those modellevels:', self.data.nlev
            return

        if('aps' in self.data.variables.keys()):
            aps = self.data.variables['aps'][0]
            print 'aps taken from file: aps = %s'%(aps)
        else:
            aps = 100000

        mlev = hyam+hybm*aps
        # interpolate interface pressure to midlvl pressures to much T and q
        # this can be done more carefully, but it doesn't really matter for the
        # application, so it may be improved some time later.
        if(len(mlev)%2 == 0):
            i = np.arange(len(mlev)-1)
            mlev = (mlev[i]+mlev[i+1])/2.0
        humConverter = HumidityConverter(mlev, temperature, spechum)
            
        moddialog = modifyDialog(datahandlers, self, humConverter)
        moddialog.setWindowTitle('Modify netCDF data')
        moddialog.show()
        print 'finished showing moddialog'

    def cleanup(self):
        self.data.close()


if __name__ == '__main__':
    qApp = QtGui.QApplication(sys.argv)
    
    aw = mainWindow()
    aw.setWindowTitle("%s" % progname)
    aw.show()
    sys.exit(qApp.exec_())
    #qApp.exec_()
