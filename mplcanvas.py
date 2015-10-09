from PyQt4 import QtCore, QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from util import DraggableLine, ZoomableFigure
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
    def __init__(self, parent=None):
        MplCanvas.__init__(self, parent)
        self.dlDict = {}
        self.axDlDict = {}
        self.fig.subplots_adjust(left=0.07, right=0.95)

    def plot_figure(self, data, tmst):
        self.fig.clf()
        N = len(data)
        for i,d in enumerate(data):
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
                dl = DraggableLine(ax, line, allowY=False)
                self.dlDict.update({d : dl})
                self.axDlDict.update({ax : dl})
                dl.connect()
                self.draw()
        self.connect()
        
    def getActiveDl(self):
        if(self.activeAx):
            return self.axDlDict[self.activeAx]
        else:
            return None
