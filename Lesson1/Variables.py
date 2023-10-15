miVariable="Hola Jovenes"

print(miVariable)
print(miVariable)

miVariable="Hola Cambie la variable para demostrar que el codigo de ejecuta lineal"
print(miVariable)

print("-----------------------------------")
print("Suma de dos números")
numero1=100
numero2=88.9
resultado=numero1+numero2
print("La suma de ",numero1," + ",numero2," = ",resultado)

print("--------------------------------------------------------------------------")
print("--------------------------------------------------------------------------")
print("Buscaremos la dirección de memoria en donde se encuentran almacenadas nuestras variables:")
print("--------------------------------------------------------------------------")
print("La variabre: ",miVariable, " se encuentra almacenada en la dirección de memoria: ", id(miVariable))
print("La variabre: ",numero1, " se encuentra almacenada en la dirección de memoria: ", id(numero1))
print("La variabre: ",numero2, " se encuentra almacenada en la dirección de memoria: ", id(numero2))
print("La variabre: ",resultado, " se encuentra almacenada en la dirección de memoria: ", id(resultado))
#Utilizamos ID() y dentro de la funcion colocamos nuestra variable, esto sirve para que nos muestra la dirección de memoria de nuestras variables
#La dirección de variable no es constatnte y puede cambiar cada vez que se ejecuta el codigo ya que se almacena en la RAM
