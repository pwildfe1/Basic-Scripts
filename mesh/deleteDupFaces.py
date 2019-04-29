import rhinoscriptsyntax as rs
import math as m


def deleteDupFacesAll(mesh):
    faces = rs.MeshFaces(mesh)
    selected = []
    newFaces = []
    for i in range(len(faces)):
        dup = False
        for j in range(len(faces)):
            count=0
            for k in range(len(faces[i])):
                if faces[i][k] in faces[j]:
                    count=count+1
            if count==len(faces[i]):
                dup = True
        if dup==False:
            newFaces.append(rs.AddMesh(faces[i],[0,1,2,3]))
    new = rs.JoinMeshes(newFaces,True)
    return new


def Main():
    mesh = rs.GetObjects("please select mesh",rs.filter.mesh)
    revised = deleteDupFacesAll(mesh)
    return revised

Main()