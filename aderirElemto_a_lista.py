mi_lista = []
mi_lista.append(5)
mi_lista.append(10)
mi_lista.append(19)
mi_lista.append(20)
mi_lista.append(25)
print(mi_lista)

mi_lista.insert(1, 20)## insertar en la posiscion 1 el numero 9.
print(mi_lista)

print(mi_lista.count(20)) ## contar cuantas veces esta el numero 20 en la lista.

mi_lista.extend([5, 12, 22, 32])## para agregar una lista al final de la lista.
print(mi_lista)

## para buscar la posicion de un numero

print(mi_lista.index(25))

## para invertir los elemntos de una lista.

mi_lista.reverse()
print(mi_lista)

## para ordenar una lista
mi_lista.sort()
print(mi_lista)

## eliminar un elemnto
mi_lista.remove(20)
print(mi_lista)

## hacer una copia de una lista
otra_lista = mi_lista.copy()
print(otra_lista)
## remueve un elemnto de la lista, y retorna el que elimino en una varaibale.
eliminado = mi_lista.pop(2)
print(eliminado)
