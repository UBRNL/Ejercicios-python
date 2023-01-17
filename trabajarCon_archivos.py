## para escribir en el texto se utiliza la "w"
## para aderir se utiliza la "a"
## para leer el texto se utiliza la "r"

notas = {
    "Iris": 60,
    "Alain": 75,
    "Jose": 60,
    "Ubernel": 100
    }
with open("Data.txt", "w")as archivo:
    for nombre, nota in notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")
