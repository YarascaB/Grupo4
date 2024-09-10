import unittest

class Geometria:
    def area(self, ancho, alto=None):
        if alto is None:  # Caso cuadrado
            return ancho * ancho
        return ancho * alto  # Caso rectángulo


class TestGeometria(unittest.TestCase):
    def setUp(self):
        self.geo = Geometria()

    def test_area_cuadrado(self):
        self.assertEqual(self.geo.area(4), 16)  # Lado = 4

    def test_area_rectangulo(self):
        self.assertEqual(self.geo.area(4, 5), 20)  # Ancho = 4, Alto = 5


if __name__ == '__main__':
    unittest.main()