import rhinoscriptsyntax as rs
import math as m

def Main():
    firstCrv = rs.GetObject("please select first curve",rs.filter.curve)
    secondCrv = rs.GetObject("please select second curve",rs.filter.curve)
    crvs = [firstCrv,secondCrv]
    pts01 = []
    pts02 = []
    connections = []
    steps = 5
    for i in range(steps+1):
        param = rs.CurveParameter(crvs[0],i/(steps))
        pt01 = rs.EvaluateCurve(crvs[0],param)
        pts01.append(pt01)
        closeParam = rs.CurveClosestPoint(crvs[1],pt01)
        pt02 = rs.EvaluateCurve(crvs[1],closeParam)
        pts02.append(pt02)
        connections.append(rs.AddLine(pt01,pt02))
    newSrf = rs.AddSweep2(crvs,connections)
    rs.DeleteObjects(connections)

Main()