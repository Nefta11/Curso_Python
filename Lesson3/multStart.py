import turtle

ventana= turtle.Screen()
ventana.bgcolor("black")
bicho = turtle.Turtle()
bicho.speed(1)
bicho.color('red')
numero_estrella= 75

for i in range(numero_estrella*5):
    bicho.forward(i*3)
    bicho.right(145)

ventana.exitonclick()