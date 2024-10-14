#Funciones
llave = False

def encender():
     print ("colocar llave")
     llave = True
     if (llave):
        print("carro encendido")
     return True

def avanzar(llave):
     if (encender()):
        print ("avanzar, run, ruun")
     else:
        print ("No puedes avanzar, carro apagado")  


def frenar():
    print ("frenar, parar, parkear")

def retroceder():
        print ("retroceder, reversa, reversa")

def pitar():
     print ("pitar, gritar, gritar")  


def apagar():
     print ("quitar llave")
     llave= False
     if (llave == False):
          print("carro apagado")

def girarIzquierda():
     girarI=True
     print ("girar a la izquierda")
     return girarIzquierda

def girarDerecha():
     girarD=True
     print ("girar a la derecha")
     return girarD

##encender()
avanzar(True)
retroceder()

if(girarDerecha()): 
     print ("No puedes girara a la izquierda")
     girarI=False
if(girarIzquierda()):
     print ("No puedes girar a la derecha")
     girarD=False