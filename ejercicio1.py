""" Crear una función donde se implemente el siguiente algoritmo que permite calcular si un
año es bisiesto:
1. Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso
5.
"""

def es_bisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano1 = int(input("Ingresa el año: "))

if es_bisiesto(ano1):
    print(f"{ano1} es un año bisiesto.")
else:
    print(f"{ano1} no es un año bisiesto.")

    ano1