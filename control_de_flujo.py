# > mayor que
# < menor que
# > = mayor o igual
# < = menor o igual
# == exactamente igual

# AND, es True cuando los dos lados sean cierto, de resto es False.
# (True and False) = False
# (True and True) = True
# (False and False) = False
# (False and True) = False

# OR, es True siempre que exista un True, de lo contrario es False.
# (True or False) = True
# (True or True) = True
# (False or False) = False
# (False or True) = True

# IF, los if solo se ejecunta si la condicion es True.

a = 5
b = 6
c = 7
if (a == 5)and (b > 7) or (c == 7 and b < c):
    print(True and False or True and True)