#Diccionarios en PYTHON
#(Se compone de una key y value)

diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario)

#Largo de elementos

print(len(diccionario))

#Acceder a un elemento con (key)
print(diccionario['IDE'])
#Otra forma de acceder un elemento
print(diccionario.get('OOP'))
#Modificar elementos 
diccionario['IDE'] ='integrated development environment'
print(diccionario)

#Recorrer los elementos 

for termino, valor in diccionario.items():#Con la funcion items nos permite recuperar key y value en un recorrido con for
    print(termino, valor)

for termino in diccionario.keys():#Con esta funcion recuperamos solamente la llave
    print(termino)

for valor in diccionario.values():#Con esta funcion solo imprimimos el valor de nuestra llave
    print(valor)

