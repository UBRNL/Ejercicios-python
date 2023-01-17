def saludar(nombre: str)-> str:
   return "Hola " + nombre + "!"

nombre = input("¿Cuál es su nombre? ")
saludo = saludar(nombre)
print(saludo)
