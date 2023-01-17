f = open('/etc/passwd', 'r')
datos = f.readlines()
#datos = None
#while datos != "":
#    datos = f.readline()
#    print(datos)
#datos = f.read()
f.close()
print(datos)


# r: lectura.
# a: ajuntar.
# w: escribir.
# x: crear.
# t: texto.
# b: binary.
# +
# f.read(18) es para leer hasta el dijito numero 18 o el que coloques dentro
# f.readline() es para ller una linea


