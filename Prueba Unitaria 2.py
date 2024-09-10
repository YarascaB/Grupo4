import unittest

class Geometria:
    def perimetro(self, ancho, alto=None):
        if alto is None:  # Caso cuadrado
            return 4 * ancho
        return 2 * (ancho + alto)  # Caso rectángulo

class TestGeometria(unittest.TestCase):
    def setUp(self):
        self.geo = Geometria()

    def test_perimetro_cuadrado(self):
            self.assertEqual(self.geo.perimetro(4), 16)  # Lado = 4

    def test_perimetro_rectangulo(self):
            self.assertEqual(self.geo.perimetro(4, 5), 18)  # Ancho = 4, Alto = 5

    if __name__ == '__main__':
        unittest.main()