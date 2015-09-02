import matplotlib.pyplot as plt
import numpy as np

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
        #ax.set_ylim(ymin=zbot,ymax=ztop)
        #ax.set_xlim(xmin=np.min(self.var), xmax=np.max(self.var))
        labels = [tick.label for tick in self.ax.xaxis.get_major_ticks()[:]]
        for label in labels:
            label.set_rotation('vertical')
        plt.legend()

    def timeline(self, X, Y, xlabel, ylabel, varlabel):
        if(self.ax.yaxis_inverted()):
            self.ax.invert_yaxis()
        self.ax.plot(X, Y, '-', label=varlabel)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        ytot = np.sum(Y, axis=0)
        yavg = ytot / Y.shape[0]
        #self.ax.set_title('integral=%f, average=%f'%(ytot, yavg))
        self.ax.axhline(yavg, color='r', linestyle=':')
        plt.legend()

    def timeline2d(self, X, Y, Z, xlabel, ylabel, zlabel):
        ymin = np.min(Y)
        ymax = np.max(Y)

        YY,XX = np.meshgrid(Y, X)

        flat = Z.flatten()
        flen = len(flat)
        colormax = np.sort(flat)[99*flen/100.0]
        #colormax = np.max(self.var)
        colormin = np.min(Z)
        
        self.ax.invert_yaxis()
        p = self.ax.pcolor(XX, YY, Z, vmin=colormin, vmax=colormax)
        cb = self.fig.colorbar(p, ax=self.ax)
        cb.set_label(zlabel)
        self.axzlabel.update({self.currentAx:zlabel})
        self.axcb.update({self.currentAx:cb})
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_xlim(np.abs(X).min(), np.abs(X).max())
        self.ax.set_ylim(top=ymin, bottom=ymax)

        #yticks = np.append(np.arange(0, np.max(z), 10000),np.min(z))#z
        #yticks[0] = zmax
        #ylabel = [int(p/100.) for p in yticks]
        #plt.yticks(yticks, ylabel)
