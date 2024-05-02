import json
import csv

cesta_de_compra = {}

while True:
    articulo = input("Ingrese el nombre del artículo (o 'terminar' para finalizar): ")
    
    if articulo.lower() == 'terminar':
        break
    
    precio = float(input("Ingrese el precio del artículo: "))
    
    cesta_de_compra[articulo] = precio

# Mostrar la lista de la compra y el coste total
print("\nLista de la compra:")
total_coste = sum(cesta_de_compra.values())

for articulo, precio in cesta_de_compra.items():
    print(f"{articulo}: ${precio}")

print(f"\nCoste total: ${total_coste}")

# Guardar el diccionario en formato JSON
with open("cesta_de_compra.json", "w") as json_file:
    json.dump(cesta_de_compra, json_file, indent=4)

# Guardar los datos en un archivo CSV
with open("cesta_de_compra.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Artículo", "Precio"])
    for articulo, precio in cesta_de_compra.items():
        writer.writerow([articulo, precio])

print("Datos guardados en archivos JSON y CSV.")