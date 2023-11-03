#Ejercicio simple
print("Inserte los siguientes datos del libro:")

name=input("Proporcione el nombre:")
id=int(input("Proporcione el ID:"))
price=float(input("Proporcione el precio:"))
send=input("Indica si el envio es gratuito (True/False): ")

if send == "True":
    send = True
elif send =="False":
    send=False
else:
    send= 'Valor incorrecto, debe escribir True/False'
    
print("------------------------------------------------")
print(f"Nombre:{name}")
print(f"ID: {id}")
print(f"Precio: {price}")
print(f"Envio Gratuito: {send}")
print("-----------------------------------------------")
