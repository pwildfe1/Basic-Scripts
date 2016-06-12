import rhinoscriptsyntax as rs
import math as m

def Main():
    srf = rs.GetObject("enter surface",rs.filter.surface)
    domainU = rs.SurfaceDomain(srf,0)
    domainV = rs.SurfaceDomain(srf,1)
    spacingX = rs.GetReal("enter spacing in u dir",50)
    spacingY = rs.GetReal("enter spacing 
    for i in range(int((domainU[1]-domainU[0])/spacingX)