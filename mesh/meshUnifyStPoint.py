import rhinoscriptsyntax as rs
import math as m

def Main():
    mesh = rs.GetObject("please select mesh",rs.filter.mesh)
    crv = rs.GetObject("please select reference crv",rs.filter.curve)
    ref = rs.VectorCreate(rs.CurveEndPoint(crv),rs.CurveStartPoint(crv))
    ref = rs.VectorUnitize(ref)
    faces = rs.MeshFaceVertices(mesh)
    verts = rs.MeshVertices(mesh)
    n = 0 
    for i in range(len(faces)):
        fStartVec = rs.VectorCreate(verts[faces[i][0]],verts[faces[i][1]])
        fStartVec = rs.VectorUnitize(fStartVec)
        dot = rs.VectorDotProduct(fStartVec,ref)
        vert = []
        if abs(dot) > .1 and dot<0:
            vert.append(verts[faces[i][2]])
            vert.append(verts[faces[i][3]])
            vert.append(verts[faces[i][0]])
            vert.append(verts[faces[i][1]])
            n=n+1
        else:
            vert.append(verts[faces[i][0]])
            vert.append(verts[faces[i][1]])
            vert.append(verts[faces[i][2]])
            vert.append(verts[faces[i][3]])
        rs.AddMesh(vert,[[0,1,2,3]])
    print(n)

Main()