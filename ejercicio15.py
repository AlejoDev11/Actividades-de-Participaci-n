cadena_de_texto = str(input("Ingrese una cadena de texto: "))

def palindromo(cadena_de_texto):
    cadena_de_texto = cadena_de_texto.lower()
    return cadena_de_texto == cadena_de_texto[::-1]

print(palindromo(cadena_de_texto))