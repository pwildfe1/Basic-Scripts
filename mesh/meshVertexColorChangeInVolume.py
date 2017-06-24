import rhinoscriptsyntax as rs
import math as m

def Main():
    mesh = rs.GetObject("select mesh",rs.filter.mesh)
    filters = rs.GetObjects("select filters",rs.filter.polysurface)
    vert = rs.MeshVertices(mesh)
    colors = []
    filterIndex = []
    cntPts = []
    for i in range(len(filters)):
        cntPts.append(rs.SurfaceAreaCentroid(filters[i])[0])
    for i in range(len(vert)):
        color = [255,255,255]
        index = len(filters)
        for j in range(len(filters)):
            if rs.IsPointInSurface(filters[j],vert[i]):
                color = [0,0,0]
                index = j
        colors.append(color)
    for i in range(len(colors)):
        if colors[i] != [255,255,255]:
            index = rs.PointArrayClosestPoint(cntPts,vert[i])
            dist = rs.Distance(vert[i],cntPts[index])
            vec = rs.VectorUnitize(rs.VectorCreate(vert[i],cntPts[index]))
            factor = abs(rs.VectorDotProduct(vec,[1,0,0]))
            factor = dist#*(factor)
            if factor>255:
                factor = 255
            colors[i]=[factor,factor,factor]
    rs.MeshVertexColors(mesh,colors)
    return colors

Main()