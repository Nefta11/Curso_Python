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

