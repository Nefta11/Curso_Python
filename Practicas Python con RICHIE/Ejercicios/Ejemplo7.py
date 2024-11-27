class bicla:
    def __init__(self, tipo_sillon, num_ruedas, diametro_rueda, tipo_color):
        print(f"Creando una bicicleta {tipo_sillon} con {num_ruedas} ruedas, {diametro_rueda} de diámetro y color {tipo_color}")
        def frenar(self):
            print("La bicicleta está frenando")
        def girar(self):
            print("La bicicleta está girando")
        def pedalear(self):
            print("La bicicleta está pedaleando")
        def avanzar(self):
            print("La bicicleta está avanzando")
    


Bici = bicla("Doble", 2, 26, "Roja")
print(type(Bici))

Bici.avanar()
Bici.pedalear()
Bici.girar()
Bici.frenar()