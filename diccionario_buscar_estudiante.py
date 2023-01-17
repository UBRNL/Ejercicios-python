def buscar_estudiante(est1:dict,est2:dict,est3:dict,est4:dict,nom:str)->dict:
    buscado = None


    if est1["nombre"]==nom:
        buscado = est1
    elif est2["nombre"]==nom:
        buscado = est2
    elif est3["nombre"]==nom:
        buscado = est3
    elif est4["nombre"]==nom:
        buscado = est4

        return buscado
##CODIGO PRINCIPAL
e_1 = {"nombre": "Lina", "codigo": "2035689", "genero": "femenino", "carrera": "ingles", "promedio": 3.58,"ssc":2}

e_2 = {"nombre": "Oscar", "codigo": "2035786", "genero": "masculino", "carrera": "ingles", "promedio": 4.58,"ssc":2}

e_3 = {"nombre": "Jose", "codigo": "2035015", "genero": "masculino", "carrera": "frances", "promedio": 3.00,"ssc":1}

e_4 = {"nombre": "Fionha", "codigo": "2035986", "genero": "femenino", "carrera": "aleman", "promedio": 3.18,"ssc":3}


nombre = input("Ingrese el nombre del estudiante a buscar: ")

est_buscado = buscar_estudiante(e_1, e_2, e_3, e_4, nombre)

if est_buscado is None:
    print("El estudiante NO existe")
else:
    print("El estudiante existe y su codigo es ", est_buscado)

