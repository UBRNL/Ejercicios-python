def area_triangulo( altura:float, base:float)-> float:
    return base * altura
resultado = area_triangulo(186, 95)
print("El area del triangulo es: ",resultado, "CM2")

def area_del_circulo(radio:float,Pi = 3.14)->float:
    return (radio * radio)* Pi
resultado = area_del_circulo(6)
print("El area del circulo es: ",resultado, "CM2")
