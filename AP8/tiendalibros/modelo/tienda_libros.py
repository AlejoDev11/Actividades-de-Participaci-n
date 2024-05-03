from modelo.libro import Libro
from modelo.carro_compra import CarroCompra
from modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from modelo.libro_agotado_error  import LibroAgotadoError
from modelo.libro_existente_error import LibroExistenteError
from modelo.existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
     # Defina metodo inicializador __init__
    def __init__(self, catalogo, carrito, isbn):
        self.catalogo = dict[str, Libro] = {}
        self.carrito: CarroCompra = CarroCompra()

    #Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn: str, titulo:str, precio: float, existencias: int): 
        try:
            for i in self.catalogo:
                if i == isbn: raise LibroExistenteError
            else:
                objeto_libro = (isbn, titulo, precio, existencias)
                if i not in self.catalogo:
                    return self.catalogo.append(objeto_libro)
        
        except:
            pass

    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro)
        
        if cantidad > libro.existencias: 
                raise ExistenciasInsuficientesError 
        else:
            self.carrito.agregar_item(libro,cantidad)

    # Defina metodo retirar_item_de_carrito
    def retirar_item_del_carrito(self, isbn: str):
        return self.carrito.quitar_item(isbn)

