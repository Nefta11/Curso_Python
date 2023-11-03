#Ejercicio simple
print("Inserte los siguientes datos del libro:")

name=input("Proporcione el nombre:")
id=int(input("Proporcione el ID:"))
price=float(input("Proporcione el precio:"))
send=input("Indica si el envio es gratuito (True/False): ")
##Siempre que metamo ya sea una cadena con algun caracter nos dara true al utilizar boll input
##Y en su caso contrario nos dara false su mandamos una cadena vacia
#Por lo que tenemos que hacer la comprobacion con if:
if send == "True":
    send = True
elif send =="False":
    send=False
else:
    send= 'Valor incorrecto, debe escribir True/False'


##Utilizamo triple comilla simple para concatenar varias cadenas y variables 
print("------------------------------------------------")
print(f'''Nombre:{name},
ID: {id},
Precio: {price},
Envio Gratuito: {send}''')
print("-----------------------------------------------")
