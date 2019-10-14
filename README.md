# CUANTICA BASICA
Teoria Cuantica Basica

Se reunen todos los retos de programacion.
El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. 
El programa permite especificar el número de posiciones y un vector ket de estado asignando las amplitudes.
Se puede describir un observable para una matriz hermitiana.
El programa puede determinar tanto valores propios como vectores propios.
Se considera la dinamica del sistema.

- El sistema calcula la probabilidad de encontrarlo en una posición en particular.
- El sistema si se le da otro vector Ket busca la probabilidad de transitar del primer vector al segundo.
- El sistema calcula la media y la varianza del observable en el estado dado.

# Generalidades

El estado actual de la partícula ndimensional puede representarse en un vector de columna compleja [c0, c1,. . . , cn − 1] T.
Sera nombrado como *ket* y cada estado de nuestro sistema sera representado por un elemento de Cn como
![aca](https://user-images.githubusercontent.com/45296448/65923022-ee18e600-e3ac-11e9-8aa2-48ae0af4e418.PNG)
Asi como un observable, una matriz de Cn elementos representado por la letra Ω

## Como usar

Esta libreria esta programada en la version de Python 3.7.4 y funciona para las versiones 3.7.* 
Debe tener instalado un entorno de desarrollo o un editor de texto donde se pueda compilar el archivo.

Si no posee uno puede ingresar a https://www.python.org/ para descargar la ultima version.

Se necesita instalar la libreria numpy en Python para que funcione el programa.
Puede instalarala de la siguiente manera:
1. Abra la consola de comandos
2. Ponga esto

        $ py -m pip install numpy
        
3. Cierre la consola.
Despues de tenerlo, puede crear un archivo .py en el mismo directorio del archivo Cuantica_Basica.py

Importe la libreria en el nuevo archivo y use las operaciones de manera directa
Por ejemplo el siguiente codigo le indicara cual es la probabilidad de encontrar una particula dandole el ket y la posicion:
El sistema esta dado por:
![aca](https://user-images.githubusercontent.com/45296448/66001638-7e1b6600-e467-11e9-84e2-dc4b59716a6f.PNG)

`import Cuantica_Basica`

`a=Cuantica_Basica.calcularParticulaPosicion([(-3.0, -1.0), (0.0, -2.0), (0.0, 1.0), (2.0, 0.0)],2)`

`print(a)`

Producira un resultado:

`0.05263157894736841`

En caso de que tenga problemas puede ejecutar el archivo Pruebas_Simulador_Sistema_Cuantico.py para ejecutar las pruebas establecidas.
En el repositorio existe un archivo Entradas_Manuales en las que puede ver codigo que le puede ayudar a hacer lectura de datos para el programa por teclado; tambien esta el archivo Casos_Prueba si desea usar el archivo de Entradas_Manuales para probar casos de prueba.

### Como usarlo por consola?

Si desea usarlo por consola, ubique la consola en la carpeta donde esta el archivo Simulador_Sistema_Cuantico.py y escriba en la consola

        $ py Cuantica_Basica.py

Para ejecutar las pruebas escriba en la consola

        $ py Pruebas_Cuantica_Basica.py
        
Puede ejecutar el idle de python si escribe

        $ py

Estando en el directorio puede ejecutar 

        import Cuantica_Basica
        Cuantica_Basica.calcularParticulaPosicion([(-3.0, -1.0), (0.0, -2.0), (0.0, 1.0), (2.0, 0.0)],2)
 
Y el resultado sera:

        0.05263157894736841

## FUNCIONALIDADES:

- Detectar cual es la probabilidad de encontrar una particula en una posicion
- Transitar desde un vector a otro
- Determinar el valor esperado entre un observador y un ket despues de observarlo varias veces
- Determinar la varianza de un observable, dandole el observable y el ket que tinen que observar
- Calcular con ayuda de la libreria numpy los valores propios del observable
- Calcular con ayuda de la libreria numpy los vectores propios del observable
- Determinar las probabilidades de que el sistema transite a algunos de sus vectores propios
- Apartir de una matriz unitaria, calcula el estado final apartir del estado inicial.


## BIBLIOGRAFIA:


        > Quantum Computing For Computer Scientists 
        Noson S. Yanofsky 
        Mirco A. Mannucci
    
Para mas proyectos, Sigueme y encuentra mis repositorios de computacion cuantica
# Buscar mas ...
CALCULADORA DE NUMEROS COMPLEJOS 
https://github.com/Wasawsky/CNYT_COMPLEJOS.git


*Por: Michael Ballesteros*
