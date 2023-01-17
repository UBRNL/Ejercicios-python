def elevar_x_a_la_y(x:int = 0, y:int = 0)->int:
    return x**y

##PROGRAMA PRINCIPAL
base = int(input("Digita la base: "))
potencia = int(input("Digita la potencia: "))

elevar_con_dos_parametros = elevar_x_a_la_y(base, potencia)
print("El resultado de elevar ", base, "a la ",potencia,"es: ", elevar_con_dos_parametros)


elevar_con_un_parametro = elevar_x_a_la_y(base)
print("El resultado de elevar ",base, "a la cero", "es:", elevar_con_un_parametro)

elevar_solo_con_potencia = elevar_x_a_la_y(y = potencia)
print("El resultado de elevar cero a la ", potencia, "es: ", elevar_solo_con_potencia)



elevar_sin_parametros = elevar_x_a_la_y()
print("El resultado de elevar cero a la cero ", "es: ", elevar_sin_parametros)
