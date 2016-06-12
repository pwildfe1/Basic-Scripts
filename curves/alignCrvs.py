import rhinoscriptsyntax as rs
import math as m

def alignCrvs(baseCrv,crvs):
    baseVec = rs.VectorCreate(rs.CurveEndPoint(baseCrv),rs.CurveStartPoint(baseCrv))
    for i in range(len(crvs)):
        vec = rs.VectorCreate(rs.CurveEndPoint(crvs[i]),rs.CurveStartPoint(crvs[i]))
        if rs.VectorDotProduct(vec,baseVec)<0:
            rs.ReverseCurve(crvs[i])
    return crvs

def Main():
    baseCrv = rs.GetObject("please enter curve to align to",rs.filter.curve)
    crvs = rs.GetObjects("please select curves to align",rs.filter.curve)
    return alignCrvs(baseCrv,crvs)

Main()