import rhinoscriptsyntax as rs
import math as m

def matchOrder(list,ref):
    indexes = []
    adjusted = []
    newList = []
    for i in range(len(ref)):
        minimum = 10000000000
        index = 0
        for j in range(len(ref)):
            if ref[j]<minimum and j not in indexes:
                minimum = ref[j]
                index = j
        indexes.append(index)
        adjusted.append(minimum)
    print(adjusted)
    for i in range(len(indexes)):
        newList.append(list[indexes[i]]) 
    return newList

def alignCrvs(crvs):
    for i in range(len(crvs)-1):
        vec01 = rs.VectorCreate(rs.CurveStartPoint(crvs[i]),rs.CurveEndPoint(crvs[i]))
        vec02 = rs.VectorCreate(rs.CurveStartPoint(crvs[i+1]),rs.CurveEndPoint(crvs[i+1]))
        if rs.VectorDotProduct(vec01,vec02)<0:
            rs.ReverseCurve(crvs[i+1])
    return crvs


def Main():
    crvs = rs.GetObjects("please select crvs",rs.filter.curve)
    ref = rs.GetObject("please select ref pt",rs.filter.point)
    num = rs.GetInteger("please select number of contours",4)
    contours = []
    dist = []
    for i in range(len(crvs)):
        midPt = rs.CurveMidPoint(crvs[i])
        dist.append(rs.Distance(ref,midPt))
    crvs = matchOrder(crvs,dist)
    crvs = alignCrvs(crvs)
    for i in range(num+1):
        pts = []
        for j in range(len(crvs)):
            normP = (1/num)*i
            param = rs.CurveParameter(crvs[j],normP)
            pts.append(rs.EvaluateCurve(crvs[j],param))
        contours.append(rs.AddInterpCurve(pts))
    return pts

Main()