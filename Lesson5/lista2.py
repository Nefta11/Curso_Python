#Acceder a un rango de nuestra lista

nombre= ["Neftali","Arturo","Hernandez","Vergara"]

#Imprimir un rango de la lista
print(nombre[0:2]) #En este ejemplo mostramos como recuperamos e imprimimos un rango de lo que tenemos en nuestra lista de nombres en este caso el nombre que aparece en la posicion 0 y 2

#Ir del inicio de la lista al indice (sin incluirlo )
print(nombre[:3])

#Desde el indice indicado hasta el final
print(nombre[1:])

#Cambiar un valor 
nombre[3]="Avryl"
print(nombre)