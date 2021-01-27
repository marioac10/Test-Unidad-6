"Este programa contiene funciones de rotacion 3D en los x, y, z junto a sus respectivas matrices de rotacion definidas" 
"en las clases anteriores"

import matplotlib.pyplot as plt 
import numpy as np
from math import cos,sin,radians #o usar lo que ya trae numpy

#________Definir las funciones
def rotRx(xc,yc,zc,xp,yp,zp,Rx):
    a=[xp,yp,zp]
    b=[1,0,0]#---------Rx11,Rx12,Rx13
    xpp=np.inner(a,b)#Producto escalar de a,b=xp*Rx11+yp*Rx12+zp*Rx13
    b=[0,cos(Rx),-sin(Rx)]#---------Rx21,Rx22,Rx23
    ypp=np.inner(a,b)#Producto escalar de a,b=xp*Rx21+yp*Rx22+zp*Rx23
    b=[0,sin(Rx),cos(Rx)]#---------Rx31,Rx32,Rx33
    zpp=np.inner(a,b)#Producto escalar de a,b=xp*Rx31+yp*Rx32+zp*Rx33
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    
    return [xg,yg,zg]
    
def rotRy(xc,yc,zc,xp,yp,zp,Ry):
    a=[xp,yp,zp]
    b=[cos(Ry),0,sin(Ry)]#---------Ry11,Ry12,Ry13
    xpp=np.inner(a,b)#Producto escalar de a,b=xp*Ry11+yp*Ry12+zp*Ry13
    b=[0,1,0]#---------Ry21,Ry22,Ry23
    ypp=np.inner(a,b)#Producto escalar de a,b=xp*Ry21+yp*Ry22+zp*Ry23
    b=[-sin(Ry),0,cos(Ry)]#---------Ry31,Ry32,Ry33
    zpp=np.inner(a,b)#Producto escalar de a,b=xp*Ry31+yp*Ry32+zp*Ry33
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    
    return [xg,yg,zg]

def rotRz(xc,yc,zc,xp,yp,zp,Rz):
    a=[xp,yp,zp]
    b=[cos(Rz),-sin(Rz),0]#---------Rz11,Rz12,Rz13
    xpp=np.inner(a,b)#Producto escalar de a,b=xp*Rz11+yp*Rz12+zp*Rz13
    b=[sin(Rz),cos(Rz),0]#---------Rz21,Rz22,Rz23
    ypp=np.inner(a,b)#Producto escalar de a,b=xp*Rz21+yp*Rz22+zp*Rz23
    b=[0,0,1]#---------Rz31,Rz32,Rz33
    zpp=np.inner(a,b)#Producto escalar de a,b=xp*Rz31+yp*Rz32+zp*Rz33
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]

    return [xg,yg,zg]

def fillStartCircleValues(x,y,z,xg,yg,zg,r,phi1,phi2,dphi):

    for phi in np.arange (phi1,phi2+dphi,dphi):#Establecer las coordenadas de los puntos del circulo
        xp=r*cos(phi)
        yp=r*sin(phi)
        zp=0

        x.append(xp)
        y.append(yp)
        z.append(zp)

        xg.append(xp)
        yg.append(yp)
        zg.append(zp)
    return [x,y,z,xg,yg,zg]

def fillStarValues(a,b,c,ag,bg,cg,r1,r2):
    p1=radians(0)
    p2=radians(365)
    dp=radians(1)
    #Vertices del pentagono exterior
    v1=radians(54)
    v2=radians(126)
    v3=radians(198)
    v4=radians(270)
    v5=radians(342)
    #Vertices del pentagono interior
    v6=radians(18)
    v7=radians(90)
    v8=radians(162)
    v9=radians(234)
    v10=radians(306)
    for p in np.arange(p1,p2,dp):
        if p==v1 or p==v2 or p==v3 or p==v4 or p==v5: 
            xp=r1*np.cos(p)
            yp=r1*np.sin(p)
            zp=0
            a.append(xp)
            b.append(yp)
            c.append(zp) 
        elif p==v6 or p==v7 or p==v8 or p==v9 or p==v10:
            xxp=r2*np.cos(p)
            yyp=r2*np.sin(p)
            zzp=0
            ag.append(xxp)
            bg.append(yyp)
            cg.append(zzp)
       
    a.append(a[0])
    b.append(b[0])
    c.append(c[0])
    ag.append(ag[0])
    bg.append(bg[0])
    cg.append(cg[0])
    #plt.plot(a,b,linewidth=5,color='b')
    #plt.plot(ag,bg,linewidth=5,color='b')

    return [a,b,c,ag,bg,cg]

#plt.scatter(xp,yp,s=10,color='b')
#plt.scatter(xxp,yyp,s=10,color='r')
#xlast=xp
#ylast=yp   
#plt.plot([xlast,xp],[ylast,yp],c='y')

#Vertices del pentagono exterior
    #v1=radians(18)
    #v2=radians(90)
    #v3=radians(162)
    #v4=radians(234)
    #v5=radians(306)
    #Vertices del pentagono interior
    #v6=radians(54)
    #v7=radians(126)
    #v8=radians(198)
    #v9=radians(270)
    #v10=radians(342)