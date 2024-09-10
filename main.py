class Geometria:
    def area(self, ancho, alto=None):
        if alto is None:  # Caso cuadrado
            return ancho * ancho
        return ancho * alto  # Caso rectángulo

    def perimetro(self, ancho, alto=None):
        if alto is None:  # Caso cuadrado
            return 4 * ancho
        return 2 * (ancho + alto)  # Caso rectángulo