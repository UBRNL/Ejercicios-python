from math import sqrt

x = float(input("Digite un numero positivo: ")) # El usuario digita el numero.
while x < 0:
    print("No puedes ingresar un numero negativo") # Mientra que el numero no sea positivo se seguira repitiendo.
    x = float(input("Digite un numero positivo: "))
print("La raiz cuadrad de {0} es {1}".format(x, sqrt(x))) # Si el usario digita el numero positivo se realizara esta funcion .
