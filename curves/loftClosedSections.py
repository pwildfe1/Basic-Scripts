import rhinoscriptsyntax as rs
import math as m

def curvekey(curve):
    point = rs.CurveStartPoint(curve)
    return point[2]


def SortCurvesByZ(crvs):
    if not crvs: return
    sorted_crvs = sorted(crvs, key=curvekey)
    return sorted_crvs

def Main():
    crvs = rs.GetObjects("please select crvs",rs.filter.curve)
    crvs = SortCurvesByZ(crvs)
    div = 6
    pts = []
    basePts = []
    sects = []
    for i in range(div):
        param = rs.CurveParameter(crvs[0],i/div)
        basePts.append(rs.EvaluateCurve(crvs[0],param))
    for i in range(len(basePts)):
        for j in range(len(crvs)):
            param = rs.CurveClosestPoint(crvs[j],basePts[i])
            pts.append(rs.EvaluateCurve(crvs[j],param))
        sects.append(rs.AddInterpCurve(pts))
        pts = []
    return sects

Main()