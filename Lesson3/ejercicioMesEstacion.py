#Ejercio que pide al usuario ingresar un mes del año y dependiendo 
#El mes le devolvera la estación

print("Programa que te muestra la estación del año dependiend el mes que metas...")
print("-----------------------------------------------")

month= int(input("Inserta el mes del año del 1 al 12:"))
#None es equivalente a null en otros lenguajes de programación
station= None

if month == 3 or month== 4 or month == 5:
    station= "Invierno"
    print(f"El mes:{month} esta dentro de la estación: {station} ")
elif month == 6 or month== 7 or month== 8:
    station = "Verano"
    print(f"El mes:{month} esta dentro de la estación: {station} ")
elif month == 9 or month== 10 or month== 11:
    station="Otoño"
    print(f"El mes:{month} esta dentro de la estación: {station} ")
elif month == 12 or month== 1 or month== 2:
    station="Invierno"
    print(f"El mes:{month} esta dentro de la estación: {station} ")
else:
    print("Valor no valido Bro")

    