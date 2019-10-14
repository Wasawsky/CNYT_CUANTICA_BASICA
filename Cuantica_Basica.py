#Cuantica Basica
#Michael Ballesteros
#2019-2

from Calculador import *
import numpy as np

def calcularParticulaPosicion(ket,X):
    calA=CalculadoraAvanzada()
    return calA.detectarParticula(ket,X)
def transitarVectorVector(ket,ket2):
    calA=CalculadoraAvanzada()
    return calA.transitarVector(ket,ket2)
def valorEsperado(obs,ket):
    """ Recibo  observable
                ket
        y calculo el valor esperado de observar repetidamente el ket
    """
    cal=Calculadora()
    obsSobreket=cal.accion(obs,ket)
    bra=cal.matrizConjugada(obsSobreket)
    ket1=cal.transpuesta([ket])
    bra1=cal.transpuesta(bra)
    car=cal.multiplicacionMatrizMatriz(bra1,ket1)[0][0]
    return car
def varianzaObservable(obs,ket):
    """ Recibo  observable
                ket
        y calculo la varianza del estado
    """
    cal=Calculadora()
    nve=cal.multiplicacion(valorEsperado(obs,ket),(-1,0))
    mve=cal.multiplicacionEscalarMatriz(cal.matrizIdentidad(len(obs)),nve)
    delta=cal.sumaMatrices(obs,mve)
    deltaCuadrado=cal.multiplicacionMatrizMatriz(delta,delta)
    var=valorEsperado(deltaCuadrado,ket)
    return var
def propiosObservable(obs):
    """ Recibo observable y calculo valores propios y vectores propios -> vector complejo,vectores complejos
    """
    for i in range(len(obs)):
        for j in range(len(obs[0])):
            obs[i][j]=complex(obs[i][j][0],obs[i][j][1])
    a=np.array(obs)
    x,v = np.linalg.eig(a)
    valPropios = [(c.real,c.imag) for c in x]
    vectPropios = [[(c.real,c.imag) for c in y]for y in v]
    return valPropios,vectPropios
def probabilidadObservable(obs,ket):
    """ Calculo la probabilidad de que un ket pase a los vectores propios del observable -> vector complejos
    """
    valP,vectP = propiosObservable(obs)
    probs=[]
    calA=CalculadoraAvanzada()
    for v in vectP:
        p=calA.transitarVector(v,ket)
        probs.append(p)
    return probs
def dinamica(un,init,steps):
    """ Recibo Matriz compleja
               vector estado inicial
               Pasos hasta donde llega el sistema
    """    
    temp=init
    up=[un]
    ur=un
    for p in range(steps):
        cal=Calculadora()
        ur=cal.multiplicacionMatrizMatriz(ur,ur)
        up.append(ur)
    un1=[]
    for k in range(len(up)):
        un1=cal.multiplicacionMatrizMatriz(up[k],up[k-1])
    temp=cal.accion(un1,init)
    return temp
