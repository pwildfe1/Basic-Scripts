import rhinoscriptsyntax as rs
import math as m

def SortCurvesByPt(curves,pt):
    indexes = []
    distances = []
    sorted = []
    min = 1000000000
    for i in range(len(curves)):
        param = rs.CurveClosestPoint(curves[i],pt)
        crvPt = rs.EvaluateCurve(curves[i],param)
        distances.append(rs.Distance(crvPt,pt))
    for i in range(len(curves)):
        for j in range(len(distances)):
            if distances[j]<min:
                min = distances[j]
                index = j
        indexes.append(index)
        sorted.append(curves[index])
        distances[index] = 1000000000
        min = 1000000000
    return sorted


def collectIntersections(set,cuts):
    intersectPts = []
    for i in range(len(cuts)):
        intersect = rs.CurveCurveIntersection(set,cuts[i])
        if intersect!=None:
            intersectPts.append(intersect[0][1])
    return intersectPts



def Main():
    crvs = rs.GetObjects("please select grid curves",rs.filter.curve)
    refPt = rs.GetObject("please select reference pt",rs.filter.point)
    tolerance = rs.GetReal("please enter tolerance",10)
    height = rs.GetReal("please enter depth",-3.5)
    crvX = []
    crvY = []
    pts = []
    posts = []
    vecX = rs.VectorCreate(rs.CurveEndPoint(crvs[0]),rs.CurveStartPoint(crvs[0]))
    for i in range(len(crvs)):
        vec = rs.VectorCreate(rs.CurveEndPoint(crvs[i]),rs.CurveStartPoint(crvs[i]))
        if rs.VectorAngle(vec,vecX)<tolerance:
            crvX.append(crvs[i])
        else:
            crvY.append(crvs[i])
    crvX = SortCurvesByPt(crvX,refPt)
    crvY = SortCurvesByPt(crvY,refPt)
    for i in range(len(crvX)):
        pts.append(collectIntersections(crvX[i],crvY))
    for i in range(len(pts)):
        for j in range(len(pts[i])):
            endPt = rs.PointAdd(pts[i][j],[0,0,height])
            posts.append(rs.AddLine(pts[i][j],endPt))

Main()