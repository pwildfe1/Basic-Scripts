import rhinoscriptsyntax as rs
import math as m

def Main():
    crvs = rs.GetObjects("please select crvs to filter",rs.filter.curve)
    polySrf = rs.GetObject("please select polysrf to filter with",rs.filter.polysurface)
    for i in range(len(crvs)):
        start = rs.CurveStartPoint(crvs[i])
        end = rs.CurveEndPoint(crvs[i])
        if rs.IsPointInSurface(polySrf,start)==False or rs.IsPointInSurface(polySrf,end)==False:
            rs.DeleteObject(crvs[i])
    return crvs

Main()