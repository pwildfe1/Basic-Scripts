import rhinoscriptsyntax as rs
import math as m

def filletCrvs(baseCrv,fillet,loc,magF,magB):
    addCrvPts = []
    base = baseCrv
    if loc == 1:
        pt = rs.CurveEndPoint(fillet)
        baseParam = rs.CurveClosestPoint(baseCrv,pt)
        filletParam = rs.CurveClosestPoint(fillet,pt)
        dir = -1
    if loc == 0:
        pt = rs.CurveStartPoint(fillet)
        baseParam = rs.CurveClosestPoint(baseCrv,pt)
        filletParam = rs.CurveClosestPoint(fillet,pt)
        dir = 1
    if loc==1 or loc==0:
        baseParamAdd = convertDirToParam(baseCrv,magB,pt)
        filletParamAdd = convertDirToParam(fillet,dir*abs(magF),pt)
        addCrvPts.append(rs.EvaluateCurve(fillet,filletParamAdd))
        addCrvPts.append(rs.EvaluateCurve(baseCrv,baseParam))
        addCrvPts.append(rs.EvaluateCurve(baseCrv,baseParamAdd))
        addCrv = rs.AddCurve(addCrvPts)
        baseCrvs = rs.SplitCurve(baseCrv,[baseParam,baseParamAdd],False)
        filletCrvs = rs.SplitCurve(fillet,filletParamAdd,False)
        addCrvStart = rs.CurveStartPoint(addCrv)
        addCrvEnd = rs.CurveEndPoint(addCrv)
        if rs.CurveLength(filletCrvs[0])>rs.CurveLength(filletCrvs[1]):
            fillet = filletCrvs[0]
        else:
            fillet = filletCrvs[1]
        for i in range(len(baseCrvs)):
            param = rs.CurveClosestPoint(addCrv,addCrvEnd)
            addTan = rs.CurveTangent(addCrv,param)
            param = rs.CurveClosestPoint(baseCrvs[i],addCrvEnd)
            baseTan = rs.CurveTangent(baseCrv,param)
            val = rs.VectorDotProduct(baseTan,addTan)
            if rs.Distance(rs.CurveStartPoint(baseCrvs[i]),addCrvEnd)==0 and val>0:
                base = baseCrvs[i]
            if rs.Distance(rs.CurveEndPoint(baseCrvs[i]),addCrvEnd)==0 and val<0:
                base = baseCrvs[i]
        waste = [base,fillet,baseCrv,addCrv]
        waste.extend(filletCrvs)
        waste.extend(baseCrvs)
        joined = rs.JoinCurves([base,addCrv,fillet])
        return [joined,waste]
    else:
        return baseCrv

def convertDirToParam(crv,value,pt):
    normParam = value/rs.CurveLength(crv)
    crvParam = rs.CurveClosestPoint(crv,pt)
    normCrvParam = rs.CurveNormalizedParameter(crv,crvParam)
    newNormParam = normCrvParam+normParam
    newNormParam = max(0,max(0,min(1,newNormParam)))
    newParam = rs.CurveParameter(crv,newNormParam)
    return newParam

def Main():
    objs = rs.GetObjects("please select objs to fillet to",rs.filter.polysurface)
    crvs = rs.GetObjects("please select curve to fillet",rs.filter.curve)
    rad = rs.GetReal("enter fillet radius",.2)
    iso = rs.GetInteger("enter 0 for u isocurve or 1 for v isocurve",1)
    srfs = rs.ExplodePolysurfaces(objs)
    srfPairs = []
    isoPairs = []
    fillets = []
    waste = []
    thres = 5
    for i in range(len(crvs)):
        pair = []
        start = rs.CurveStartPoint(crvs[i])
        end = rs.CurveEndPoint(crvs[i])
        ####create surface pair####
        startSrf = rs.PointClosestObject(start,srfs)
        endSrf = rs.PointClosestObject(end,srfs)
        if startSrf!=None and endSrf!=None:
            ####create parameter pair####
            param = rs.SurfaceClosestPoint(startSrf[0],start)
            startIso = rs.ExtractIsoCurve(startSrf[0],param,iso)
            param = rs.SurfaceClosestPoint(endSrf[0],end)
            endIso = rs.ExtractIsoCurve(endSrf[0],param,iso) 
            isoPairs.append(pair)
            if rs.Distance(start,startSrf[1])<thres:
                crvUp = filletCrvs(startIso,crvs[i],0,thres,thres*2)
                crvDown = filletCrvs(startIso,crvs[i],0,thres,-thres*2)
                if crvUp!=None and crvDown!=None:
                    fillets.extend([crvUp[0],crvDown[1]])
                    waste.append(startIso)
                    waste.extend(crvUp[1])
                    waste.extend(crvDown[1])
            if rs.Distance(end,endSrf[1])<thres:
                crvUp = filletCrvs(endIso,crvs[i],1,thres,thres*2)
                crvDown = filletCrvs(endIso,crvs[i],1,thres,-thres*2)
                if crvUp!=None and crvDown!=None:
                    waste.append(endIso)
                    fillets.extend([crvUp[0],crvDown[0]])
                    waste.extend(crvUp[1])
                    waste.extend(crvDown[1])
    rs.DeleteObjects(srfs)
    rs.DeleteObjects(crvs)
    rs.DeleteObjects(waste)
    return fillets

Main()