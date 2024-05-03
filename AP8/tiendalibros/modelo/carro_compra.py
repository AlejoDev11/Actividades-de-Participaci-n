from modelo.item_compra import ItemCompra
class CarroCompra:
    def __init__(self, item):
        self.item: list[ItemCompra] = [] #Lista vacía de ItemCompra
    # Defina metodo inicializador __init__(self)

    # Defina el metodo agregar_item
    def agregar_item(self, libro, cantidad): 
        item_compra = ItemCompra(libro, cantidad) #Objeto item_compra
        self.item.append(item_compra)
        return self.item 

    # Defina el metodo calcular_total
    def calcular_total(self):
        total = 0
        for item_compra in self.item:
            total += item_compra.calcular_subtotal
        return total 
    
    # Defina el metodo quitar_item
    def quitar_item(self, isbn, libro):
        self.item = [item for item in self.item if not (item.libro.isbn == isbn)]