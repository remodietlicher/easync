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
        
        # # read in sigma coords and convert to mid-level pressure
        # # from echam stream file
        # try:
        #     pdata = Dataset(str(self.filename), mode='r')
        # except:
        #     print 'invalid filename "%s"'%(self.filename)
        #     return
        self.done(True)
        # hyam = pdata.variables['hyam'][:]
        # hybm = pdata.variables['hybm'][:]
        # aps = pdata.variables['aps'][0,0,:]
        hyam = np.array([1000, 3000, 5000, 7000, 8988.068359375, 10898.337890625, 
                         12625.966796875, 14083.875, 15212.78125, 15977.908203125, 
                         16365.806640625, 16381.3125, 16044.609375, 15388.43359375, 
                         14455.39453125, 13295.40625, 11963.26171875, 10516.318359375, 
                         9012.30859375, 7507.275390625, 6053.626953125, 4698.31591796875, 
                         3481.1435546875, 2433.18725585938, 1575.34753417969, 917.019409179688, 
                         454.8876953125, 171.845024108887, 36.0317916870117, 0, 0])
        hybm = np.array([0, 0, 0, 0, 0.000195429078303275, 0.00165527942590415, 
                         0.0060569163179025, 0.0147566441446543, 0.0286470074206591, 
                         0.0482312496751547, 0.0736913084983826, 0.104949295520782, 
                         0.141722559928894, 0.183572381734848, 0.229945927858353, 
                         0.280211985111237, 0.333690196275711, 0.38967365026474, 
                         0.447445213794708, 0.50628736615181, 0.565485417842865, 
                         0.624324411153793, 0.682079493999481, 0.737999826669693, 
                         0.791286110877991, 0.841061413288116, 0.886335849761963, 
                         0.925964534282684, 0.958599209785461, 0.982633352279663, 0.996140748262405])
        aps = 100000
         
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
