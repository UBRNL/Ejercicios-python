horas_pasiente = int(input ("Cuantas horas tienes con el dolor: "))
dias_pasiente = int(input ("Cuantos dias tienes con el dolor: "))
resultado = horas_pasiente * dias_pasiente
OMG = 48
if resultado > OMG:
    print("Tu vida esta en peligro,", resultado, "Es muchas horas")
elif resultado < OMG:
    print("Acude a un medico", resultado, "Es muchas horas")

