from modelo.tienda_libros import Libro 

class ItemCompra:
    def __init__(self, libro:str, cantidad:int):
        self.libro: Libro = libro 
        self.cantidad: int = cantidad

    def calcular_subtotal(self, cantidad, precio):
        subtotal = cantidad * precio
        return subtotal 
    
    