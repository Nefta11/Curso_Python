#Ejercicio determinar si la edad de una persona es mayor o menor de edad

años=18

print("Programa que determina si eres mayor o menor de edad")
print("----------------------------------------------------")

edad=int(input("Digite su edad en el siguiente campo:"))

if edad >= años:
    print(f"Usted es mayor de edad Felicidades tienes: {edad} años")
else:
    print(f"No eres mayor de edad, lo siento pequeñin tu edad es: {edad} años")