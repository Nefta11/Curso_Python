#Aqui comenzamos a ver las sentencia if/else

condicion= True
#En python no necesariamente tenemos que tener los valores flase y verdadero
#Ya que por default una cadena que contenga algo lo detectara como true
#y si la cadena esta vacia devuelve falso

#Con el siguiente ejemplo ya si jala el boolena ya que hace las comprobaciones primero


if condicion == True:
    print('condición verdadera')
elif condicion == False:
    print('Condición falsa')
else:
    print('Condición no reconocida')