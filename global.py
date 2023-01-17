class Hola:
    def patata(self):
        print("toma")

h = Hola()
globals()["h"].patata()

# Ejemplo de una class estatica.

class Hola:
    def patata():
        print("toma")

globals()["Hola"].patata()