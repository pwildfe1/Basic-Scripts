import rhinoscriptsyntax as rs
import math as m

def genSrfGrid(srf,resoU,resoV):
    domU = rs.SurfaceDomain(srf,0)
    rangeU = domU[1]-domU[0]
    domV = rs.SurfaceDomain(srf,1)
    rangeV = domV[1]-domV[0]
    grid = []
    norms = []
    tiles = []
    for i in range(resoU):
        for j in range(resoV):
            u = rangeU*i/resoU + domU[0]
            v = rangeV*j/resoV + domV[0]
            grid.append([u,v])
    for i in range(len(grid)-resoV):
        if (i+1)%resoV != 0:
            pt01 = rs.EvaluateSurface(srf,grid[i][0],grid[i][1])
            norm01 = rs.SurfaceNormal(srf,grid[i])
            pt02 = rs.EvaluateSurface(srf,grid[i+1][0],grid[i+1][1])
            norm02 = rs.SurfaceNormal(srf,grid[i+1])
            pt03 = rs.EvaluateSurface(srf,grid[i+1+resoV][0],grid[i+1+resoV][1])
            norm03 = rs.SurfaceNormal(srf,grid[i+1+resoV])
            pt04 = rs.EvaluateSurface(srf,grid[i+resoV][0],grid[i+resoV][1])
            norm04 = rs.SurfaceNormal(srf,grid[i+resoV])
            norms.append([norm01,norm02,norm03,norm04])
            tiles.append([pt01,pt02,pt03,pt04])
    return tiles

def Main():
    srf = rs.GetObject("please select surface",rs.filter.surface)
    tiles = genSrfGrid(srf,20,40)
    for i in range(len(tiles)):
        rs.AddCurve(tiles[i],1)

Main()