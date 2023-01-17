def es_palindromo(cadena:str)->bool:
    palindromo = False
    sin_espacio = cadena.replace(" ","")
    en_minus = sin_espacio.lower()

    i =0
    j =len(en_minus)-1

    while i < j and en_minus[i] == en_minus[j]:
        i +=1
        j -=1

    if i == j:
        palindromo = True
    return palindromo
