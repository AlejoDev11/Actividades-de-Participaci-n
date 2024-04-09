from dataclasses import dataclass

@dataclass
class Elemento: 
    nombre = str 

    def __eq__(self) -> bool:
        return self.nombre == self.nombre
       
class Conjunto:
    elementos = list[Elemento]
    contador = 0 

    def __init__(self, nombre: str):
        self.elementos = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador #Atributo privado 

    @property #Propiedad de solo lectura 
    def id(self,):
        return self.__id
    
    def contiene(self, elemento) -> bool:
        for i in self.elementos:
            if i.nombre == elemento.nombre:
                return True
            return False
    
    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            if not self.contiene(elemento):
                self.agregar_elemento(elemento)