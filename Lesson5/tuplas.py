#Una tupla es como una lista pero a diferencia de la lista 
#Nuestra tupla no se le puede agregar, modificar o eliminar datos de esa lista
#Si no que se queda con los elementos que ya tiene TIPO INMUTABLE

#definir una tupla
#NO se utilian corchetes si no parentesis
frutas = ("Naranja","Platano","Mandarina")

#Saber la cantidades de elemento que tiene nuestra tupla
print(frutas)
print(len(frutas))
#Accedet a un elemento
print(frutas[0])

#Navegacion inversa
print(frutas[-1])#Para acceder a los indices si utilizamos corchetes

#Acceder a un rango
print(frutas[0:1])

#En las tuplas cuando solo tenemos un elemento al final se tiene que poner una coma
#Po que si no seria como un simple string
#Ejemplo ('Naranja',)<- de esa manera