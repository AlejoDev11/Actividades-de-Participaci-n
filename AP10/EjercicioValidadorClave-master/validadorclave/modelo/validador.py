# TODO: Implementa el código del ejercicio aquí

from abc import ABC, abstractmethod
from validadorclave.modelo.errores import *

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada = longitud_esperada

    @abstractmethod 
    def es_valida():
        pass 

    def _validar_longitud(self, clave: str) -> bool:
        self.clave: str = clave 
        return len(clave) >= self.longitud_esperada
    
    def _contiene_mayuscula(self) -> bool:
        return any(char.isupper() for char in self.clave)

    def _contiene_minuscula(self) -> bool:
        return any(char.islower () for char in self.clave)

    def _contiene_numero(self) -> bool:
        return any(char.isdigit () for char in self.clave)
        
class ReglaValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self):
        return any(char in "@ _ # $ %" for char in self.clave)
    
    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave no cumple con la longitud mínima.")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave no contiene una letra mayúscula.")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave no contiene una letra minúscula.")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave no contiene un número.")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave no contiene un carácter especial.")
        return True
    
class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)
    
    def contiene_calisto(self, clave:str) -> bool:
        objetivo = "calisto"
        indice = clave.lower().find(objetivo)

        if indice ==-1:
            return False

        subcadena = clave[indice:indice + len(objetivo)]
        mayusculas = sum(c.isupper() for c in subcadena)

        return 2 <= mayusculas < len(objetivo)
    
    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave no cumple con la longitud mínima.")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave no contiene un número.")
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("La clave no contiene la palabra secreta 'calisto' con al menos dos letras mayúsculas.")
        return True
        
class Validador:
    def __init__(self, regla: ReglaValidacion) -> None:
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool: 
        return self.regla.es_valida(clave)

    