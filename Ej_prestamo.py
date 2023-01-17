num = float(input("Valor a prestar: "))
si_es_menor = 1.2
si_es_mayor = 1.8
if num <= 30.000:
    print("Tu pagarias 1.2%. En total ", num * si_es_menor, "Pesos")
elif num >= 31.000:
    print("Tu pagarias 1.8%. En total " , num * si_es_mayor, "Pesos")
else:
    print("No cumples los requisitos ")
