import rhinoscriptsyntax as rs
import math as m

def skeleton(geo,crvs):
    pts = []
    section = []
    split = False
    for i in range(len(crvs)):
        params = rs.CurveBrepIntersect(crvs[i],geo)
        for j in range(len(params)):
            if rs.IsPoint(params[j]) and split==False:
                param = rs.CurveClosestPoint(crvs[i],params[j])
                crvs[i] = rs.SplitCurve(crvs[i],param)[0]
                pts.append(param[j])
                split = True
    bone = rs.AddInterpCurve(pts)
    bone = rs.PullCurve(geo,bone,True)
    return bone

def Main():
    heart = rs.GetObject("please select center point",rs.filter.polysurface)
    spine = rs.GetObject("please select curve",rs.filter.curve)
    heartPt = rs.SurfaceAreaCentroid(heart)[0]
    divPts = rs.DivideCurveLength(spine,1)
    connections = []
    for i in range(len(divPts)):
        connections.append(rs.AddLine(divPts[i],heartPt))
    bones = skeleton(heart,connections)
    return bones


Main()