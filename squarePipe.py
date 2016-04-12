import rhinoscriptsyntax as rs
import math as m

def squarePipeOnSrf(crv,srfs,width,height):
    divPts = rs.DivideCurve(crv,100)
    sections = []
    for i in range(len(divPts)):
        obj = rs.PointClosestObject(divPts[i],srfs)[0]
        param = rs.SurfaceClosestPoint(obj,divPts[i])
        norm = rs.SurfaceNormal(obj,param)
        param = rs.CurveClosestPoint(crv,divPts[i])
        tan = rs.CurveTangent(crv,param)
        plane = rs.PlaneFromNormal(divPts[i],tan,norm)
        sections.append(rs.AddRectangle(plane,width,height))
    pipe = rs.AddSweep1(crv,sections)
    rs.DeleteObjects(sections)
    return pipe

def squarePipe(crv,width,height,subDiv,xAxis=[]):
    divPts = rs.DivideCurve(crv,subDiv)
    sections = []
    for i in range(len(divPts)):
        param = rs.CurveClosestPoint(crv,divPts[i])
        tan = rs.CurveTangent(crv,param)
        if len(xAxis)>0:
            plane = rs.PlaneFromNormal(divPts[i],tan,xAxis)
        else:
            plane = rs.PlaneFromNormal(divPts[i],tan)
        sections.append(rs.AddRectangle(plane,width,height))
    pipe = rs.AddSweep1(crv,sections)
    rs.DeleteObjects(sections)
    return pipe

def Main():
    srfs = rs.GetObjects("please select surfaces")
    crvs = rs.GetObjects("please select curves to squarePipe on surface",rs.filter.curve)
    spines = rs.GetObjects("please select curves to squarePipe",rs.filter.curve)
    subDiv = rs.GetInteger("please enter resolution",10)
    pipes = []
    copySrfs = []
    for i in range(len(srfs)):
        if rs.IsPolysurface(srfs[i]):
            copySrfs.extend(rs.ExplodePolysurfaces(srfs[i]))
        else:
            copySrfs.append(rs.CopyObject(srfs[i]))
    for i in range(len(crvs)):
        pipes.append(squarePipeOnSrf(crvs[i],copySrfs,.0254,.05))
    for i in range(len(spines)):
        crv = rs.PointClosestObject(rs.CurveStartPoint(spines[i]),crvs)[0]
        param = rs.CurveClosestPoint(crv,rs.CurveStartPoint(spines[i]))
        xAxis = rs.CurveTangent(crv,param)
        pipes.append(squarePipe(spines[i],.0254,.0125,subDiv,xAxis))
    rs.DeleteObjects(copySrfs)
    return pipes


Main()