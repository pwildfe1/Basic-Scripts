import rhinoscriptsyntax as rs
import math as m

def Main():
    mesh = rs.GetObject("please select mesh to trim",rs.filter.mesh)
    vol = rs.GetObject("please select bounding volume to omit",rs.filter.polysurface)
    ang = rs.GetReal("please enter angle of filter",60)
    norms = rs.MeshFaceNormals(mesh)
    faceCnts = rs.MeshFaceCenters(mesh)
    meshCnt = rs.MeshAreaCentroid(mesh)
    fVert = rs.MeshFaceVertices(mesh)
    meshVert = rs.MeshVertices(mesh)
    newMeshes = []
    newMeshVert = []
    newFaceIndex = []
    num = 0
    for i in range(len(faceCnts)):
        if rs.IsPointInSurface(vol,faceCnts[i])==False:
            compVec = rs.VectorCreate(meshCnt,faceCnts[i])
            if rs.VectorDotProduct(norms[i],compVec)>m.cos(ang*m.pi/180):
                newMeshVert.extend([meshVert[fVert[i][0]],meshVert[fVert[i][1]],meshVert[fVert[i][2]],meshVert[fVert[i][3]]])
                rs.AddMesh(newMeshVert,[[0,1,2,3]])
                newMeshVert = []
        else:
            newMeshVert.extend([meshVert[fVert[i][0]],meshVert[fVert[i][1]],meshVert[fVert[i][2]],meshVert[fVert[i][3]]])
            rs.AddMesh(newMeshVert,[[0,1,2,3]])
            newMeshVert = []

Main()