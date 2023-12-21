diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario)

#Recorrer los elementos 

for termino, valor in diccionario.items():#Con la funcion items nos permite recuperar key y value en un recorrido con for
    print(termino, valor)

for termino in diccionario.keys():#Con esta funcion recuperamos solamente la llave
    print(termino)

for valor in diccionario.values():#Con esta funcion solo imprimimos el valor de nuestra llave
    print(valor)

#Comprobar existencia de algun elementos
    print('IDE' in diccionario)

#Agregar un elemento a dicc
    diccionario['PK']="Primry Key"
    print(diccionario)

    #No es posible agregar llaves duplicadas , si agregamos una llave existente sobreescribe la llave con el nuevo valor

#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#Limpiar
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario
print(diccionario)