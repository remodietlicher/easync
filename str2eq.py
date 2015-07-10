import numpy as np
from copy import copy, deepcopy

ops = ['+', '-', '*', '/', '(', ')']

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
    print varlist
    return varlist

def evalEq(string, varDict):
    pos = 0
    zero = 0
    nested = [zero]
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
            value = copy(varDict[var])
            evaluate = True
        if(evaluate):
            #print value, nLvl, nested[nLvl], lastOp
            #print nested[nLvl].shape
            if(lastOp == 'None'):
                nested[nLvl] = value
            elif(lastOp == '+'):
                nested[nLvl][:] += value
            elif(lastOp == '-'):
                nested[nLvl][:] -= value
            elif(lastOp == '*'):
                nested[nLvl][:] *= value
            elif(lastOp == '/'):
                nested[nLvl][:] /= value+1e-12
            #print nested[nLvl].shape
                    
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
    #else:
    #    print 'result:', nested[0]
        
    return nested[0]
        
        
