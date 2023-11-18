#Palbra break dentro de los ciclos

for letra in 'Holanda':
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break #Rompe todo nuestro ciclo no imprime el else 
else:
    print("Fin ciclo for") 