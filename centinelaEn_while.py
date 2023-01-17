#def contar_digito(numero: int)->int:
 #   contar = 0
  #  centinela = False

   # while centinela == False:
    #    if numero == 0:
     #       centinela = True
      #  else:
       #     contar += 1
        #    numero //= 10

    # return contar
# Programa principal
#num = int(input("Ingresa el numero entero: "))
#digitos = contar_digito(num)
#print("La cantidad de digito del numero es: ",digitos)        

def calcular_factorial(n: int)->int:
    contar = 0
    factorial = 1

    while factorial == False:
        if n == 0:
            factorial = True
        else:
            factorial *= n
            n -= 1
    return factorial

# Programa principal
numero = int(input("Ingresa el numero: "))

while numero < 0:
    print("No se permiten numeros negativos.")
    numero = int(input("Ingresa un numero: "))

print(numero, "! es igual a",calcular_factorial(numero))
