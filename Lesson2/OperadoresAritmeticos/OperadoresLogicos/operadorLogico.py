#Operadores Logicos
#and esta exprecion devuelve true si ambos valores son verdaderos en otro caso devulve falso
#or esta exprecion dvuelve true si alguno de los valores son verdaderos en otro para devolver falso ambos valores deven ser falsos
#not es un operador unario solo nececita de un valor para funcionar 

#Ejemplo con and
a=True
b=False
resultado= a and b
print(f"Exprecion realizada con true and true para AND: {resultado}")
print(f"Exprecion realizada con true and false para AND: {resultado}")

resultado= a or b
print(f"Exprecion realizada con true and false para OR: {resultado}")

resultado= not a
print(f"Exprecion realizada con true and false para OR pero negando a a: {resultado}")

