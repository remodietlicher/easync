from PyQt4 import QtCore, QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from util import DraggableLine
from plothandler import plotHandler

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = plt.figure()
        self.fig.subplots_adjust(hspace=0.5)

        self.ph = plotHandler(self.fig)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.setFocusPolicy( QtCore.Qt.ClickFocus )
        self.setFocus()

    def plot_figure(self):
        pass

class dataCanvas(MplCanvas):
    def __init__(self, dialog=None, parent=None):
        self.dialog = dialog
        MplCanvas.__init__(self, parent)
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
        else:
            print 'unknown dimensions of input'
        self.ph.setTitle(data.longname)
        self.draw()


class modifyCanvas(MplCanvas):
    def __init__(self, parent=None):
        MplCanvas.__init__(self, parent)
        self.ax = self.fig.add_subplot(111)
        self.dl = None

    def plot_figure(self, data, tmst):
        self.ax.cla()
        if(data.hasHeightVal and data.hasTimeVal):
            print data.var.shape
            X = data.var[tmst]
            Y = data.height
            if(not self.ax.yaxis_inverted()):
                self.ax.invert_yaxis()
            line, = self.ax.plot(X, Y, 'o-', picker=5)
            self.dl = DraggableLine(line, allowY=False)
            self.dl.connect()
            self.draw()
