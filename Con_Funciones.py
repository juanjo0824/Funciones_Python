print("--------------------------------")
print("- BUSCAR UN NUMERO EN CONJUNTO -")
print("--------------------------------")

#Definición de la funció
def buscarDatosEnLista(datoABuscar, lista):
  r = False
  for i in lista:
    if i == datoABuscar:
      r = True
  return r

#Entrada
dato = int(input("Número a buscar: ")) #se recibe el dato del usuario

#Procesamiento
listas = [1,2,3,4,5] #Se almacena una lista de datos
if buscarDatosEnLista(dato, lista):
  print("Lo encontre")
else:
  print("No lo encontre")

  #Salida
  print("\nEso era. . .")
    