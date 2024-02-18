lista = [2,3,3,5,7,10]

def calcular_media():
    sumar_lista = sum(lista)
    dividir_lista = sumar_lista / len(lista)
    return dividir_lista
print(calcular_media())