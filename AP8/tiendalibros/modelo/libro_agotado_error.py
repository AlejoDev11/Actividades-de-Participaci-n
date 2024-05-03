from tiendalibros.modelo.libro_error import LibroError
from modelo.tienda_libros import Libro


class LibroAgotadoError(LibroError):
    def __init__(self, libro: Libro):
        super().__init__(Libro)

    def __str__(self):
        return "El libro con titulo {} y isbn: {} esta agotado".format(self.libro.titulo and self.libro.isbn)

    # Defina metodo inicializador

    # Defina metodo especial
