import pickle

class Juguete:
    nombre = "potato"
    precio = 1.25

    def __int__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def getNombre(self):
        return self.nombre

f = open('datos.bin', 'rb')
potato = pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre(), 'precio:',potato.precio)
## repr, es la forma tecnica
## str es la forma que se puede ver 
