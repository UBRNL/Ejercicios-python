def buscar_estudiante(est1:dict, est2:dict, est3:dict, est4:dict, nom:str)->dict:
    buscado = None

    if est1["nombre"] == nom:
        buscado = est1
    elif est2["nombre"] == nom:
        buscado = est2
    elif est3["nombre"] == nom:
        buscado = est3
    elif est4["nombre"] == nom:
        buscado = est4

    return buscado

## programa principal

e_1 = {"nombre": "Fionha", "codigo": 1233456, "genero": "femenino"}
e_2 = {"nombre": "Jose", "codigo": 12334987, "genero": "masculino"}
e_3 = {"nombre": "nikolas", "codigo": 1202456, "genero": "masculino"}
e_4 = {"nombre": "cristian", "codigo": 1233000, "genero": "masculino"}

nombre = input("Ingres el nombre del estudiante: ")
est_buscado = buscar_estudiante(e_1, e_2, e_3, e_4,nombre)

if est_buscado is None:
    print("El estudiante no existe")
else:
    print("El estudiante existe y su codigo es ", est_buscado["codigo"])
