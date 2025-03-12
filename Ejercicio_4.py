# Construir una función como parámetro una lista de datos numericos y que retorne  el promedio de dichos datos

import random

print("--------------------------------")
print("-------PROMEDIO LISTA DATOS-----")
print("--------------------------------")

#Definicion de la función
def calcular_promedio_lista(numeros):
    suma = 0
    for i in lista:
        suma = suma + i
    promedio = suma / len(lista)
    return promedio
    
# Entrada
# Creamos una lista vacia
lista = []
# Tamaño lista
n = int(input("digite el tamaño de la lista: "))

for i in range(n):
   num = random.randint(14,18)
   lista.append(num)

#Procesamiento
print("Lista: ", lista)
print("El promedio de la lista es:", calcular_promedio_lista(lista))

#Salida
print("\nEso era...")


