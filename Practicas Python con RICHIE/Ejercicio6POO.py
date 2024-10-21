class Perro:
    especie = "mamifero"
    def __init__(self,nombre,raza):
        print(f"Creando un perro {nombre} de raza {raza}")
    def ladrar(self):
        print("Guau, guau, guau")
    def caminar(self, pasos):
        print(f"El perro realizo {pasos} pasos")

mi_perro = Perro("Toby","Labrador")
su_perro = Perro("Firula","Bulldog")

print(type(mi_perro))

print(mi_perro.especie)
print(su_perro.especie)
print(Perro.especie)

mi_perro.ladrar()
su_perro.ladrar()

mi_perro.caminar(10)
su_perro.caminar(20)