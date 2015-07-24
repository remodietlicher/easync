#!/usr/bin/env python

from cmodifydialog import Ui_ModifyDialog
from mplcanvas import modifyCanvas

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class modifyDialog(Ui_ModifyDialog):
    def __init__(self, data):
        Ui_ModifyDialog.__init__(self)
        self.data = data

        self.canvas = modifyCanvas(self)
        toolbar = NavigationToolbar(self.canvas, parent=self)

        self.plotLayout.addWidget(toolbar)
        self.plotLayout.addWidget(self.canvas)

        self.canvas.plot_figure(data, 0)
        
        self.use_for_all_timesteps_checkbox.stateChanged.connect(self.applyToAllTmsts)
        self.select_all_checkbox.stateChanged.connect(self.selectAllPOnLine)
        self.tmst_spinbox.valueChanged.connect(self.loadTmst)
        self.save_button.clicked.connect(self.saveNetCDF)

    def saveNetCDF(self):
        self.data.writeVariableToFile()

    def applyToAllTmsts(self):
        self.data.var[:,:] = self.canvas.dl.line.get_xdata()

    def loadTmst(self):
        tmst = self.tmst_spinbox.value()
        tmin = 0
        tmax = self.data.var.shape[0]-1
        if(tmst < tmin):
            print 'timestep must not be negative: %s'%(tmst)
            self.tmst_spinbox.setValue(tmin)
        elif(tmst > tmax):
            print 'timestep must not be larger than %s. Given %s'%(tmax, tmst)
            self.tmst_spinbox.setValue(tmax)
        else:
            self.canvas.plot_figure(self.data, tmst)

    def selectAllPOnLine(self):
        if(self.select_all_checkbox.isChecked()):
            if(self.canvas.dl):
                print 'selecting all'
                self.canvas.dl.select_all()
        else:
            self.canvas.dl.deselect_all()
