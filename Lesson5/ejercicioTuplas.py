#Dada la siguien tupla,
#Crear una lista que solo incluya los números menores a 5

tuplas =(12,1,8,3,2,5,8)
lista =[]

#Filtramos los elementos menores a 5 de la tupla
for tupla in tuplas:
    if tupla <5:
        lista.append(tupla)

#Imprimimos la lista
print(lista)