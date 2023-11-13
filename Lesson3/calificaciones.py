#Ejercicio de calificaciones
print("Programa que determina como te fue de B a F dependiendo tu calificación")
calif=int(input("Ingresa tu calificación 0-10"))

if (9>calif<10):
    print("A")
elif(8>calif<9):
    print("B")
elif(7>calif<8):
    print("C")
elif(6>calif<7):
    print("D")
elif(0>calif<6):
    print("F")