# Clases dinamicas #
#class Dino:
#    encender = False
 #   def inicia(self):
  #      pass

#k = Dino()
#print(k.encender)

# clases estaticas
#class Opciones:
 #   ServidorSeguro = True
 #   Reiniciar = False

#if Opciones.ServidorSeguro:
#   pass

#if Opciones.Reiniciar:
#    pass


# Eredar clases , de la clase madre ejemplo.
class Jugete:
    _encendido = True
    def __init__(self) -> None:
        print("estoy en el constructor de la clase Jugete")
    def enciende(self):
        print("Enciendo el aparato")
        self._enecendido = True
    def apaga(self):
        print("Apago el parato")
        self._encendido = False
    def isEncendido(self):
        return self._encendido

class Potato(Jugete):
    def quitarOreja(self):
        pass
    def ponerOreja(self):
        pass

class Dino(Jugete):
    color = None
    nombre = None
    def __init__(self, nombre):
        super().__init__(nombre)
        print("Estoy en el constructor de Dino")


    def verEscama(self):
        pass


p = Dino("Midinosaurio") #esto es instanciar..
p.enciende()
print(p.isEncendido())
p.apaga()
print(p.isEncendido()) 

