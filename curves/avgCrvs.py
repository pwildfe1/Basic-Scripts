import rhinoscriptsyntax as rs
import math as m

def Main():
    crvs = rs.GetObjects("please select crvs to average",rs.filter.curve)
    avgPts = []
    allPts = []
    pts = []
    divPts = rs.DivideCurve(crvs[0],40)
    for i in range(len(divPts)):
        for j in range(len(crvs)):
            param = rs.CurveClosestPoint(crvs[j],divPts[i])
            pts.append(rs.EvaluateCurve(crvs[j],param))
        allPts.append(pts)
        pts = []
    for i in range(len(allPts)):
        sum = [0,0,0]
        for j in range(len(allPts[i])):
            sum = rs.PointAdd(allPts[i][j],sum)
        avgPts.append(sum/len(allPts[i]))
    avgCrv = rs.AddCurve(avgPts)
    return avgCrv

Main()