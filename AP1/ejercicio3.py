import random

def numeros_aleatorios():
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 50)) 
    return lista

print(numeros_aleatorios())
