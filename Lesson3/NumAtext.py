numero= int(input("Proporciona un valor entre 1 y 3:"))

numeroT=""

if numero == 1:
    numeroT = "Número uno"
elif numero == 2:
    numeroT = "Número dos"
elif numeroT == 3:
    numeroT = "Número tres"
else:
    print("Numero fuera de rango bobito")

print(f"Numero proporcionado: {numero} - {numeroT}")