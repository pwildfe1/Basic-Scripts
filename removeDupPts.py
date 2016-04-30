import rhinoscriptsyntax as rs
import math as m

def removeDup(freePts):
    pts=[]
    for i in range(len(freePts)):
        pts.append(freePts[i])
    for i in range(len(pts)):
        count=0
        dup=True
        while dup==True:
            index=freePts.index(pts[i])
            test=freePts.pop(freePts.index(pts[i]))
            if pts[i] in freePts:
                freePts.pop(freePts.index(pts[i]))
            if not pts[i] in freePts:
                freePts.insert(index,pts[i])
                dup=False
    return freePts

def Main():
    selectPts = rs.GetObjects("please select points to remove duplicates",rs.filter.point)
    selectPts = removeDup(selectPts)
    return selectPts