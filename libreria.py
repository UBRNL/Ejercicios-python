#items = input("Ingresa los paises separados con comas: \n")

#paises = [pais for pais in items.split(",")]

#print(",".join(sorted(list(set(paises)))))

from functools import reduce

def ej2(lista): 
    resultado = list(filter((lambda x: x % 2), lista)) 
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(resultado)

lista = list(range(100))

ej2(lista)
