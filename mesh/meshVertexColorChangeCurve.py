import rhinoscriptsyntax as rs
import math as m

def Main():
    meshes = rs.GetObjects("please select meshes",rs.filter.mesh)
    crvs = rs.GetObjects("please select curves",rs.filter.curve)
    thres = rs.GetReal("please enter threshold",10)
    power = rs.GetReal("please enter power rate",1)
    for i in range(len(meshes)):
        vertices = rs.MeshVertices(meshes[i])
        colors = []
        for j in range(len(vertices)):
            closePt = rs.PointClosestObject(vertices[j],crvs)[1]
            dist = rs.Distance(closePt,vertices[j])
            val = m.pow(dist/thres,power)*255
            if val>255: val = 255
            colors.append([val,val,val])
        rs.MeshVertexColors(meshes[i],colors)

Main()