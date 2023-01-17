from abc import ABC, abstractclassmethod, abstractmethod
# en esta clase se utilizan una serie de funciones que seran comunes para otras clases, lo que 
# se marque como metodo abstracto, sera obligatorioamente otilizados por las otras clases.
class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau")


class Gato(Animal):
    def sonido(self):
        print("mihau")
p = Perro()
p.sonido()
p = Gato()
p.sonido()