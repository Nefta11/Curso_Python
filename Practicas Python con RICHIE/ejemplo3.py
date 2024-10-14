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
     print ("girar a la izquierda")

def girarDerecha():
     print ("girar a la derecha")

##encender()
avanzar(True)