class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
      
    def mostrar(self):
        print("El nombre: ",self.nombre)
        print("La nota: ",self.nota)
 
   
    def resultado(self):
        if self.nota < 5:
            print("El alumno ha reprobado")
        else:
            print("El alumno ha aprobado")
 
 
 

# los nuevos objetos
alumno1 = Alumno()
alumno2 = Alumno()
 
# los atributos
alumno1.inicializar("Fionha",4.5)
alumno2.inicializar("Jose",5.0)
 

alumno1.resultado()
alumno1.resultado()
alumno2.resultado()
alumno2.resultado()
