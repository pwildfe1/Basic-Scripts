import rhinoscriptsyntax as rs
import math as m

def Main():
    mesh = rs.GetObject("select mesh",rs.filter.mesh)
    cntPts = rs.GetObjects("select points",rs.filter.point)
    power = rs.GetReal("select power distribution",1)
    vert = rs.MeshVertices(mesh)
    distances = []
    colors = []
    filterIndex = []
    for i in range(len(vert)):
        color = [255,255,255]
        colors.append(color)
    for i in range(len(vert)):
        index = rs.PointArrayClosestPoint(cntPts,vert[i])
        dist = rs.Distance(vert[i],cntPts[index])
        distances.append(dist)
    maxDist = distances[0]
    minDist = distances[0]
    for i in range(len(distances)):
        if distances[i]>maxDist:
            maxDist = distances[i]
        if distances[i]<minDist:
            minDist = distances[i]
    rangeDist = maxDist-minDist
    for i in range(len(vert)):
        factor = m.pow((distances[i]-minDist)/(rangeDist),power)*255
        if factor>255:
            value = 255
        else:
            value = factor
        #rs.AddCircle(vert[i],.33*(1.2-value/255))
        colors[i]=[factor,factor,factor]
    rs.MeshVertexColors(mesh,colors)
    return colors

Main()