import rhinoscriptsyntax as rs
import math as m

def orientCrvs(crvs,pt,refLine):
    dists = []
    indexes = []
    ref = rs.VectorCreate(rs.CurveEndPoint(refLine),rs.CurveStartPoint(refLine))
    for i in range(len(crvs)):
        vec = rs.VectorCreate(rs.CurveMidPoint(crvs[i]),pt)
        amnt = rs.VectorDotProduct(vec,ref)
        dists.append(amnt)
    for i in range(len(dists)):
        minimum = 10000000000000000000000000000000000
        for j in range(len(dists)):
            if dists[j]<minimum and j not in indexes:
                index = j
                minimum = dists[j]
        indexes.append(index)
    ordered = []
    for i in range(len(indexes)):
        ordered.append(crvs[indexes[i]])
    return ordered

def alignCrvs(crvs):
    ref = rs.VectorCreate(rs.CurveEndPoint(crvs[0]),rs.CurveStartPoint(crvs[0]))
    ref = rs.VectorUnitize(ref)
    for i in range(len(crvs)):
        vec = rs.VectorCreate(rs.CurveEndPoint(crvs[0]),rs.CurveStartPoint(crvs[0]))
        vec = rs.VectorUnitize(vec)
        if rs.VectorDotProduct(vec,ref)<0:
            rs.ReverseCurve(crvs[i])
    return crvs

def Main():
    crvs = rs.GetObjects("please select crvs to connect",rs.filter.curve)
    pt = rs.GetObject("please select orientation point",rs.filter.point)
    refLine = rs.GetObject("please select reference vector line",rs.filter.curve)
    crvs = orientCrvs(crvs,pt,refLine)
    crvs = alignCrvs(crvs)
    sts = []
    ens = []
    for i in range(len(crvs)):
        sts.append(rs.CurveStartPoint(crvs[i]))
        ens.append(rs.CurveEndPoint(crvs[i]))
    rs.AddInterpCurve(ens)
    rs.AddInterpCurve(sts)

Main()