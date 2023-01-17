from math import pi

radio = float(input("Digite el radio del circulo: "))

print("Seleccione una opcion: ")
print("a) Calcular el diametro. ")
print("b) Calculaer el perimetro. ")
print("c) Calcular el area. ")

opcion = input("Digite a, b o c y pulse enter: ")

if opcion == "a":
    diametro = 2 * radio
    print("El diametro es:", diametro)
elif opcion == "b":
    perimetro = 2 * pi * radio
    print("El perimetro es:", perimetro)
elif opcion == "c":
    area = 2 * pi * radio ** 2
    print("El area es:", area)
else:
    print("Solo hay 3 opciones: a, b o c")
    print("Usted tecleo: opcion")
