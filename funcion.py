"""
Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde
en el abecedario y mostrar el nuevo string en pantalla. Por ejemplo:
Hola → H(8) o(15) l(12) a(1)"""

import string

def numerador_caracteres(frase):
    abecedario = string.ascii_lowercase
    resultado = ""
    for letra in frase:
        if letra.lower() in abecedario:
            posicion = abecedario.index(letra.lower()) + 1
            resultado += f"{letra}({posicion}) "
        else:
            resultado += letra
    return resultado.strip()

# Ejemplo de uso
frase = input("Ingresa una frase: ")
print(numerador_caracteres(frase))

"""import string
def numerador_caracteres():
    abecedario = string.ascii_letters[:26]
    dict_letra_a_entero = dict()
    for letra in range(len(abecedario)):
        dict_letra_a_entero[abecedario[letra]] = n"""