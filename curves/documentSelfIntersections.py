import rhinoscriptsyntax as rs
import math as m

def Main():
    crvs = rs.GetObjects("please select curves",rs.filter.curve)
    for i in range(len(crvs)):
        if rs.CurveLength(crvs[i])<.4:
            rs.DeleteObject(crvs[i])
    for i in range(len(crvs)):
        if rs.IsCurve(crvs[i]):
            intersect = rs.CurveCurveIntersection(crvs[i])
            if intersect!=None:
                for j in range(len(intersect)):
                    rs.AddPoint(intersect[j][1])

Main()