#!/usr/bin/env python

from cmodifydialog import Ui_ModifyDialog
from mplcanvas import modifyCanvas

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class modifyDialog(Ui_ModifyDialog):
    def __init__(self, data):
        Ui_ModifyDialog.__init__(self)
        self.data = data
        self.activeAx = None

        self.canvas = modifyCanvas(self)
        toolbar = NavigationToolbar(self.canvas, parent=self)

        self.verticalLayout.addWidget(toolbar)
        self.plotLayout.addWidget(self.canvas)

        self.canvas.plot_figure(data, 0)
        
        self.copy_button.clicked.connect(self.applyCopy)
        self.change_button.clicked.connect(self.applyChange)
        self.select_all_checkbox.stateChanged.connect(self.selectAllPOnLine)
        self.tmst_spinbox.valueChanged.connect(self.loadTmst)
        self.save_button.clicked.connect(self.saveNetCDF)

    def saveNetCDF(self):
        for d in self.data:
            d.writeVariableToFile()

    def applyCopy(self):
        if(self.apply_selection_cb.isChecked()):
            self.applySelectedToAllTmsts()
        else:
            self.applyToAllTmsts()

    def applyChange(self):
        if(self.apply_selection_cb.isChecked()):
            self.applySelectedChangeToAllTmsts()
        else:
            self.applyChangeToAllTmsts()

    def applyToAllTmsts(self):
        for d in self.data:
            dl = self.canvas.dlDict[d]
            d.var[:,:] = dl.line.get_xdata()

    def applySelectedToAllTmsts(self):
        for d in data:
            dl = self.canvas.dlDict[d]
            selected = dl.selected
            d.var[:,selected] = dl.line.get_xdata()[selected]

    def applySelectedChangeToAllTmsts(self):
        for d in self.data:
            dl = self.canvas.dlDict[d]
            selected = dl.selected
            diff = dl.line.get_xdata()[selected] - d.var[:,selected]
            d.var[:,selected] += diff

    def applyChangeToAllTmsts(self):
        for d in self.data:
            dl = self.canvas.dlDict[d]
            diff = dl.line.get_xdata() - d.var[:,:]
            d.var[:,:] += diff

    def loadTmst(self):
        tmst = self.tmst_spinbox.value()
        tmin = 0
        tmax = self.data[0].var.shape[0]-1
        if(tmst < tmin):
            print 'timestep must not be negative: %s'%(tmst)
            self.tmst_spinbox.setValue(tmin)
        elif(tmst > tmax):
            print 'timestep must not be larger than %s. Given %s'%(tmax, tmst)
            self.tmst_spinbox.setValue(tmax)
        else:
            self.canvas.plot_figure(self.data, tmst)

    def selectAllPOnLine(self):
        dl = self.canvas.getActiveDl()
        if(self.select_all_checkbox.isChecked()):
            if(dl):
                print 'selecting all'
                dl.select_all()
        else:
            dl.deselect_all()
