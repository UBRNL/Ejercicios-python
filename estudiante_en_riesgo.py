def quienes_en_riesgo(est1:dict, est2:dict, est3:dict, est4:dict)->dict:
    en_riesgo = {}
    if est1["promedio"] < 3.4:
        en_riesgo[est1["codigo"]] = est1["promedio"]
    if est2["promedio"] < 3.4:
         en_riesgo[est2["codigo"]] = est2["promedio"]
    if est3["promedio"] < 3.4:
         en_riesgo[est3["codigo"]] = est3["promedio"]
    if est4["promedio"] < 3.4:
         en_riesgo[est4["codigo"]] = est4["promedio"]

    return en_riesgo
    
## programa principal

e_1 = {"nombre": "Fionha", "codigo": 1233456, "genero": "femenino", "promedio": 5.0, "ssc": 3}
e_2 = {"nombre": "Jose", "codigo": 12334987, "genero": "masculino", "promedio": 3.5, "ssc": 2}
e_3 = {"nombre": "nikolas", "codigo": 1202456, "genero": "masculino", "promedio": 2.9, "ssc": 3}
e_4 = {"nombre": "cristian", "codigo": 1233000, "genero": "masculino", "promedio": 3.3, "ssc": 4}

riesgo = quienes_en_riesgo(e_1, e_2, e_3, e_4,)
print(riesgo)
