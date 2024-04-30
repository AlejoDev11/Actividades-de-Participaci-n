class ItemCompra:
    def __init__(self, libro:str, cantidad:int):
        self.libro = libro
        self.cantidad = 0 

    def calcular_subtotal(self, cantidad, precio):
        subtotal = cantidad * precio
        return subtotal 
    
    