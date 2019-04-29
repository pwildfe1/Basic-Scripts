import rhinoscriptsyntax as rs
import math as m

class vectorLine:
    def __init__(self,st,en):
        self.st = st
        self.en = en
        self.vec = [self.en[0]-self.st[0],self.en[1]-self.st[1],self.en[2]-self.st[2]]
    def paramToPoint(self,t):
        coord = []
        for i in range(len(self.vec)):
            coord.append(self.vec[i]*t + self.st[i])
        return coord
    def closestPt(self,pt):
        pt = rs.PointCoordinates(pt)
        x = pt[0]
        y = pt[1]
        z = pt[2]
        ax = self.vec[0]
        ay = self.vec[1]
        az = self.vec[2]
        bx = self.st[0]
        by = self.st[1]
        bz = self.st[2]
        numerator = ax*x+ay*y+az*z - (ax*bx+ay*by+az*bz)
        param = numerator/(m.pow(ax,2)+m.pow(ay,2)+m.pow(az,2))
        return param

def Main():
    line = rs.GetObject("please select line",rs.filter.curve)
    pt = rs.GetObject("please select point",rs.filter.point)
    st = rs.CurveStartPoint(line)
    en = rs.CurveEndPoint(line)
    myVec = vectorLine(st,en)
    param = myVec.closestPt(pt)
    rs.AddPoint(myVec.paramToPoint(param))
    param = rs.CurveClosestPoint(line,pt)
    rs.AddPoint(rs.EvaluateCurve(line,param))

Main()
