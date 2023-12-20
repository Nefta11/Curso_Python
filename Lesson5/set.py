#Coleccion de tipo SET

#Se caracteriza por:
#No mantiene un orden como la tupla y la lista(o tiene un indice)
#No permite almacenar elementos duplicados
#No es posible modificar los elemementos ya almacenados
#Si es posible agregar o eliminar elementos 

#Se utilizan llaves
planetas = {"Marte","Jupiter","Venus"}
print(planetas)

#largo de un SET
print(len(planetas))

#Revisar si un elemento esta presente
print("Marte" in planetas)

#Agregar elementos a nuestro SET
planetas.add("Tierra")
print(planetas)

#No se pueden duplicar elementos
planetas.add("Tierra")
print(planetas)

#Elimar un elemento dentro de SET
planetas.remove("Tierra") #Posiblemente arroje un error si no se encuentra el elemento que se quiere eliminar
print(planetas)
planetas.discard("Júpiter") #ESTA FUNCION TAMBIEN ELEIMINA UN ELEMENTO DENTRO DE SET PERO NO ARROJA ERROR EN CASO DE QUE NO SE ENCUENTRE EL ELEMENTO COMO EL ANTERIOR
print(planetas)



