class Motor: # Tiene objeto de tipo Motor
    tipo = "Diesel"

class Ventanas: # Tiene objeto de tipo Ventan
    cantidad = 6 # dentrode ventana podemos crear un metodo para cambiar la cantidad

    def CambirCantidad(self, valor):
        self.cantidad = valor


class Ruedas: # Tiene objeto de tipo Rueda
    cantidad = 4

class Carroceria: # Tiene objeto de tipo Carroceria
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

c = Coche()
print("Motor es", c.motor.tipo)
print("Ventana: ", c.carroceria.ventanas.cantidad)
print("Las Ruedas son: ", c.carroceria.ruedas.cantidad)

c.carroceria.ventanas.CambirCantidad(7)
print("Las ventanas ahora son: ", c.carroceria.ventanas.cantidad)


