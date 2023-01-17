class Vehiculo:
    def color(self):
        print("Negro")
    def puertas(self):
        print(4)
    def ruedas(self):
        print(6)

class Coche(Vehiculo):
    def velocidad(self):
        print("180.kilometros por hora")
    def cilindraje(self):
        print("1.5")

p = Vehiculo()
p.color()

p = Coche()
p.cilindraje()
p.velocidad()

