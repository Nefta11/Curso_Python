class Bicicleta:
    def __init__(self, tipo_sillon, num_rin, diam_rueda, tipo_color):
        print(f"Creando una bicicleta {tipo_sillon} de {num_rin} rin, {diam_rueda} de diámetro y {tipo_color} color")

    def frenar(self):
        print("La bicicleta está frenando")

    def girar(self):
        print("La bicicleta está girando")

    def pedalear(self):
        print("Se esta pedaleando")

Baika = Bicicleta("Baika", "2", "26", "negro")

Baika.pedalear()
Baika.girar()
Baika.frenar()

