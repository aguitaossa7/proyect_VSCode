"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
informando de ello.
Fruta Precio
Plátano 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70"""



precios_frutas = {
    "plátano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}

fruta_elegida = input("Ingrese el nombre de la fruta: ").lower()
kilos = float(input("Ingrese la cantidad de kilos: "))

if fruta_elegida in precios_frutas:

    precio_total = precios_frutas[fruta_elegida] * kilos
    print(f"El precio de {kilos} kilos de {fruta_elegida} es: {precio_total}")
else:
    print("Lo siento, esa fruta no está en el diccionario.")