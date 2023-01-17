def mejor_del_salon(est1:dict, est2:dict, est3:dict, est4:dict, est5:dict)->dict:
    el_mejor = {}
    if est1["promedio"] > 3.4 :
        el_mejor[est1] = est1["promedio"]
    if est2["promedio"] > 3.4 :
         el_mejor[est2] = est2["promedio"]
    if est3["promedio"] > 3.4 :
         el_mejor[est3] = est3["promedio"]
    if est4["promedio"] > 3.4 :
         el_mejor[est4] = est4["promedio"]
    if est5["promedio"] > 3.4 :
         el_mejor[est4] = est5["promedio"]

    return el_mejor
    
## programa principal

e_1 = {"nombre": "Fionha", "matematica": 4.2, "Español": 3.9, "Ciencias": 4.1, "Literatura": 3.9, "Artes": 4.5, "promedio": 4.1}
e_2 = {"nombre": "Jose", "matematica": 3.2, "Español": 3.5, "Ciencias": 4.0, "Literatura": 4.9, "Artes": 3.5, "promedio": 3.8}
e_3 = {"nombre": "nikolas", "matematica": 4.5, "Español": 4.9, "Ciencias": 4.2, "Literatura": 2.9, "Artes": 3.5, "promedio": 4.0}
e_4 = {"nombre": "cristian", "matematica": 3.6, "Español": 3.5, "Ciencias": 4.4, "Literatura": 3.9, "Artes": 3.0, "promedio": 3.6}
e_5 = {"nombre": "cristian", "matematica": 4.0, "Español": 2.9, "Ciencias": 4.9, "Literatura": 4.1, "Artes": 4.0, "promedio": 3.9}

alumno = mejor_del_salon(e_1, e_2, e_3, e_4, e_5)
print(alumno)
