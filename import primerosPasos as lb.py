import primerosPasos as lb

def ejecutar_convertir_a_dolares(trm:float)->None:
    pesos = float(input("ingrese la cantidad de peso: "))
    dolares = lb.convertir_a_dolares(pesos,trm)
    print(pesos, "pesos son:" , round(dolares,2),"dolar")

def ejecutar_convertir_a_pesos(trm:float)->None:
    dolares = float(input("ingrese la cantidad de dolares: "))
    pesos = lb.convertir_a_pesos(dolares,trm)
    print(dolares, "dolares son:" , round(pesos),"pesos")

def iniciar_aplicacion()->None:
    trm = float(input("ingrese la TRM: "))
    ejecutar_convertir_a_dolares(trm)
    ejecutar_convertir_a_pesos(trm)

iniciar_aplicacion()
                     