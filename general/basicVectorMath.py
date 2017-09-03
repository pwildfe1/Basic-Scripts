import math as m
import rhinoscriptsyntax as rs

def vecRotate(vec,ang,axis):
    cos = m.cos(m.pi/180*ang)
    sin = m.sin(m.pi/180*ang)
    v = vec
    u = vecUnitize(axis)
    R1,R2,R3 = [] , [] , []
    c = 1-cos

    R1.append(cos+m.pow(u[0],2)*c)
    R1.append(u[0]*u[1]*c-u[2]*sin)
    R1.append(u[0]*u[2]*c+u[1]*sin)
    
    R2.append(u[1]*u[0]*c+u[2]*sin)
    R2.append(cos+m.pow(u[1],2)*c)
    R2.append(u[1]*u[2]*c-u[0]*sin)
    
    R3.append(u[2]*u[0]*c-u[1]*sin)
    R3.append(u[2]*u[1]*c+u[0]*sin)
    R3.append(cos+m.pow(u[2],2)*c)
    
    x = vecDot(v,R1)
    y = vecDot(v,R2)
    z = vecDot(v,R3)
    
    return [x,y,z]

def vecMag(vec):
    sum = 0    
    for i in range(len(vec)):
        sum = sum+m.pow(vec[i],2)
    sum = m.pow(sum,.5)
    return sum


def transpose(matrix):
    transpose = []    
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transpose.append(matrix[j][i])
    return transpose


def vecUnitize(vec):
    mag = vecMag(vec)
    for i in range(len(vec)):
        vec[i] = vec[i]/mag
    return vec


def vecDot(v1,v2):
    sum = 0    
    for i in range(len(v1)):
        sum = v1[i]*v2[i] + sum
    return sum


def vecAng(v1,v2):
    v1 = vecUnitize(v1)
    v2 = vecUnitize(v2)
    val = vecDot(v1,v2)
    ang = m.acos(val)
    return ang


def vecDiff(v1,v2):
    nV = []
    for i in range(len(v1)):
        nV.append(v1[i]-v2[i])
    return nV


def vecAdd(v1,v2):
    nV = []
    for i in range(len(v1)):
        nV.append(v1[i]+v2[i])
    return nV




def Main():
    crv = rs.GetObject("please select crv",rs.filter.curve)
    #axis = rs.GetObject("please select axis",rs.filter.curve)
    ang = 34
    vec = rs.VectorCreate(rs.CurveEndPoint(crv),rs.CurveStartPoint(crv))
    axis = rs.VectorCreate([1,.25,.5],[0,0,0])
    newVec = rs.VectorRotate(vec,ang,axis)
    print(newVec)
    vec = rs.VectorCreate(rs.CurveEndPoint(crv),rs.CurveStartPoint(crv))
    newVec = vecRotate(vec,ang,axis)
    print(newVec)

Main()