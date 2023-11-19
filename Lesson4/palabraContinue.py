# for i in range(6):#Funcion de range, le das un rango de nuemero y te da esa cantidad iniciando en 0
#   if i % 2 ==0: #De esta manera nos manda solo los numeros pares
#      print(f"Valor: {i}")


#Aqui vamos a utilizar la palabra continuos

for i in range(6):
    if i%2 !=0:
        continue  #Ejecuta la siguiente iteración y ya no ejecuta ninguna de las siguientes.
    print(f"Valor : {i}")