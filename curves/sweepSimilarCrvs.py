import rhinoscriptsyntax as rs
import math as m

def sweepSimilar(rail01,rail02):
    pt01 = rs.CurveMidPoint(rail01)
    param01 = rs.CurveClosestPoint(rail01,pt01)
    tan01 = rs.CurveTangent(rail01,param01)
    param02 = rs.CurveClosestPoint(rail02,pt01)
    pt02 = rs.EvaluateCurve(rail02,param02)
    tan02 = rs.CurveTangent(rail02,param02)
    if(rs.VectorDotProduct(tan01,tan02)<0):
        rs.ReverseCurve(rail02)
    spine = rs.AddCurve([pt01,pt02])
    srf = rs.AddSweep2([rail01,rail02],[spine],True)
    return srf


def Main():
    rail01 = rs.GetObject("please select first rail",rs.filter.curve)
    rail02 = rs.GetObject("please select second rail",rs.filter.curve)
    sweepSimilar(rail01,rail02)


Main()