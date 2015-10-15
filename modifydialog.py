#!/usr/bin/env python

from cmodifydialog import Ui_ModifyDialog
from mplcanvas import modifyCanvas

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class modifyDialog(Ui_ModifyDialog):
    def __init__(self, datahandlers, humConverter=None):
        Ui_ModifyDialog.__init__(self)
        self.datahandlers = datahandlers
        self.activeAx = None

        self.canvas = modifyCanvas(humConverter=humConverter, parent=self)
        toolbar = NavigationToolbar(self.canvas, parent=self)

        self.verticalLayout.addWidget(toolbar)
        self.plotLayout.addWidget(self.canvas)

        self.canvas.plot_figure(self.datahandlers, 0)
        self.canvas.register_release_listener(self)
        
        self.copy_button.clicked.connect(self.applyCopy)
        self.change_button.clicked.connect(self.applyChange)
        self.select_all_checkbox.stateChanged.connect(self.selectAllPOnLine)
        self.tmst_spinbox.valueChanged.connect(self.loadTmst)
        self.save_button.clicked.connect(self.saveNetCDF)

    def update_data(self):
        tmst = self.tmst_spinbox.value()
        for d in self.datahandlers:
            dl = self.canvas.dlDict[d.longname]
            d.var[tmst,:] = dl.line.get_xdata()

    def saveNetCDF(self):
        for d in self.datahandlers:
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
        for d in self.datahandlers:
            dl = self.canvas.dlDict[d.longname]
            d.var[:,:] = dl.line.get_xdata()

    def applySelectedToAllTmsts(self):
        for d in data:
            dl = self.canvas.dlDict[d.longname]
            selected = dl.selected
            d.var[:,selected] = dl.line.get_xdata()[selected]

    def applySelectedChangeToAllTmsts(self):
        for d in self.datahandlers:
            dl = self.canvas.dlDict[d.longname]
            selected = dl.selected
            diff = dl.line.get_xdata()[selected] - d.var[:,selected]
            d.var[:,selected] += diff

    def applyChangeToAllTmsts(self):
        for d in self.datahandlers:
            dl = self.canvas.dlDict[d.longname]
            diff = dl.line.get_xdata() - d.var[:,:]
            d.var[:,:] += diff

    def loadTmst(self):
        tmst = self.tmst_spinbox.value()
        tmin = 0
        tmax = self.datahandlers[0].var.shape[0]-1
        if(tmst < tmin):
            print 'timestep must not be negative: %s'%(tmst)
            self.tmst_spinbox.setValue(tmin)
        elif(tmst > tmax):
            print 'timestep must not be larger than %s. Given %s'%(tmax, tmst)
            self.tmst_spinbox.setValue(tmax)
        else:
            self.canvas.update_figure(tmst)
                

    def selectAllPOnLine(self):
        dl = self.canvas.getActiveDl()
        if(self.select_all_checkbox.isChecked()):
            if(dl):
                print 'selecting all'
                dl.select_all()
        else:
            dl.deselect_all()
