from Libreria.Library.Calculadora import *
from Libreria import *

def calcularParticulaPosicion(ket,X):
    return Simulador_Sistema_Cuantico.detectarParticula(ket,X)
def transitarVectorVector(ket,ket2):
    return Simulador_Sistema_Cuantico.detectarParticula(ket,ket2)
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


 
    
