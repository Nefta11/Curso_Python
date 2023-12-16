#Acceder a un rango de nuestra lista

nombres= ["Neftali","Arturo","Hernandez","Vergara"]

#Imprimir un rango de la lista
print(nombres[0:2]) #En este ejemplo mostramos como recuperamos e imprimimos un rango de lo que tenemos en nuestra lista de nombres en este caso el nombre que aparece en la posicion 0 y 2

#Ir del inicio de la lista al indice (sin incluirlo )
print(nombres[:3])

#Desde el indice indicado hasta el final
print(nombres[1:])

#Cambiar un valor 
nombres[3]="Avryl"
print(f"Sustituyendo el elemendo en el indice 3",nombres)

#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No existen mas valores en la lista")

