
"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El
programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el
usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el
coste total.
"""
cesta_de_compra = {}

while True:
    articulo = input("Ingrese el nombre del artículo (o 'terminar' para finalizar): ")
    
    if articulo.lower() == 'terminar':
        break
    
    precio = float(input("Ingrese el precio del artículo: "))
    
    cesta_de_compra[articulo] = precio

print("\nLista de la compra:")
total_coste = sum(cesta_de_compra.values())

for articulo, precio in cesta_de_compra.items():
    print(f"{articulo}: ${precio}")

print(f"\nCoste total: ${total_coste}")


