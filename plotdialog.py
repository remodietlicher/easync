#!/usr/bin/env python

import sys
import os
from cmainwindow import Ui_MainWindow
from cplotdialog import Ui_PlotDialog
from plothandler import plotHandler
from mplcanvas import dataCanvas
from copy import copy

from netCDF4 import Dataset
import numpy as np

from PyQt4 import QtCore, QtGui

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

class plotDialog(Ui_PlotDialog):
    def __init__(self, data):
        Ui_PlotDialog.__init__(self)

        self.configDialog = None
        self.data = data
        self.nAxes = len(data)
        self.plotTypes = [d.defaultPlotType for d in data]
        self.canvas = dataCanvas(dialog=self, parent=self)
        self.activeAxId = 0
        self.reloadFigures()
        self.activeAx = self.canvas.fig.add_subplot(self.nAxes,1,self.activeAxId+1)
        toolbar = NavigationToolbar(self.canvas, self)

        self.ax2AxId = {self.canvas.fig.add_subplot(self.nAxes,1,i+1) : i for i in range(self.nAxes)}

        self.plotLayout.addWidget(toolbar)
        self.plotLayout.addWidget(self.canvas)

    def registerConfigDialog(self, configDialog):
        self.configDialog = configDialog
        self.updateAvailablePlots()
        self.updateConfig()
        self.updateAxesCombobox()

    def setActiveAx(self, ax=None):
        print 'setting ax: %s'%(ax)
        if(isinstance(ax, int)):
            self.activeAxId = self.configDialog.getActiveAxId()
        else:
            self.activeAxId = self.ax2AxId[ax]
        print 'active axis=', self.activeAxId
        self.activeAx = self.canvas.fig.add_subplot(self.nAxes,1,self.activeAxId+1)
        self.updateAvailablePlots()
        self.updateConfig()
         
    def reloadFigures(self):
        self.canvas.fig.clf()
        for i,d in enumerate(self.data):
            current = min(i, self.nAxes-1)
            self.canvas.plot_figure(d, self.nAxes, current, self.plotTypes[i])
        self.activeAx = self.canvas.fig.add_subplot(self.nAxes,1,self.activeAxId+1)

    def updateAxesCombobox(self):
        self.configDialog.activeax_comb.blockSignals(True)
        self.configDialog.activeax_comb.clear()
        for i in range(len(self.data)):
            if(i<self.nAxes):
                self.configDialog.activeax_comb.addItem('Axis %i'%(i+1))
        self.configDialog.activeax_comb.blockSignals(False)

    def updateConfig(self):
        handles, labels = self.activeAx.get_legend_handles_labels()
        xlabel = self.activeAx.get_xlabel()
        ylabel = self.activeAx.get_ylabel()
        zlabel = self.canvas.ph.axzlabel.get(self.activeAxId, '')
        title = self.activeAx.get_title()
        self.configDialog.setAxes(xlabel, ylabel, zlabel, title)
        self.configDialog.setPlotType(self.plotTypes[self.activeAxId])
        self.configDialog.setLabels(labels)
        self.configDialog.setActiveAxId(self.activeAxId)

    def updateAvailablePlots(self):
        self.configDialog.plot_comb.blockSignals(True)
        self.configDialog.plotToCBID = {}
        self.configDialog.plot_comb.clear()
        cnt = 0
        if(self.data[self.activeAxId].hasTimeVal):
            self.configDialog.plot_comb.addItem('TIME')
            self.configDialog.plotToCBID.update({'TIME':cnt})
            cnt += 1
        if(self.data[self.activeAxId].hasHeightVal):
            self.configDialog.plot_comb.addItem('HEIGHT')
            self.configDialog.plotToCBID.update({'HEIGHT':cnt})
            cnt += 1
        if(self.data[self.activeAxId].hasTimeVal and self.data[self.activeAxId].hasHeightVal):
            self.configDialog.plot_comb.addItem('TIMEHEIGHT')
            self.configDialog.plotToCBID.update({'TIMEHEIGHT':cnt})
            cnt += 1
            self.configDialog.plot_comb.addItem('TIMESLICE')
            self.configDialog.plotToCBID.update({'TIMESLICE':cnt})          
            cnt += 1
        self.configDialog.plot_comb.blockSignals(False)
        
        
    def set_unit(self):
        text = str(self.configDialog.zlabel_field.text())
        cb = self.canvas.ph.axcb.get(self.activeAxId, None)
        #print 'setting %s to'%(text), cb
        if(cb):
            cb.set_label(text)
            self.canvas.ph.axzlabel.update({self.activeAxId:text})
        self.canvas.draw()

    def set_xlabel(self):
        label = self.configDialog.xlabel_field.text()
        self.activeAx.set_xlabel(label)
        self.canvas.draw()

    def set_ylabel(self):
        label = self.configDialog.ylabel_field.text()
        self.activeAx.set_ylabel(label)
        self.canvas.draw()

    def set_title(self):
        title = self.configDialog.title_field.text()
        self.activeAx.set_title(title)
        self.canvas.draw()

    def setNAxes(self):
        if self.configDialog.onefig_cb.isChecked():
            self.nAxes = 1
        else:
            self.nAxes = len(self.data)
        self.activeAxId = 0
        self.reloadFigures()
        self.updateAxesCombobox()
        self.updateConfig()
        
    def setLabelsToPlot(self):
        handles, labels = self.activeAx.get_legend_handles_labels()
        newLabels = [str(self.configDialog.legend_list.item(i).text()) for i in range(self.configDialog.legend_list.count())]
        print newLabels
        self.activeAx.legend(handles, newLabels)
        self.canvas.draw()
        handles, labels = self.activeAx.get_legend_handles_labels()

    def changePlotType(self):
        self.activeAx.cla()
        newType = self.configDialog.getPlotType()
        self.plotTypes[self.activeAxId] = newType
        self.canvas.plot_figure(self.data[self.activeAxId], self.nAxes, self.activeAxId, self.configDialog.getPlotType())
        cb = self.canvas.ph.axcb[self.activeAxId]
        if(cb and (newType == 'TIME' or newType == 'HEIGHT' or newType == 'TIMESLICE')):
            cb.remove()
            self.canvas.ph.axcb[self.activeAxId] = None
            #self.canvas.fig.subplots_adjust(right=0.9)
        self.canvas.draw()
        self.updateConfig()

    def editLegendList(self):
        item, text = self.configDialog.getLegendItemText()
        item.setText(text)
        self.setLabelsToPlot()
        

    
