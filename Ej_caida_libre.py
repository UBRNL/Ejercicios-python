def funcion_1()->str:
    return "Hola mi amigo "

def funcion_2(palabra:str)->str:
    return funcion_1()+str(palabra)


resultado = print(funcion_2("Juan"))
print("El resultado de mi funcion es: " + str(resultado))
