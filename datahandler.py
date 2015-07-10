import numpy as np
from copy import copy
from str2eq import evalEq, getVars

class dataHandler:
    def __init__(self, data, equation):
        self.data = data
        self.time = data.variables['time']
        self.timeunit = data.variables['time'].units
        vardict = {key:var[:] for key,var in data.variables.iteritems()}
        print vardict.keys()
        self.var = np.squeeze(evalEq(equation, vardict))
        self.varcpy = copy(self.var)
        self.varunit = 'combined'
        self.varlabel = equation
        self.longname = equation
        self.ndim = len(self.var.shape)
        self.ndimtot = len(self.var.shape)
        self.nlvl = self.var.shape[0]
        try:
            self.height = data.variables['lev'][:]
            self.heightunit = 'pressure [Pa]'
        except:
            self.height = np.linspace(0, self.nlvl, self.nlvl+1)
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
        
#    def __init__(self, data, varname=''):
#        self.data = data
#        self.time = data.variables['time'][:]
#        self.timeunit = data.variables['time'].units
#        self.var = np.squeeze(data.variables[varname][:])
#        self.varcpy = copy(self.var)
#        self.ndim = len(self.var.shape)
#        self.nlvl = self.var.shape[0]
#        try:
#            self.height = data.variables['lev'][:]
#            self.heightunit = 'pressure [Pa]'
#        except:
#            self.height = np.linspace(0, self.nlvl, self.nlvl+1)
#            self.heightunit = 'model level'
#        self.varunit = ''
#        self.varlabel = varname
#        self.longname = varname
#        try:
#            self.varunit = data.variables[varname].units
#        except:
#            print 'variable is dimensionless or unit not given'
#        try:
#            self.longname = data.variables[varname].long_name
#        except:
#            print 'no variable information.'

    def integrateZ(self):
        self.var = np.sum(self.var, axis=1)/self.var.shape[1]
        self.ndim = len(self.var.shape)

    def integrateT(self):
        self.var = np.sum(self.var, axis=0)/self.var.shape[0]
        self.ndim = len(self.var.shape)

    def restore(self):
        self.var = copy(self.varcpy)
        self.ndim = len(self.var.shape)
