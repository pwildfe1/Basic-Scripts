import rhinoscriptsyntax as rs
import math as m

def normalRange(vals,newMax,newMin):
    oldMin = vals[0]
    oldMax = vals[0]
    for i in range(len(vals)):
        if vals[i]<oldMin:
            oldMin = vals[i]
        if vals[i]>oldMax:
            oldMax = vals[i]
    for i in range(len(vals)):
        vals[i] = (vals[i]-oldMin)/(oldMax-oldMin)*(newMax-newMin) + newMin
    return vals
