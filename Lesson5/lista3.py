#Preguntar el largo de una lista
nombres=["Belliham","Rodri","Benzema","Cristiano"]    

print(len(nombres))

#Agregar un elemento
nombres.append("Chicharo")#append es una funcion que ya vine cargada en python y nos sirve para agregar un nuevo elemento a la lista
print(nombres)

#Insertar un elemento en un indice proporcionado
nombres.insert(1,"Ronaldo")
print(nombres)

#Remover un elemento No por indice si no por valor
nombres.remove("Chicharo")
print(nombres)

#Remover el último valor agregado Elimina el ultimo elemento de la lista
nombres.pop()
print(nombres)