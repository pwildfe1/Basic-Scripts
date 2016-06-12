import rhinoscriptsyntax as rs
import math as m

def remapNormalized(start,end,newStart,newEnd,value):
    newVal = (value-start)/(end-start)*(newEnd-newStart)+newStart
    return newVal

def Main():
    #you need to enter values
    newNum = []
    start = min(num)
    end = max(num)
    for i in range(len(num)):
        newNum.append(remapNormalized(start,end,.25,.8,num[i]))
    return newNum

a = Main()