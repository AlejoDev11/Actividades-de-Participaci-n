from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    def __init__(self):
        super.__init__()
    # Defina metodo inicializador

    # Defina metodo especial
    def __str__(self):
        return print("El libro con titulo <TITULO_DEL_LIBRO> y isbn: <ISBN_DEL_LIBRO> ya existe en el catálogo")
