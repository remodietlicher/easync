from chumiditycreatorpopdialog import Ui_HumidityCreatorPopDialog
from datahandler import dataHandler
from modifydialog import modifyDialog
from util import HumidityConverter

from netCDF4 import Dataset
import numpy as np

from PyQt4 import QtCore, QtGui

class humidityCreatorPopDialog(Ui_HumidityCreatorPopDialog):
    def __init__(self, data, parent=None):
        Ui_HumidityCreatorPopDialog.__init__(self)
        self.filename = ''
        self.data = data

        self.open_button.clicked.connect(self.getFilename)
        self.open_button.clicked.connect(self.setFilename)
        self.cancel_button.clicked.connect(self.done)
        self.load_button.clicked.connect(self.makeHumCreatorDialog)
        
    def getFilename(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'File Browser')

    def setFilename(self):
        self.dataname_field.setText(self.filename)

    def makeHumCreatorDialog(self):
        datahandlers = []
        
        # read in temperature and specific humidity from forcing file
        temperature = self.data.variables['t'][0,:]
        spechum = self.data.variables['q'][0,:]
        
        # read in sigma coords and convert to mid-level pressure
        # from echam stream file
        try:
            pdata = Dataset(str(self.filename), mode='r')
        except:
            print 'invalid filename "%s"'%(self.filename)
            return
        self.done(True)
        hyam = pdata.variables['hyam'][:]
        hybm = pdata.variables['hybm'][:]
        aps = pdata.variables['aps'][0,0,:]
        mlev = hyam+hybm*aps

        humConverter = HumidityConverter(mlev, temperature, spechum)

        varnames = ['q', 't']
        for name in varnames:
            dh = dataHandler(self.data, str(name))
            datahandlers.append(dh)
            
        moddialog = modifyDialog(datahandlers, humConverter)
        moddialog.setWindowTitle('Modify netCDF data')
        moddialog.show()
        self.done(True)
