class Perro:
    especie = "mamifero"
    def __init__(self,nombre,raza):
        print(f"Creando un perro {nombre} de raza {raza}")
    def ladrar(self):
        print("Guau")
    pass

mi_perro = Perro("Toby","Labrador")
su_perro = Perro("Firula","Bulldog")

print(type(mi_perro))

print(mi_perro.especie)
print(su_perro.especie)
print(Perro.especie)

mi_perro.ladrar()