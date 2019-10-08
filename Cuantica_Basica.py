from Libreria.Library.Calculadora import *

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
    delta=


obs=[]
for i in range(2):
    vf=[tuple(map(float, x.split(","))) for x in (input().split(" "))]
    obs.append(vf)
ket=[tuple(map(float, x.split(","))) for x in (input().split(" "))]
print(valorEsperado(obs,ket))
    
    
