import numpy as np
import matplotlib.pyplot as plt
from plothandler import plotHandler
from copy import copy

class DraggableLine:
    def __init__(self, line, allowX=True, allowY=True):
        self.line = line
        self.pick = None
        self.allowX = allowX
        self.allowY = allowY
        self.collect = False
        self.selected = []

        ax = self.line.figure.add_subplot(111)
        self.markers, = ax.plot([],[],'o',color='r')

    def select_all(self):
        self.selected = [i for i, val in enumerate(self.line.get_xdata())]
        self.collect = True
        self.update_markers()

    def deselect_all(self):
        self.selected = []
        self.collect = False
        self.update_markers()

    def connect(self):
        'connect to all the events we need'
        self.cidpick = self.line.figure.canvas.mpl_connect(
            'pick_event', self.on_pick)
        self.cidrelease = self.line.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.line.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)
        self.cidkeypress = self.line.figure.canvas.mpl_connect(
            'key_press_event', self.on_key_press)
        self.cidkeyrelease = self.line.figure.canvas.mpl_connect(
            'key_release_event', self.on_key_release)
        
    def disconnect(self):
        'disconnect all the stored connection ids'
        self.line.figure.canvas.mpl_disconnect(self.cidpick)
        self.line.figure.canvas.mpl_disconnect(self.cidrelease)
        self.line.figure.canvas.mpl_disconnect(self.cidmotion)

    def on_key_press(self, event):
        print 'pressing key: %s'%(event.key)
        if(event.key == 'control'):
            self.collect = True

    def on_key_release(self, event):
        print 'releasing key: %s'%(event.key)
        if(event.key == 'control'):
            self.collect = False


    def on_pick(self, event):
        ind = event.ind
        if(self.collect):
            self.selected = np.union1d(self.selected, ind)
            print self.selected
        else:
            self.selected = ind
        xdata = self.line.get_xdata()
        ydata = self.line.get_ydata()

        x0 = copy(xdata[self.selected])
        y0 = copy(ydata[self.selected])
        self.update_markers()

        self.pick = x0, y0, event.mouseevent.xdata, event.mouseevent.ydata

    def on_motion(self, event):
        if self.pick is None: return
        if event.inaxes != self.line.axes: return
        x0, y0, xpick, ypick = self.pick
        dx = event.xdata - xpick
        dy = event.ydata - ypick

        xdata = self.line.get_xdata()
        ydata = self.line.get_ydata()

        for i,idx in enumerate(self.selected):
            if(self.allowX):
                xdata[idx] = x0[i] + dx
            if(self.allowY):
                ydata[idx] = y0[i] + dy

        self.line.set_data(xdata, ydata)
        self.update_markers()

        self.line.figure.canvas.draw()

    def on_release(self, event):
        'on release we reset the pick data'
        self.pick = None
        self.line.figure.canvas.draw()

    def update_markers(self):
        ax = self.line.figure.add_subplot(111)
        xdata = self.line.get_xdata()
        ydata = self.line.get_ydata()

        xmarked = xdata[self.selected]
        ymarked = ydata[self.selected]
        self.markers.set_data(xmarked, ymarked)
        self.line.figure.canvas.draw()

class ZoomableFigure:
    def __init__(self, dialog, plothandler):
        self.plothandler = plothandler
        self.dialog = dialog

    def connect(self):
        print 'connecting button_press_event'
        self.ciddblclick = self.plothandler.fig.canvas.mpl_connect(
             'button_press_event', self.on_dblclick)

    def on_dblclick(self, event):
        if event.dblclick:
            print 'double clicking on: (%.1f, %.1f)'%(event.xdata, event.ydata)
            ax = event.inaxes
            time = event.xdata
            self.dialog.setActiveAx(ax=ax)
            print 'got: ax=%s, time=%s'%(ax, time)
            self.dialog.configDialog.setSliceTime(time)
            self.dialog.configDialog.setPlotType('TIMESLICE')
            self.dialog.changePlotType()
        
        
