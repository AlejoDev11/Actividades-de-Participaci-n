import math

class Punto: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio 

    def calcular_area(self):
        PI = 3.14
        return PI * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * PI * self.radio 
    
    def punto_pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return distancia_centro_punto <= self.radio
    
PI = 3.14

centro_circulo = Punto(0,0)

mi_circulo =  Circulo(centro_circulo,5)

print("Area:",mi_circulo.calcular_area())
print("Perimetro:", mi_circulo.calcular_perimetro())

punto_test = Punto(7,-8)

if mi_circulo.punto_pertenece(punto_test):
    print("El punto pertenece al circluo")
else:
    print("El punto no pertenece al circulo")