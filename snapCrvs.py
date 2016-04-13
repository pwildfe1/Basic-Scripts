import rhinoscriptsyntax as rs
import math as m

def Main():
    guides = rs.GetObjects("please select guides",rs.filter.curve)
    skeleton = rs.GetObjects("please select ribs",rs.filter.curve)
    reso = rs.GetInteger("please enter resolution",10)
    pts = []
    for i in range(len(skeleton)):
        pts.append(rs.DivideCurve(skeleton[i],reso))
    rs.DeleteObjects(skeleton)
    for i in range(len(pts)):
        pts[i][0] = rs.PointClosestObject(pts[i][0],guides)[1]
        pts[i][reso] = rs.PointClosestObject(pts[i][reso],guides)[1]
    for i in range(len(pts)):
        skeleton[i] = rs.AddCurve(pts[i])
    return skeleton 

Main()