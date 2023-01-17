def promedio_lista(numeros:list)->float:
    sumatoria = 0
    total = 0

    for i in numeros:
        if i > 0:
            sumatoria += i
            total += 1

    promedio = sumatoria/total
    return promedio
lista = [4, -1, -4, 5, 3, 4, -10, 14, 22, -35, 40, 41]
print(promedio_lista(lista))


def menor_posicion_lista(numeros:list)->int:
    indice = 0
    menor = numeros[0]

    for num in range(0, len(numeros)):
        if numeros [num] < menor:
            indice = num
            menor = numeros[num]
    return indice

lista = [4, -1, -4, 5, 3, 4, -10, 14, 22, -35, 40, -61]
print(menor_posicion_lista(lista))
