from PyQt4 import QtCore, QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np

from util import DraggableLine, ZoomableFigure, HumidityConverter
from plothandler import plotHandler

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = plt.figure()
        self.fig.subplots_adjust(hspace=0.5)
        self.fig.canvas.mpl_connect('button_release_event', self.setActiveAx)
        self.activeAx = None

        self.ph = plotHandler(self.fig)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.setFocusPolicy( QtCore.Qt.ClickFocus )
        self.setFocus()

    def plot_figure(self):
        pass

    def setActiveAx(self, event):
        self.activeAx = event.inaxes

    def connect(self):
        self.cidrelease = self.fig.canvas.mpl_connect('button_release_event', self.setActiveAx)

    def disconnect(self):
        self.fig.canvas.mpl_disconnect(self.cidrelease)


class dataCanvas(MplCanvas):
    def __init__(self, dialog=None, parent=None):
        self.dialog = dialog
        MplCanvas.__init__(self, parent)
        self.zfig = ZoomableFigure(self.dialog, self.ph)
        self.zfig.connect()
    def plot_figure(self, data, nAxes, current, plotType):
        self.ph.makeAxes(nAxes, current)
        xlabel = ''
        ylabel = ''
        zlabel = ''
        print 'plotting %s...'%(data.longname)
        if(plotType == 'TIME'):
            xlabel = data.timeunit
            ylabel = data.varunit
            zlabel = ''
            self.ph.timeline(data.time, data.getTimeValue(), xlabel, ylabel, data.varlabel)
        elif(plotType == 'HEIGHT'):
            xlabel = data.varunit
            ylabel = data.heightunit
            zlabel = ''
            self.ph.xzplot(data.getHeightValue(), data.height, xlabel, ylabel, data.varlabel)
        elif(plotType == 'TIMEHEIGHT'):
            xlabel = data.timeunit
            ylabel = data.heightunit
            zlabel = data.varunit
            self.ph.timeline2d(data.time, data.height, data.getTimeHeightMatrix(), xlabel, ylabel, zlabel)
        elif(plotType == 'TIMESLICE'):
            xlabel = data.varunit
            ylabel = data.heightunit
            zlabel = ''
            time = self.dialog.configDialog.time
            self.ph.xzplot(data.getTimeSlice(time), data.height, xlabel, ylabel, data.varlabel)
        else:
            print 'unknown dimensions of input'
        self.ph.setTitle(data.longname)
        self.draw()


class modifyCanvas(MplCanvas):
    def __init__(self, humConverter=None, parent=None):
        MplCanvas.__init__(self, parent)
        self.humConverter = humConverter
        self.dlDict = {}
        self.axDlDict = {}
        self.fig.subplots_adjust(left=0.07, right=0.95)
        self.datahandlers = None
        self.height = None

    def plot_figure(self, datahandlers, tmst):
        self.datahandlers = datahandlers
        self.height = datahandlers[0].height
        self.heightunit = datahandlers[0].heightunit
        self.fig.clf()
        N = len(datahandlers)
        if(self.humConverter): N += 1
        for i,d in enumerate(datahandlers):
            if(d.hasHeightVal and d.hasTimeVal):
                subplotID = 100+N*10+i+1
                ax = self.fig.add_subplot(subplotID)
                ax.set_title(d.longname)
                ax.set_ylabel(d.heightunit)
                ax.set_xlabel(d.varunit)
                X = d.var[tmst]
                Y = d.height
                if(not ax.yaxis_inverted()):
                    ax.invert_yaxis()
                line, = ax.plot(X, Y, 'o-', picker=5)
                dl = DraggableLine(ax, line, d.longname)
                if(self.humConverter):
                    dl.register_listener(self.humConverter)
                self.dlDict.update({d.longname : dl})
                self.axDlDict.update({ax : dl})
                dl.connect()
        self.connect()
        if(self.humConverter):
            subplotID = 100+N*10+N
            ax = self.fig.add_subplot(subplotID)
            ax.set_title(self.humConverter.rhn)
            ax.set_ylabel(self.heightunit)
            ax.set_xlabel('')
            X = self.humConverter.relhum
            Y = self.height
            print 'relhum:', X.shape
            print 'height:', Y.shape
            ax.set_xlim(left=0, right=max(1.2, np.max(X)))
            if(not ax.yaxis_inverted()):
                ax.invert_yaxis()
            line, = ax.plot(X, Y, 'o-', picker=5)
            dl = DraggableLine(ax, line, self.humConverter.rhn)
            dl.register_listener(self.humConverter)
            self.dlDict.update({self.humConverter.rhn : dl})
            self.axDlDict.update({ax : dl})
            dl.connect()
            self.connect_humidity()

    def update_figure(self, tmst):
        temperature = None
        spechum = None
        for dh in self.datahandlers:
            dl = self.dlDict[dh.longname]
            # ubergibt var by reference, also wird mit dem plot auch
            # gleich die variable beschrieben!
            dl.line.set_xdata(dh.var[tmst])
            dl.update_markers()
            if self.humConverter:
                if(dh.longname == self.humConverter.tn):
                    temperature = dh.var[tmst]
                elif(dh.longname == self.humConverter.qn):
                    spechum = dh.var[tmst]
        if self.humConverter:
            self.humConverter.set_profiles(temperature, spechum)
            dl = self.dlDict[self.humConverter.rhn]
            dl.line.set_xdata(self.humConverter.relhum)
            dl.update_markers()
        self.draw()
        
    def connect_humidity(self):
        for k, v in self.dlDict.iteritems():
            self.humConverter.register_listener(v, k)
        
    def getActiveDl(self):
        if(self.activeAx):
            return self.axDlDict[self.activeAx]
        else:
            return None
