import numpy as np
from copy import copy, deepcopy

ops = ['+', '-', '*', '/', '(', ')']
old_err_state = np.seterr(divide='raise')
ignored_states = np.seterr(**old_err_state)
meps = np.finfo(np.float32).eps
print 'machine precision for %s: %s'%('np.float32', meps)

def getNext(string, pos):
    var = ''
    i = pos
    loop = True
    while(loop):
        #print i
        if(i < len(string)):
            s = string[i]
            if(s in ops):
                if(var == ''):
                    var = s
                    i += 1
                    loop = False
                else:
                    loop = False
            elif(s != ' '):
                var += s
                i += 1
        else:
            loop = False
    return i, var

def getVars(string):
    pos = 0
    varlist = []
    while(pos < len(string)):
        pos, var = getNext(string, pos)
        if var not in ops:
            varlist.append(var)
    return varlist

def evalEq(string, varDict):
    pos = 0
    zero = 0
    nested = [zero]
    nestedStr = ['']
    nestedOp = ['+']
    nLvl = 0
    lastOp = 'None'
    while(pos < len(string)):
        pos, var = getNext(string, pos)
        #print var
        evaluate = False
        #print nested
        if(var==')'):
            if(nLvl > 0):
                value = nested.pop()
                lastOp = nestedOp.pop()
                nLvl -= 1
                evaluate = True
            else:
                print 'missing "("'
                return None
        if(var not in ops):
            value = varDict[var]
            evaluate = True
        if(evaluate):
            value = np.where(np.abs(value)==0, 0, value)
            if(lastOp == 'None'):
                nested[nLvl] = copy(value)
            elif(lastOp == '+'):
                nested[nLvl][:] += value
            elif(lastOp == '-'):
                nested[nLvl][:] -= value
            elif(lastOp == '*'):
                nested[nLvl][:] *= value
            elif(lastOp == '/'):
                zeros = np.zeros(value.shape)
                nested[nLvl][:] = np.where(np.abs(value)==0, 0, nested[nLvl][:]/value)
                    
        if(var == '('):
            nLvl += 1
            nested.append(zero)
            nestedOp.append(lastOp)
            lastOp = 'None'
        else:
            lastOp = var

    if(nLvl > 0):
        print 'missing ")"'
        return None
        
    return nested[0]
        
        
