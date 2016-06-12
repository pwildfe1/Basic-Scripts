import rhinoscriptsyntax as rs
import math as m

def skeleton(geo,crvs):
    pts = []
    section = []
    for i in range(len(crvs)):
        params = rs.CurveBrepIntersect(crvs[i],geo)
        for j in range(len(params)):
            if len(params[j])>0:
                param = rs.CurveClosestPoint(crvs[i],params[j][0])
                crvs[i] = rs.SplitCurve(crvs[i],param)[1]
                for k in range(len(params[j])):
                    if rs.IsPoint(params[j][k]):
                        rs.DeleteObject(params[j][k])
        pts.append(rs.CurveStartPoint(crvs[i]))
    bone = rs.AddInterpCurve(pts)
    #bone = rs.PullCurve(geo,bone,True)
    return bone

def skeletonBrep(geo,crvs):
    pts = []
    section = []
    for i in range(len(crvs)):
        pts.append(rs.CurveEndPoint(crvs[i]))
    bone = rs.AddInterpCurve(pts)
    bone = rs.PullCurve(geo,bone,True)
    return bone

def Main():
    heart = rs.GetObject("please select center point",rs.filter.polysurface)
    spine = rs.GetObject("please select curve",rs.filter.curve)
    reso = rs.GetReal("please enter desired length b/w spines",1)
    heartPt = rs.SurfaceAreaCentroid(heart)[0]
    divPts = rs.DivideCurveLength(spine,reso)
    connections = []
    for i in range(len(divPts)):
        endPt = rs.PointClosestObject(divPts[i],[heart])[1]
        connections.append(rs.AddLine(divPts[i],endPt))
        #connections.append(rs.AddLine(divPts[i],heartPt))
    #bones = skeleton(heart,connections)
    bones = skeletonBrep(heart,connections)
    return bones


Main()