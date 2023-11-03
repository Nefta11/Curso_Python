#Ejercicio simple
print("Inserte los siguientes datos del libro:")

name=input("Proporcione el nombre:")
id=int(input("Proporcione el ID:"))
price=float(input("Proporcione el precio:"))
send=bool(input("Indica si el envio es gratuito (True/False): "))


print("------------------------------------------------")
print(f"Nombre:{name}")
print(f"ID: {id}")
print(f"Precio: {price}")
print(f"Envio Gratuito: {send}")
print("-----------------------------------------------")
