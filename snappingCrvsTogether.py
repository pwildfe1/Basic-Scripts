import rhinoscriptsyntax as rs
import math as m

def Main():
    crvs = rs.GetObjects("please select curves to connect",rs.filter.curve)
    objs = rs.GetObjects("please enter exclusion volumes",rs.filter.polysurface)
    thres = rs.GetReal("please enter threshold radius",.4)
    connections = []
    pts = []
    for i in range(len(crvs)):
        pts.append(rs.CurveStartPoint(crvs[i]))
    for i in range(len(pts)):
        minDist = 200
        dist =[]
        for j in range(len(crvs)):
            if i!=j:
                param = rs.CurveClosestPoint(crvs[j],pts[i])
                closePt = rs.EvaluateCurve(crvs[j],param)
                dist.append(rs.Distance(pts[i],closePt))
            else:
                dist.append(2000)
        print len(dist)
        for j in range(len(dist)):
            if dist[j]<minDist:
                minDist = dist[j]
                close = j
        if minDist>thres and minDist<2:
            print minDist
            connections.append(rs.AddLine(pts[i],pts[close]))
        dist = []
    """pts = []
    for i in range(len(crvs)):
        pts.append(rs.CurveEndPoint(crvs[i]))
    for i in range(len(pts)):
        minDist = 200
        dist = []
        check = True
        for j in range(len(objs)):
            if rs.IsPointInSurface(objs[j],pts[i]):
                check = False
        for j in range(len(crvs)):
            if i!=j and check==True:
                param = rs.CurveClosestPoint(crvs[j],pts[i])
                closePt = rs.EvaluateCurve(crvs[j],param)
                dist.append(rs.Distance(pts[i],closePt))
            else:
                dist.append(2000)
        for j in range(len(dist)):
            if dist[j]<minDist:
                minDist = dist[j]
                close = j
        if minDist>thres and minDist<2:
            connections.append(rs.AddLine(pts[i],pts[close]))"""
    return connections

Main()