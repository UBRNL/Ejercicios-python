def calcular_precio_pasaje(temporada_alta: bool, compañia: str, edad: int, estudiante: bool)->int:
    precio = 5000000
    variaciones = 0
    seguro = False

    if compañia == "ALAS":
        if temporada_alta:
            variaciones +=0.3
        else:
            if edad >= 18 and estudiante:
                variaciones -= 0.1
    elif compañia == "VOLAR":
        if temporada_alta:
            variaciones += 0.2
        if edad > 60:
            seguro = True

    if edad < 18:
        variaciones -= 0.5

    precio *=(1+variaciones)

    if seguro:
        precio += 100000
    return round (precio)
temp = bool(int(input("Es temporada alta? Ingresa 1 para SI o 0 para NO: ")))
compañia = input("Ingresa la compañia para la que viajara: ")
edad = int(input("Ingresa la edad de la persona: "))
est =bool(int(input("Es estudiante? Ingresa 1 para SI o 0 para NO: ")))

tarifa = calcular_precio_pasaje(temp, compañia, edad, est)

print ("La tarifa del pasaje es de $"+str(tarifa)+" COP")
