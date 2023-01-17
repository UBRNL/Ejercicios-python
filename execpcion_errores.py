num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

try:
    resultado = num1 / num2
    print(f"{num1} / {num2} =", resultado)
except ZeroDivisionError as e:
    print(e)
finally:
    print("Good job")
