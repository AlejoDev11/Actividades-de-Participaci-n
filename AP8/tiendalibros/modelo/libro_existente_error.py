from tiendalibros.modelo.libro_error import LibroError
from modelo.tienda_libros import Libro


class LibroExistenteError(LibroError):
    def __init__(self, libro: Libro):
        super.__init__(Libro)
    # Defina metodo inicializador

    # Defina metodo especial
    def __str__(self):
        return "El libro con titulo {} y isbn: {} ya existe en el catálogo".format(self.libro.titulo and self.libro.isbn)
