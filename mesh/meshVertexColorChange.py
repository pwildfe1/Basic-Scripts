import rhinoscriptsyntax as rs
import math as m

def Main():
    meshes = rs.GetObjects("please select meshes",rs.filter.mesh)
    container = rs.GetObject("please select filter volume",rs.filter.polysurface)
    for i in range(len(meshes)):
        vertices = rs.MeshVertices(meshes[i])
        colors = []
        for j in range(len(vertices)):
            if rs.IsPointInSurface(container,vertices[j]):
                colors.append([255,0,0])
            else:
                colors.append([0,0,0])
        rs.MeshVertexColors(meshes[i],colors)

Main()