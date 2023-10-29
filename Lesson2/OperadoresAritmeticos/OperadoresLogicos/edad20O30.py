#Ejercicio que determina si la edad de una persona esta dentro del rango de los 20's o 30´s
print("Ejercicio que determina si la edad de una persona esta dentro de los 2o´s y 30´s")
print("--------------------------------------------------------------------")
Edad=int(input("Introducce tu edad en el siguiente campo:"))

##veintes= Edad >=20 and Edad<30
#treintas= Edad >= 30 and Edad <40

#if veintes or treintas:
 #   print(f"Su edad es de: {Edad} años esta dentro del rango 20's o 30´s")
#else:
 #   print(f"Su edad es de : {Edad} años no esta dentro del rango 20´s ni 30´s")


#Mismo ejercio pero de manera mas correcta 
#if (Edad >=20 and Edad<30) or (Edad >= 30 and Edad <40):
 #   print(f"Su edad es de: {Edad} años esta dentro del rango 20's o 30´s")
#else:
 #   print(f"Su edad es de : {Edad} años no esta dentro del rango 20´s ni 30´s")


#Sintaxis Simplificada para el and

if (20 >= Edad <30) or (30 >= Edad <40):
    print(f"Su edad es de: {Edad} años esta dentro del rango 20's o 30´s")
else:
    print(f"Su edad es de : {Edad} años no esta dentro del rango 20´s ni 30´s")

