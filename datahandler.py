import numpy as np
from copy import copy
from str2eq import evalEq, getVars

class dataHandler:
    def __init__(self, data, equation):
        self.data = data
        self.time = data.variables['time']
        self.timeunit = data.variables['time'].units
        vardict = {key:var[:] for key,var in data.variables.iteritems()}
        self.var = np.squeeze(evalEq(equation, vardict))
        self.varcpy = copy(self.var)
        self.varunit = 'combined'
        self.varlabel = equation
        self.longname = equation
        self.ndim = len(self.var.shape)
        self.ndimtot = len(self.var.shape)
        if(self.ndimtot > 1):
            self.nlvl = self.var.shape[1]
        else:
            self.nlvl = 0
        try:
            self.height = data.variables['lev'][:]
            self.heightunit = 'pressure [Pa]'
        except:
            self.height = np.linspace(0, self.nlvl-1, self.nlvl)
            self.heightunit = 'model level'
        variables = getVars(equation)
        if(len(variables) == 1):
            varname = variables[0]
            self.varunit = ''
            self.varlabel = varname
            self.longname = varname
            try:
                self.varunit = data.variables[varname].units
            except:
                print 'variable is dimensionless or unit not given'
            try:
                self.longname = data.variables[varname].long_name
            except:
                print 'no variable information.'

        self.hasTimeVal = False
        self.hasHeightVal = False
        self.defaultPlotType = ''
        if(self.ndim == 1 and len(self.time)==len(self.var)):
            self.hasTimeVal = True
            self.defaultPlotType = 'TIME'
        elif(self.ndim == 1):
            self.hasHeightVal = True
            self.defaultPlotType = 'HEIGHT'
        elif(self.ndim == 2):
            self.hasTimeVal = True
            self.hasHeightVal = True
            self.defaultPlotType = 'TIMEHEIGHT'

    def integrateZ(self):
        self.var = np.sum(self.var, axis=1)/self.var.shape[1]
        self.ndim = len(self.var.shape)

    def integrateT(self):
        self.var = np.sum(self.var, axis=0)/self.var.shape[0]
        self.ndim = len(self.var.shape)

    def getNearestTimeID(self, t):
        idx = (np.abs(self.time[:] - t)).argmin()
        return idx

    def restore(self):
        self.var = copy(self.varcpy)
        self.ndim = len(self.var.shape)

    def getTimeValue(self):
        if(self.hasTimeVal and not self.hasHeightVal):
            return self.var
        elif(self.hasTimeVal and self.hasHeightVal):
            return np.sum(self.var, axis=1)/self.var.shape[1]
        else:
            return None

    def getHeightValue(self):
        if(self.hasHeightVal and not self.hasTimeVal):
            return self.var
        elif(self.hasTimeVal and self.hasHeightVal):
            return np.sum(self.var, axis=0)/self.var.shape[0]
        else:
            return None

    def getTimeHeightMatrix(self):
        if(self.hasHeightVal and self.hasTimeVal):
            return self.var
        else:
            return None

    def getTimeSlice(self, time):
        if(self.hasTimeVal and self.hasHeightVal):
            idx = self.getNearestTimeID(time)
            return self.var[idx]
        else:
            return None

    def writeVariableToFile(self):
        self.data.variables[self.varlabel][:] = self.var[:]
