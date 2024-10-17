#Sintaxis correcta del ciclo for
for i in range(3):
    print('contador con ciclo for',i)

#Sintaxis correcta del ciclo while
x=0
while x < 3:
    print('contador con ciclo while',x)
    x+=1

#Utilizar ciclo for con palabra continue
print('Utilizar for con continue')
for i in range(7):
    if i == 4:
        continue
    print(i)

#ciclo while con instruccion para romper la ejecucion 
print('----------------------Ciclo while con brake----------------------')
x=0
while True:
    if x == 3:
        break
    x+=1
    print(x)
    
#Manejo de excepciones assert, try, except, finally, raise
print('----------------------assert, try, except, finally, raise----------------------')
x='10'

valor=None
try:
    #valor=x
    valor=int(x)

    y=3
    c=valor+y
    print(c)
except Exception as e:
    print('Hay un error:',e)
finally:
    print('El valor es',valor)

#Variables globales y locales
print('-------------Variables globales y locales-------------')
a=0

def suma_uno():
    for i in range(6):
        global a
        print(a)
        a=a+1
    print('La variable global a tiene un valod de:',a)

print('La variable global a tiene un valod de:',a)
suma_uno()
print('La variable global a tiene un valod de:',a)

#Variable nonlocal
