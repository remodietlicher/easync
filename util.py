import numpy as np
import matplotlib.pyplot as plt
from plothandler import plotHandler
from copy import copy

class DraggableLine:
    def __init__(self, ax, line, ltype):
        self.line = line
        self.ax = ax
        self.pick = None
        self.collect = False
        self.selected = []
        self.moveListeners = []
        self.ltype = ltype
        self.converter = None
        
        self.markers, = self.ax.plot([],[],'o',color='r')

    def register_move_listener(self, listener):
        self.moveListeners.append(listener)

    def register_release_listener(self, listener):
        self.releaseListeners.append(listener)

    def forward_move(self, data):
        for l in self.moveListeners:
            l.handle_data_change(data, self.ltype)
        
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
        self.line.figure.canvas.mpl_disconnect(self.cidkeypress)
        self.line.figure.canvas.mpl_disconnect(self.cidkeyrelease)

    def on_key_press(self, event):
        if(event.key == 'control'):
            self.collect = True

    def on_key_release(self, event):
        if(event.key == 'control'):
            self.collect = False


    def on_pick(self, event):
        ind = event.ind
        if(self.collect):
            self.selected = np.union1d(self.selected, ind)
        else:
            self.selected = ind
        xdata = self.line.get_xdata()
        ydata = self.line.get_ydata()

        x0 = copy(xdata[self.selected])
        y0 = copy(ydata[self.selected])
        self.update_markers()
        self.line.figure.canvas.draw()

        self.pick = x0, y0, event.mouseevent.xdata, event.mouseevent.ydata

    def on_motion(self, event):
        if self.pick is None: return
        if event.inaxes != self.line.axes: return
        x0, y0, xpick, ypick = self.pick
        dx = event.xdata - xpick

        xdata = self.line.get_xdata()

        for i,idx in enumerate(self.selected):
                xdata[idx] = x0[i] + dx
        
        self.update_data(xdata)
        self.forward_move(xdata)

    def on_release(self, event):
        self.pick = None

    def update_data(self, xdata):
        self.line.set_xdata(xdata)
        self.update_markers()
        self.line.figure.canvas.draw()

    def update_markers(self):
        xdata = self.line.get_xdata()
        ydata = self.line.get_ydata()

        xmarked = xdata[self.selected]
        ymarked = ydata[self.selected]
        self.markers.set_data(xmarked, ymarked)

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

class HumidityConverter:
    def __init__(self, pressure, temperature, spechum):
        self.pressure = pressure
        self.eps = 0.622
        self.temperature = temperature
        self.spechum = spechum
        self.relhum = self.t_q_to_rh()
        self.t_listeners = []
        self.q_listeners = []
        self.rh_listeners = []

        self.qn = 'Specific humidity'
        self.rhn = 'relative humidity'
        self.tn = 'Temparature'

    def set_profiles(self, temperature, spechum):
        self.temperature = temperature
        self.spechum = spechum
        self.relhum = self.t_q_to_rh()

    def register_listener(self, listener, ltype):
        if(ltype == self.qn):
            self.q_listeners.append(listener)
        elif(ltype == self.rhn):
            self.rh_listeners.append(listener)
        elif(ltype == self.tn):
            self.t_listeners.append(listener)

    def handle_data_change(self, data, t):
        if(t == self.tn):
            self.set_temperature(data)
        elif(t == self.rhn):
            self.set_relhum(data)
        elif(t == self.qn):
            self.set_spechum(data)

    def notify_temperature_listeners(self):
        for l in self.t_listeners:
            l.update_data(self.temperature)

    def notify_relhum_listeners(self):
        for l in self.rh_listeners:
            l.update_data(self.relhum)

    def notify_spechum_listeners(self):
        for l in self.q_listeners:
            l.update_data(self.spechum)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.relhum = self.t_q_to_rh()
        self.notify_relhum_listeners()

    def set_relhum(self, relhum):
        self.relhum = relhum
        self.spechum = self.t_rh_to_q()
        self.notify_spechum_listeners()

    def set_spechum(self, spechum):
        self.spechum = spechum
        self.relhum = self.t_q_to_rh()
        self.notify_relhum_listeners()

    # Pa and K    
    def magnus(self, T):
        # k1 -> k3 for hPa and deg C
        k1 = 6.1094
        k2 = 17.625
        k3 = 243.04
        T0 = 273.16
        return k1*100*np.exp(k2*(T-T0)/((T-T0)+k3))

    def t_q_to_rh(self):
        T = self.temperature
        q = self.spechum
        es = self.magnus(T)
        w = q/(1-q)
        e = w/(w+self.eps)*self.pressure
        return e/es
        
    def t_rh_to_q(self):
        T = self.temperature
        rh = self.relhum
        es = self.magnus(T)
        e = rh*es
        w = e*self.eps/(e+self.pressure)
        return w/(w+1)
        
        
