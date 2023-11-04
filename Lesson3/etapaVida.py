#Programa que pide que proporciones tu edad y dependiendo de esta te dara un mensaje.
print("------------------------------------")
edad= int(input("Proporciona tu edad: "))


if 0 <= edad <10:
    print(f"Tu edad es de {edad} \nLa infancia es increible vive al maximo bebe...")
elif 10<= edad < 20:
    print(f"Tu edad es de {edad} \nMuchos cambios y mucho estudio...")
elif 20 <= edad < 30:
    print(f"Tu edad es de {edad} \nAmor y comienza el trabajo...")
else:
    print("Etapa de vida no reconocida Bobito")

