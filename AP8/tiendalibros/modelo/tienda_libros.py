from modelo.carro_compra import CarroCompra

class TiendaLibros:
     # Defina metodo inicializador __init__
    def __init__(self, catalogo, carrito, isbn):
        self.catalogo = {isbn:object}
        self.carrito = CarroCompra()

    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, libro, cantidad):
        if self.isbn not in self.catalogo:
            raise LibroAgotadoError
        
        elif libro.isbn not in self.catalogo.existencias < cantidad:
                raise ExistenciasInsuficientesError 
        else:
            self.carrito.agregar_item(libro,cantidad)

    # Defina metodo retirar_item_de_carrito
    def retirar_item_del_carrito(self, isbn):
        return self.carrito.quitar_item(isbn)

class LibroError(Exception):
        pass

class LibroExistenteError(LibroError):
    def __init__(self):
        super.__init__()
   
    def __str__(self):
        return print("El libro con titulo <TITULO_DEL_LIBRO> y isbn: <ISBN_DEL_LIBRO> ya existe en el catálogo")

    # Defina metodo adicionar_libro_a_catalogo
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

class LibroAgotadoError(LibroError):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return print("El libro con titulo <TITULO_DEL_LIRBO> y isbn <ISBN_DEL_LIBRO> esta agotado")
    
class ExistenciasInsuficientesError(LibroError):
    def __init__(self, cantidad_a_comprar: 0):
        super().__init__()
        self.cantidad_a_comprar: cantidad_a_comprar = int 
             
