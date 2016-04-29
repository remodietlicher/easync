import matplotlib.pyplot as plt
import numpy as np
import scipy
from matplotlib.colors import LogNorm
import matplotlib.ticker

llog = False

class plotHandler:
    def __init__(self, fig):
        self.fig = fig
        self.ax = None
        self.axzlabel = {}
        self.axcb = {}
        self.nAxes = 1
        self.currentAx = 1

    def makeAxes(self, nAxes, current):
        self.ax = self.fig.add_subplot(nAxes, 1, current+1)
        self.nAxes = nAxes
        self.currentAx = current
        if(nAxes==1):
            self.ax.hold(True)

    def setAxes(self, ax):
        self.ax = ax

    def setTitle(self, title):
        self.ax.set_title(title)

    def xzplot(self, X, Y, xlabel, ylabel, varlabel):
        if(not self.ax.yaxis_inverted()):
            self.ax.invert_yaxis()
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.plot(X, Y, label=varlabel)
        labels = [tick.label for tick in self.ax.xaxis.get_major_ticks()[:]]
        for label in labels:
            label.set_rotation('vertical')
        plt.legend()
        self.ax.set_xlim(np.min(X), np.max(X))
        # Ugly hack to 'identify' model levels on Y axis
        if np.sum(Y%1)==0:
            self.ax.set_ylim(top=np.min(Y), bottom=np.max(Y))
            print 'identified integer Y-axis. Assuming model levels'
        else:
            self.ax.set_ylim(top=np.max(Y), bottom=np.min(Y))

    def timeline(self, X, Y, xlabel, ylabel, varlabel):
        if(self.ax.yaxis_inverted()):
            self.ax.invert_yaxis()
        self.ax.plot(X, Y, '-', label=varlabel)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        ytot = np.sum(Y, axis=0)
        yavg = ytot / Y.shape[0]
        self.ax.axhline(yavg, color='r', linestyle=':')
        self.ax.set_xlim(np.min(X), np.max(X))
        plt.legend()

    def timeline2d(self, X, Y, Z, xlabel, ylabel, zlabel):
        ymin = np.min(Y)
        ymax = np.max(Y)
        zmax = np.max(Z)
        zmin = np.min(Z)

        adjustTicks = False
        tickpwr = 0
        magdiff = 0
        norm = None
        print 'min=%s, max=%s'%(zmin, zmax)

        flatsort = np.sort(Z, axis=None)
        n = len(flatsort)
        z20 = flatsort[np.ceil(0.20*n)]
        z80 = flatsort[np.floor(0.80*n)]
        z01 = flatsort[np.ceil(0.01*n)]
        z99 = flatsort[np.floor(0.99*n)]
        tickpwr = np.floor(np.log10(z99))
        nlev = 500
        
        YY,XX = np.meshgrid(Y, X)
        
        self.ax.invert_yaxis()
        p = self.ax.contourf(XX, YY, Z, nlev, norm=norm)#, cmap='gist_stern')
        cb = self.fig.colorbar(p, ax=self.ax)
        cb.set_label(zlabel)


        self.axzlabel.update({self.currentAx:zlabel})
        self.axcb.update({self.currentAx:cb})
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_xlim(np.abs(X).min(), np.abs(X).max())
        self.ax.set_ylim(top=ymin, bottom=ymax)
