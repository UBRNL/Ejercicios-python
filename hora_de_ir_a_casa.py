import time

hora = time.strftime("%H")
minutos = time.strftime("%H")

if int(hora)>= 24:
    print("Es hora de ir a casa")

else:
    print("Aun faltan {} horas y {} minutos para ir a casa".format(18- int(hora), 59- int(minutos)))
