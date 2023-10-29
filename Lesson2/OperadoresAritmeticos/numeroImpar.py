#Ejerecio verificar si un número ingresado por un usuario es par o impar

print("Programa que te verifica si un número es par o impar")
print("----------------------------------------------------")

Numero=int(input("Ingresa un número:"))
print(Numero % 2)
if Numero % 2 == 0:
    print(f"El número {Numero} es par")
else:
    print(f"El número de {Numero} es impar")    
    