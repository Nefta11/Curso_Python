#Función input para procesar la entrada de datos de usuarios 
mensaje=input("Escribe un mesnsaje: ")

#Por default cuando mandas un input en python espera recibir una cadena osea string
print("El mensaje que has escrito es:",mensaje)
print("Fin del programa.....")
print("-----------------------------------------------------------------")


#para que en un input se pueda meter un int o floar tienes que hacer como un tipo casteo, ejemplo: int(input("mensaje que quieras"))
numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa un segundo número: "))
multiplicación = numero1 * numero2
print("El resultado de la multiplicacion del número: ",numero1," * ",numero2," = ",multiplicación)
