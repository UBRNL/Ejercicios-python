def operaciones(a, b):
    return a + b, a - b, a * b, a / b

resultado = operaciones(5, 5)
print(resultado)


##Funcion anonima es muy difente, es para realizar una funcion simple, ejemplo:::


anonima = lambda nombre, nombre2: print("Hola", nombre, "adios", nombre2)
anonima("pepe", "oscar")

sumatoria = lambda x: (x+x)*2
print(sumatoria(3))
