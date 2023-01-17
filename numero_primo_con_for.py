def es_numero_primo(numero:int)->bool:
    primo = True
    for i in range(2, numero): ## buscaremos desde el 2 hasta el anterior al numero
        if numero % i == 0:
            primo = False

        return primo
