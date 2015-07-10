#!/usr/bin/env python

import sys
import os
from cmainwindow import Ui_MainWindow
from cplotdialog import Ui_PlotDialog
from plothandler import plotHandler
from copy import copy

from netCDF4 import Dataset
import numpy as np

from PyQt4 import QtCore, QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = plt.figure()
        self.fig.subplots_adjust(wspace=0.5)

        self.ph = plotHandler(self.fig)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

    def plot_figure(self):
        pass

class sineCanvas(MplCanvas):
    def plot_figure(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)
        self.axes.plot(t, s)
        self.draw()

class dataCanvas(MplCanvas):
    def __init__(self, dialog=None, parent=None):
        self.dialog = dialog
        MplCanvas.__init__(self, parent)
    def plot_figure(self, data, nAxes, current):
        self.ph.makeAxes(nAxes, current)
        xlabel = ''
        ylabel = ''
        zlabel = ''
        if(data.ndim == 0):
            print data.var
        elif(data.ndim == 1 and len(data.time)==len(data.var)):
            xlabel = data.timeunit
            ylabel = data.varunit
            zlabel = ''
            self.ph.timeline(data.time, data.var, xlabel, ylabel, data.varlabel)
        elif(data.ndim == 1):
            xlabel = data.varunit
            ylabel = data.heightunit
            zlabel = ''
            self.ph.xzplot(data.var, data.height, xlabel, ylabel, data.varlabel)
        elif(data.ndim == 2):
            xlabel = data.timeunit
            ylabel = data.heightunit
            zlabel = data.varunit
            self.ph.timeline2d(data.time, data.height, data.var, xlabel, ylabel, zlabel)
        else:
            print 'unknown dimensions of input'
        #self.dialog.updateOptions()
        self.draw()

