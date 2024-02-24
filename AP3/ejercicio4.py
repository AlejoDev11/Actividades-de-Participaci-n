class Punto: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo: 
    def __init__(self, punto_esquina1, punto_esquina2):
        self.esquina1 = punto_esquina1
        self.esquina2 = punto_esquina2

    def calcular_lados(self):
        lado_horizontal = abs(self.esquina1.x - self.esquina2.x)
        lado_vertical = abs(self.esquina1.y - self.esquina2.y)
        return lado_horizontal, lado_vertical

    def calcular_perimetro(self):
        lado_horizontal, lado_vertical = self.calcular_lados()
        return 2 * (lado_horizontal + lado_vertical)

    def calcular_area(self):
        lado_horizontal, lado_vertical = self.calcular_lados()
        return  lado_horizontal * lado_vertical

    def es_cuadrado(self):
        lado_horizontal, lado_vertical = self.calcular_lados()
        return lado_horizontal == lado_vertical

esquina1 = Punto(1,1) 
esquina2 = Punto(4,4)

mi_rectangulo = Rectangulo(esquina1, esquina2)

print("Perímetro:", mi_rectangulo.calcular_perimetro())
print("Area:", mi_rectangulo.calcular_area())

if mi_rectangulo.es_cuadrado:
    print("El rectangulo es un cuadrado")
else:
    print("El rectangulo no es un cuadrado")
