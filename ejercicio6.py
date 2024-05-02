"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) como claves de un diccionario, pregunte al usuario la
nota que ha sacado en cada asignatura y actualice cada entrada del diccionario. Imprimir el
diccionario al final del programa."""


dict_notas = {"Matemáticas": None, "Física": None, "Química": None, "Historia": None, "Lengua": None}

for asignatura in dict_notas:
    nota = input(f"Ingrese la nota de {asignatura}: ")
    dict_notas[asignatura] = float(nota)

print(f"Notas finales:")
print(dict_notas)

