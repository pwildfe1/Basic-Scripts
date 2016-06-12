import rhinoscriptsyntax as rs
import math as m


def Main():
    obj = rs.GetObject("please select surface/polysurface to place ptGrid on")
    xSpace = rs.GetReal("please enter cell width",50)
    ySpace = rs.GetReal("please enter cell length",xSpace)
    pts = []
    surface = False
    if rs.IsSurface(obj):
        surface=True
    box = rs.BoundingBox(obj)
    vecX = rs.VectorUnitize(rs.VectorCreate(box[1],box[0]))
    vecY = rs.VectorUnitize(rs.VectorCreate(box[3],box[0]))
    vecZ = rs.VectorCreate(box[4],box[0])
    for i in range(int(rs.Distance(box[1],box[0])/xSpace)):
        for j in range(int(rs.Distance(box[3],box[0])/ySpace)):
            pt = rs.PointAdd(box[0],[i*xSpace,j*ySpace,0])
            crv = rs.AddLine(pt,rs.PointAdd(pt,vecZ))
            if surface == False:
                intersect = rs.CurveMeshIntersection(crv,obj)
                if intersect!=None:
                    intersect = rs.CurveMeshIntersection(crv,obj)[0]
                    pts.append(intersect)
                    rs.AddPoint(intersect)
                else:
                    pts.append(pt)
            rs.DeleteObject(crv)
    return pts

Main()