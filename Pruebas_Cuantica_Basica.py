import unittest
import Cuantica_Basica

class Prueba_Simulador(unittest.TestCase):
    def test_calcularParticulaPosicion(self):
        self.assertEqual(Cuantica_Basica.calcularParticulaPosicion( [(-3.0, -1.0), (0.0, -2.0), (0.0, 1.0), (2.0, 0.0)] , 2 ), 0.05263157894736841)
    def test_transitarVectorVector(self):
        self.assertEqual(Cuantica_Basica.transitarVectorVector([(1.0, 0.0), (0.0, -1.0)],[(0.0, 1.0), (1.0, 0.0)]),(0.0, -0.9999999999999998))
    def test_valorEsperado(self):
        self.assertEqual(Cuantica_Basica.valorEsperado([[(1.0, 0.0), (0.0, -1.0)], [(0.0, 1.0), (2.0, 0.0)]] , [(1.0, 0.0), (0.0, 1.0)] ), (5.0, 0.0))
    def test_varianzaObservable(self):
        self.assertEqual(Cuantica_Basica.varianzaObservable([[(1.0, 0.0), (0.0, -1.0)], [(0.0, 1.0), (2.0, 0.0)]],[(1.0, 0.0), (0.0, 1.0)]),(13.0, 0.0))
    def test_probabilidadObservable(self):
        self.assertEqual(Cuantica_Basica.probabilidadObservable([[(-1.0, 0.0), (0.0, -1.0)], [(0.0, 1.0), (1.0, 0.0)]],[(0.5, 0.0), (0.5, 0.0)]), [(0.6532814824381882, -0.27059805007309845), (0.6532814824381882, -0.27059805007309845)])
    def test_dinamica(self):
        self.assertEqual(Cuantica_Basica.dinamica( [[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)],
                                                    [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)],
                                                    [(0.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0)],
                                                    [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0)],
                                                    [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)],
                                                    [(1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0.0, 0.0)]]
                                                   ,[(1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)] ,
                                                      3),
                                                 [[(0.0, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)], [(1.0, 0.0)], [(0.0, 0.0)]])
if __name__ == "__main__":
    unittest.main()
