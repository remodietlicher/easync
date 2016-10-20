import matplotlib.pyplot as plt
import numpy as np
import scipy
from matplotlib.colors import LogNorm
import matplotlib.ticker

llog = False
lnotlog = True

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

        flatsort = np.sort(Z[np.abs(Z) > 1e-15], axis=None)
        n = len(flatsort)
        if(n>10):
            z20 = flatsort[np.ceil(0.2*n)]
            z80 = flatsort[np.floor(0.8*n)]
            z01 = flatsort[np.ceil(0.01*n)]
            z99 = flatsort[np.floor(0.99*n)]
            tickpwr = np.floor(np.log10(z99))
        else:
            z20 = zmin
            z80 = zmax
            z01 = zmin
            z99 = zmax
            tickpwr = 0

        print 'z20=%s, z80=%s'%(z20, z80)

        if(z20 < 0 or z20 == z80):
            levels = np.linspace(zmin, zmax, 7)          
        else:
            tickpwr = max(np.floor(np.log10(np.abs(z99))), np.floor(np.log10(np.abs(z01))))

            magdiff = np.abs(np.log10(z20)-np.log10(z80))
            print 'magdiff:', magdiff
            if((magdiff>=6 or llog) and not lnotlog):
                norm = LogNorm()
                emin = np.ceil(np.log10(zmax))-6
                emax = np.ceil(np.log10(zmax))
                levels = np.logspace(emin, emax, 7)

            else:
                if(np.abs(z01-z99)>0):
                    levels = np.linspace(z01, z99, 7)
                else:
                    levels = np.linspace(zmin, zmax, 7)
                if(tickpwr != 0):
                    zlabel = r'$10^{%i}$ %s'%(tickpwr, zlabel)
                prettyticks = ['%.3f'%(v/10**tickpwr) for v in levels]
                # prettyticks = ['%.1g'%(v) for v in levels]
                adjustTicks = True
        
        YY,XX = np.meshgrid(Y, X)
        
        self.ax.invert_yaxis()
        if(norm):
            p = self.ax.contourf(XX, YY, Z, levels=levels, norm=norm)
        else:
            p = self.ax.contourf(XX, YY, Z, levels=levels, norm=norm, extend='both')
            p.cmap.set_under('b', alpha=0.3)
            p.cmap.set_over('r', alpha=0.3)
        cb = self.fig.colorbar(p, ax=self.ax)
        cb.set_label(zlabel)
        cb.locator = matplotlib.ticker.FixedLocator(levels)
        if(adjustTicks):
            cb.formatter = matplotlib.ticker.FixedFormatter(prettyticks)
            cb.update_ticks()


        self.axzlabel.update({self.currentAx:zlabel})
        self.axcb.update({self.currentAx:cb})
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_xlim(np.abs(X).min(), np.abs(X).max())
        self.ax.set_ylim(top=ymin, bottom=ymax)
