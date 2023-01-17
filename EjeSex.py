def perimetro_trangulo(cateno1:float, cateno2:float)->float:
    hipotenusa = calcular_hip(cateno1, cateno2)
    return cateno1 + cateno2 + hipotenusa
def calcular_hip(cateno1:float,cateno2:float):
    suma_cuadrado = (cateno1**2) + (cateno2**2)
    hipotenusa = pow(suma_cuadrado,0.5)
    return hipotenusa
cadena_cat_1 = input("Indique la longitud del primer cateto: ")
cadena_cat_2 = input("Indique la longitud del segundo cateto: ")
cat_1 = float(cadena_cat_1)
cat_2 = float(cadena_cat_2)
perimetro = perimetro_trangulo(cat_1, cat_2)
print("El perímetro de un triángulo rectángulo que tenga catetos de longitud", cat_1, "y", cat_2, "es", perimetro)

    
