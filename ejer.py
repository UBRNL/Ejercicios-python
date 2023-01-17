def calcular_IMC(peso:float, altura:float,)->float:
    imc = peso/((altura)**2)
    return imc

peso = float(input("Digita su peso en Kg: "))
estatura = float(input("Digita su altura en M: "))
print("Su indice de masa corpora es: ", round(calcular_IMC(peso,estatura), 2))
