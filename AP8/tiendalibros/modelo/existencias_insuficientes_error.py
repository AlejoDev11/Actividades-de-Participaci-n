from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo_libro, isbn_libro, cantidad_comprar, existencias):
        self.titulo_libro = titulo_libro
        self.isbn_libro = isbn_libro
        self.cantidad_comprar = cantidad_comprar
        self.existencias = existencias

    def __str__(self):
        return (f"El libro con título {self.titulo_libro} y ISBN {self.isbn_libro} "
                f"no tiene suficientes existencias para realizar la compra: "
                f"cantidad a comprar: {self.cantidad_comprar}, "
                f"existencias: {self.existencias}")

    # Defina metodo inicializador

    # Defina metodo espcial
