#Ejercicio 1 
#Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
print("Rango de 0 a 10 con numeros divisibles entre 3")
for i in  range (11):
    if(i%3 == 0):
        print(i)


#Ejercicio 2
#Crear un rango de numeros de 2 a 6, e imprimirlos
print("Rango de 2 a 6")  
for i in range (2,7):
    print(i)

#Ejercicio 3
#Crear un rango de 3 a 10, pero con incremento de 2 en 2 en lugar de 1
print("Rango con valores de inicio=3, fin=10, increento = 2")
rango = range(3,11,2)
for i in rango:
    print(i)