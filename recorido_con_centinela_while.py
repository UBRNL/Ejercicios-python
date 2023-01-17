def posicion_recorido_parcial_con_centinela (lista = input("Ingresa la lista: "),buscador = input(int("Ingresa el buscador: ")))->int:
     
    i = 0
    posicion = -1
    ya_encontre = False
    while i < len(lista) and ya_encontre == False:
        if lista[i] == buscador:
            ya_encontre = True
            posicion = i
        i += 1
        return posicion
