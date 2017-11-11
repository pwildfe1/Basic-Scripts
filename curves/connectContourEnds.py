import rhinoscriptsyntax as rs
import math as m

def orientCrvs(crvs,pt):
    dists = []
    indexes = []
    for i in range(len(crvs)):
        dists.append(rs.Distance(rs.CurveMidPoint(crvs[i]),pt))
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
    crvs = orientCrvs(crvs,pt)
    crvs = alignCrvs(crvs)
    sts = []
    ens = []
    for i in range(len(crvs)):
        sts.append(rs.CurveStartPoint(crvs[i]))
        ens.append(rs.CurveEndPoint(crvs[i]))
    rs.AddCurve(ens)
    rs.AddCurve(sts)

Main()