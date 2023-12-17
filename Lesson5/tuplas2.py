verduras =("Cebolla","Aguacate","Tomate")

print(verduras)

#recorre elementos

for verdura in verduras:
    print(verdura, end= " ")#Se imprime en una sola linea solo dejando un espacio en blanco

#Cambiar valor de una tupla

#Conversion de tupla a lista para modificarla
    
verdurasLista= list(verduras)#Con esta funcion se convierte nuestra tupla a lista
verdurasLista[0]="Zanahoria"
verduras= tuple(verdurasLista) # Sirve para cambiarla a tupla nuevamente
print("\n",verduras)


#Eliminar la tupla por completo

del verduras
print(verduras)