class plotDialog(Ui_PlotDialog):
    def __init__(self, data):
        Ui_PlotDialog.__init__(self)

        self.data = data
        self.nAxes = len(data)
        d = {'avgT':False, 'avgH':False, 'onefig':False}
        self.cbState = []
        for i in range(self.nAxes):
            self.cbState.append(copy(d))
        self.activeAx = None
        self.activeAxId = 0
        self.canvas = dataCanvas(dialog=self, parent=self.plotWidget)
        self.updateFigure()
        self.setActiveAx()
        toolbar = NavigationToolbar(self.canvas, self)

        self.plotLayout.addWidget(toolbar)
        self.plotLayout.addWidget(self.canvas)

        self.titleaxis_button.clicked.connect(self.set_xlabel)
        self.titleaxis_button.clicked.connect(self.set_ylabel)
        self.titleaxis_button.clicked.connect(self.set_title)
        self.titleaxis_button.clicked.connect(self.set_unit)
        self.activeax_comb.activated.connect(self.setActiveAx)

        self.avgT_cb.stateChanged.connect(self.averageTime)
        self.avgH_cb.stateChanged.connect(self.averageHeight)
        self.onefig_cb.stateChanged.connect(self.setNAxes)

        self.legendedit_button.clicked.connect(self.editLegendList)

    def setActiveAx(self):
        self.activeAxId = self.activeax_comb.currentIndex()
        print 'active axis=',self.activeAxId
        self.activeAx = self.canvas.fig.add_subplot(self.nAxes,1,self.activeAxId+1)
        self.updateOptions()
         
    def updateFigure(self):
        self.activeax_comb.clear()
        for i,d in enumerate(self.data):
            current = min(self.nAxes-1, i)
            self.canvas.plot_figure(d, self.nAxes, current)
            if(i<self.nAxes):
                self.activeax_comb.addItem('Axis %i'%(current+1))

    def updateOptions(self):
        ndimtot = self.data[self.activeAxId].ndimtot
        ndim = self.data[self.activeAxId].ndim
        if(ndim == 1):
            self.unit_field.setEnabled(False)
        elif(ndim == 2):
            self.unit_field.setEnabled(True)
        if(ndimtot == 1):
            self.avgT_cb.setEnabled(False)
            self.avgH_cb.setEnabled(False)
        elif(ndimtot == 2):
            self.avgT_cb.setEnabled(True)
            self.avgH_cb.setEnabled(True)
        if(self.avgH_cb.isChecked()):
            self.avgT_cb.setEnabled(False)
        if(self.avgT_cb.isChecked()):
            self.avgH_cb.setEnabled(False)

        self.onefig_cb.blockSignals(True)
        self.avgH_cb.blockSignals(True)
        self.avgT_cb.blockSignals(True)
        self.onefig_cb.setChecked(self.cbState[self.activeAxId]['onefig'])
        self.avgH_cb.setChecked(self.cbState[self.activeAxId]['avgH'])
        self.avgT_cb.setChecked(self.cbState[self.activeAxId]['avgT'])
        self.onefig_cb.blockSignals(False)
        self.avgH_cb.blockSignals(False)
        self.avgT_cb.blockSignals(False)

        handles, labels = self.activeAx.get_legend_handles_labels()
        xlabel = self.activeAx.get_xlabel()
        ylabel = self.activeAx.get_ylabel()
        zlabel = self.canvas.ph.axzlabel.get(self.activeAxId, '')
        print 'getting xlabel "%s", ylabel "%s", zlabel "%s" for axis "%s"'%(xlabel, ylabel,zlabel, self.activeAxId)
        self.xlabel_field.setText(xlabel)
        self.ylabel_field.setText(ylabel)
        self.unit_field.setText(zlabel)
        
    def set_unit(self):
        text = str(self.unit_field.text())
        cb = self.canvas.ph.axcb.get(self.activeAxId, None)
        print 'setting %s to'%(text), cb
        if(cb):
            cb.set_label(text)
            self.canvas.ph.axzlabel.update({self.activeAxId:text})
        self.canvas.draw()

    def set_xlabel(self):
        label = self.xlabel_field.text()
        self.activeAx.set_xlabel(label)
        self.canvas.draw()

    def set_ylabel(self):
        label = self.ylabel_field.text()
        self.activeAx.set_ylabel(label)
        self.canvas.draw()

    def set_title(self):
        title = self.title_field.text()
        self.activeAx.set_title(title)
        self.canvas.draw()

    def setNAxes(self):
        self.cbState[self.activeAxId]['onefig'] = self.onefig_cb.isChecked()
        self.canvas.ph.fig.clear()
        if self.onefig_cb.isChecked():
            self.nAxes = 1
        else:
            self.nAxes = len(self.data)
        self.updateFigure()

    def updateLabels(self):
        handles, labels = self.activeAx.get_legend_handles_labels()
        newLabels = [str(self.legend_list.item(i).text()) for i in range(self.legend_list.count())]
        print labels
        print newLabels
        self.activeAx.legend(handles, newLabels)
        self.canvas.draw()        

    def averageTime(self):
        self.cbState[self.activeAxId]['avgT'] = self.avgT_cb.isChecked()
        self.activeAx.cla()
        if(self.avgT_cb.isChecked()):
            self.data[self.activeAxId].integrateT()
            cb = self.canvas.ph.axcb[self.activeAxId]
            if(cb):
                cb.remove()
        else:
            self.data[self.activeAxId].restore()
        self.canvas.plot_figure(self.data[self.activeAxId], self.nAxes, self.activeAxId)
        self.updateOptions()

    def averageHeight(self):
        self.cbState[self.activeAxId]['avgH'] = self.avgH_cb.isChecked()
        #print self.cbState
        self.activeAx.cla()
        if(self.avgH_cb.isChecked()):
            self.data[self.activeAxId].integrateZ()
            cb = self.canvas.ph.axcb[self.activeAxId]
            if(cb):
                cb.remove()
        else:
            self.data[self.activeAxId].restore()
        self.canvas.plot_figure(self.data[self.activeAxId], self.nAxes, self.activeAxId)
        self.updateOptions()

    def editLegendList(self):
        item = self.legend_list.currentItem()
        text = self.legendedit_field.text()
        item.setText(text)
        self.updateLabels()
        

    
