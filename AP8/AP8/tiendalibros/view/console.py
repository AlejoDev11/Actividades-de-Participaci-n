import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    # Defina el metodo retirar_libro_de_carrito_de_compras
    def retirar_libro_de_carrito_de_compras(self):
        print(input(str("Ingrese el ISBN del libro que desea retirar del carrito: ")))
        return self.tienda_libros.retirar_item_del_carrito
    print("El libro ha sido retirado correctamente.")

    # Defina el metodo agregar_libro_a_carrito_de_compras
    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = print(input(str("Ingrese el ISBN del libro que desea agregar: ")))
            cantidad = print(input(int("Ingrese la cantidad de unidades del libro: ")))
            if isbn not in self.tienda_libros.catalogo:
                return self.tienda_libros.agregar_libro_a_carrito

        except ValueError as e:
            print("Error:", e)
            print("Por favor ingrese un ISBN valido y una cantidad entera positiva")

        except self.tienda_libros.ExistenciasInsuficientesError as e:
            print("Error:", e)
            print("No hay suficientes existencias del libro en la tienda")

        except self.tienda_libros.LibroAgotadoError as e:
            print("Error:", e)
            print("El libro se encuentra agotado")
            
    # Defina el metodo adicionar_un_libro_a_catalogo
    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = print(input(str("Ingrese el ISBN del libro")))
            titulo = print(input(str("Ingrese el titulo del ibro")))
            precio = print(input(float("Ingrese el precio del libro")))
            existencias = print(input(int("Ingrese las existencias del libro")))

            return self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
        
        except ValueError as e:
            print("Error:", e)
            print("Por favor, ingrese un precio válido y un número entero para las existencias.")

        except ValueError as e: 
            print("Error:", e)
            print("El ISBN o el titulo no son correctos, intente de nuevo")