#!/usr/bin/env python

from cmodifydialog import Ui_ModifyDialog
from mplcanvas import modifyCanvas

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class modifyDialog(Ui_ModifyDialog):
    def __init__(self, data):
        Ui_ModifyDialog.__init__(self)
        self.data = data

        self.canvas = modifyCanvas(self)
        toolbar = NavigationToolbar(self.canvas, parent=self)

        self.plotLayout.addWidget(toolbar)
        self.plotLayout.addWidget(self.canvas)

        self.canvas.plot_figure(data, 0)
        
        self.use_for_all_timesteps_checkbox.stateChanged.connect(self.applyToAllTmsts)


    def applyToAllTmsts(self):
        return
