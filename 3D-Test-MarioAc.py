#Mario Edmundo Ac Hernandez
#Num.Control: 18390055
#Fecha: 27/01/2021
#Programa que plotea un triangulo(plano) y un punto(hit point) para ver si esta dentro o fuera de él.

#Profe no pude hacer como hacer que el usuario ingrese los valores y sustituirlos en el array
#por lo que lo hice de manera directa en los arrays.

#Logre trazar el triangulo con las lineas al hitpoint y modificar para salga con mi no.control
import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import Tools3D as tools

#____Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=80
yc=40
zc=40

#Plano y linea de sistema
x=[40,30,80,40,75]
y=[60,10,60,60,40]
z=[0,0,0,0,0]

for i in range(len(x)):
    xg.append(x[i]+xc)
    yg.append(y[i]+yc)
    zg.append(z[i]+zc)

#__Plotear el sistema 
#def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
    plt.axis([0,180,100,0])
    plt.axis('on')
    plt.grid(False)
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')#plano
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')#Ploteamos el plano en este caso es el triangulo
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')
    #plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='k')
    plt.plot([xg[3],xg[4]],[yg[3],yg[4]],color='b')#Line:Ploteamos la primer linea para trazar el primer triangulo
    plt.plot([xg[1],xg[4]],[yg[1],yg[4]],color='b')#Line:Ploteamos la segunda linea para trazar el  triangulo
    plt.plot([xg[2],xg[4]],[yg[2],yg[4]],color='b')#Line:Ploteamos las lineas para trazar el primer triangulo

    if hitcolor=='g':# Do not touch hit point
        plt.scatter(xg[4],yg[4],s=20,color=hitcolor)
    else:
        plt.scatter(xhg,yhg,s=20,color=hitcolor)

    plt.show()

def hitpoint(x,y,z):
    #___distance point 3 to 4
    a=x[4]-x[3]
    b=y[4]-y[3]
    c=z[4]-z[3]
    Q45=sqrt(a*a+b*b+c*c) 
    # unit vector components point 3 to 4
    lx=a/Q45 
    ly=b/Q45
    lz=c/Q45
    #___distance point 0 to 2
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q03=sqrt(a*a+b*b+c*c) 
    # unit vector components point 0 to 2
    ux=a/Q03 #———unit vector 0 to 3
    uy=b/Q03
    uz=c/Q03
    #___distance point 0 to 1
    a=x[0]-x[0]
    b=y[0]-y[0]
    c=z[0]-z[0]
    Q01=sqrt(a*a+b*b+c*c)
    # unit vector components point 0 to 1
    vx=a/Q01 #———unit vector 0 to 1
    vy=b/Q01
    vz=c/Q01
    #___normal vector unit
    nx=uy*vz-uz*vy 
    ny=uz*vx-ux*vz
    nz=ux*vy-uy*vx
    #_____vector components 0 t0 3
    vx1b=x[3]-x[0]
    vy1b=y[3]-y[0]
    vz1b=z[3]-z[0]
    #__perpenticular distance 3 to plane triangular
    Qn=(vx1b*nx+vy1b*ny+vz1b*nz)

    #___cos of angle p
    cosp=lx*nx+ly*ny+lz*nz

    #___distance 3 to hit point
    Qh=abs(Qn/cosp)

    #__Hit point coordinates
    xh=x[3]+Qh*lx
    yh=y[3]+Qh*ly
    zh=z[3]+Qh*lz

    #___global hit point coodinates
    xhg=xh+xc
    yhg=yh+yc
    zhg=zh+zc
    #____checar si la linea de 4 A 5 queda fuera de los valores del rectangulo
    #__Component of vector V0h
    a=xh-x[0]
    b=yh-y[0]
    c=zh-z[0]
    #dot products
    up=a*ux+b*uy+c*uz
    vp=a*vx+b*vy+c*vz


    #Calculamos la longitud de la linea del triangulo para calcular el area



    #Si no estamos saliendo del plano del objeto rectangulo 
    hitcolor='r'
    if up<0:
        hitcolor='b'
    if up>Q03:
        hitcolor='b'
    if vp<0:
        hitcolor='b'
    if vp>Q01:
        hitcolor='b'
    
    #___Si el punto de 3 a 4 no alcanza el hit point
    a=x[4]-x[3]
    b=y[4]-y[3]
    c=z[4]-z[3]
    Q45=sqrt(a*a+b*b+c*c)
    if Q45 < Qh:
        hitcolor='g'
    return xh,yh,xhg,yhg,hitcolor 


def plotPlaneLinex(xc,yc,zc,Rx):
    for i in range(len(y)):
        [xg[i],yg[i],zg[i]]=tools.rotRx(xc,yc,zc,x[i],y[i],z[i],Rx)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)

def plotPlaneLiney(xc,yc,zc,Ry):
    for i in range(len(y)):
        [xg[i],yg[i],zg[i]]=tools.rotRy(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)

def plotPlaneLinez(xc,yc,zc,Rz):
    for i in range(len(y)):
        [xg[i],yg[i],zg[i]]=tools.rotRz(xc,yc,zc,x[i],y[i],z[i],Rz)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)
    

####___pedir al usaurio que eje desea trabajar y plotear el PlaneLine
while True:
    axis=input("Teclea el eje que deseas visualizar 'x,y,z' o escribe tu No.Control para salir ?:")
    if axis=='x':#plotear el eje X
        Rx=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinex(xc,yc,zc,Rx)#LLamamos a la funcion de ploteo
    if axis=='y':
        Ry=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLiney(xc,yc,zc,Ry)#LLamamos a la funcion de ploteo
    if axis=='z':
        Rz=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinez(xc,yc,zc,Rz)#LLamamos a la funcion de ploteo
    if axis== '18390055': #Validar que ingrese el numero de control
        break