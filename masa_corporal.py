def calculo_imc(peso:float, altura:float)->float:

    imc = peso/((altura)**2)
    return imc

peso = input("Dijita su peso en Kg: ")
estatura = input("Dijita su estatura:" )
indice = round (calculo_imc (float(peso), float(estatura)))
print("indice de masa corporal es : ", indice)
