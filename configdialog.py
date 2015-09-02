from cconfigdialog import Ui_ConfigDialog

class configDialog(Ui_ConfigDialog):
    def __init__(self, plotDialog):
        Ui_ConfigDialog.__init__(self)

        self.plotDialog = plotDialog

        self.plotToCBID = {}

        self.titleaxis_button.clicked.connect(self.plotDialog.set_xlabel)
        self.titleaxis_button.clicked.connect(self.plotDialog.set_ylabel)
        self.titleaxis_button.clicked.connect(self.plotDialog.set_title)
        self.titleaxis_button.clicked.connect(self.plotDialog.set_unit)
        self.activeax_comb.currentIndexChanged.connect(self.plotDialog.setActiveAx)
        
        self.onefig_cb.stateChanged.connect(self.plotDialog.setNAxes)

        self.plot_comb.currentIndexChanged.connect(self.plotDialog.changePlotType)

        self.legendedit_button.clicked.connect(self.plotDialog.editLegendList)
        
        plotDialog.registerConfigDialog(self)

        self.time = 0

    def setSliceTime(self, time):
        self.time = time

    def setPlotType(self, plotType):
        self.plot_comb.blockSignals(True)
        self.plot_comb.setCurrentIndex(self.plotToCBID[str(plotType)])
        self.plot_comb.blockSignals(False)

    def getPlotType(self):
        return self.plot_comb.currentText()

    def setAxes(self, xlabel, ylabel, zlabel, title):
        self.xlabel_field.setText(xlabel)
        self.ylabel_field.setText(ylabel)
        self.zlabel_field.setText(zlabel)
        self.title_field.setText(title)

    def getActiveAxId(self):
        return self.activeax_comb.currentIndex()

    def setLabels(self, labels):
        self.legend_list.clear()
        for l in labels:
            self.legend_list.addItem(l)

    def getLegendItemText(self):
        return self.legend_list.currentItem(), self.legendedit_field.text()
