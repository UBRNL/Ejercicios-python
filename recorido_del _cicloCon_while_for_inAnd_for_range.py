def suma_recorido_total_con_while(lista:list)->int:
    i = 0
    suma = 0
    while i < len(lista):
        suma += lista[i]
        i += 1
        return suma

## len es igual a longitud
    
def suma_recorido_total_con_for_in_range(lista:list)->int:
    suma = 0
    for i in range(0, len(lista)):
        suma += lista[i]
        return suma

def suma_recorido_total_con_for_in(lista:list)->int:
    suma = 0
    for cadena_numero in lista:
        suma += cadena_numero
        return suma
