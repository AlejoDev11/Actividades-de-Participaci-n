from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return print("El libro con titulo <TITULO_DEL_LIRBO> y isbn <ISBN_DEL_LIBRO> esta agotado")

    # Defina metodo inicializador

    # Defina metodo especial
