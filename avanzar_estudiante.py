def avanzar_estudiante(est1:dict, est2:dict, est3:dict, est4:dict)->dict:
    est1["ssc"] += 1
    est2["ssc"] += 1
    est3["ssc"] += 1
    est4["ssc"] += 1
## programa principal

e_1 = {"nombre": "Fionha", "codigo": 1233456, "genero": "femenino", "ssc": 3}
e_2 = {"nombre": "Jose", "codigo": 12334987, "genero": "masculino", "ssc": 2}
e_3 = {"nombre": "nikolas", "codigo": 1202456, "genero": "masculino", "ssc": 3}
e_4 = {"nombre": "cristian", "codigo": 1233000, "genero": "masculino", "ssc": 4}

print("Semestre estudiante 1:", e_1["ssc"])
print("Semestre estudiante 2:", e_2["ssc"])
print("Semestre estudiante 3:", e_3["ssc"])
print("Semestre estudiante 4:", e_4["ssc"])

avanzar_estudiante(e_1, e_2, e_3, e_4)

print("Nuevo semestre estudiante 1:", e_1["ssc"])
print("Nuevo semestre estudiante 2:", e_2["ssc"])
print("Nuevo semestre estudiante 3:", e_3["ssc"])
print("Nuevo semestre estudiante 4:", e_4["ssc"])
