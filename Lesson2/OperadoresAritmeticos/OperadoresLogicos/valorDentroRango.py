#Ejercicio que determina si el valor que mete el usuario esta dentro de un rango
valor=int(input("Escriba un valor que este dentro del rango 0 a 10:"))

if (valor >=0) and (valor <=10):
    print(f"El número: {valor} esta dentro del rango indicado")
else:
    print(f"El número: {valor} no esta dentro del rango indicado")