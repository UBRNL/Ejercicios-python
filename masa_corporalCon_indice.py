def calculo_imc(peso:float, altura:float)->float:

    imc = peso/((altura)**2)
    return imc

peso = input("Dijita su peso en Kg: ")
estatura = input("Dijita su estatura:" )
indice = calculo_imc(peso, estatura)
print("Sindice de masa corporal es : ", indice)
