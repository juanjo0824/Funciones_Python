# Construir una función que reciba como parámetro una lista de datos numericos y retorne la suma de dichos datos.

print("--------------------------------")
print("------SUMA LISTA DATOS----------")
print("--------------------------------")

#Definicion de la función 
def sumar_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i 
    return suma    

# Entrada
lista = [1,2,3,4,5,6]

# Procesamiento
print("La suma es", sumar_lista_datos(lista))

#Salida 
print("\nEso era...")