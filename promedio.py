def el_mejor_de_todos(est1:dict, est2:dict, est3:dict, est4:dict, est5:dict)->dict:
    return The_best
if est1["promedio"] > est2["promedio"]:
    print(promedio)
elif est2["promedio"] > est3["promedio"]:
    print(promedio)
elif est4["promedio"] > est5["promedio"]:
    print(promedio)

## programa principal
Matematica = M
Español = E
Ciencia = C
literatuta = L
Arte = A
promedio = (M+E+C+L+A)/5


e_1 = {"nombre": "Fionha", "Matematica": 4.2, "Español": 3.9, "Ciencias": 4.1, "Literatura": 3.9, "Artes": 4.5, "promedio": 4.1}
e_2 = {"nombre": "Jose", "Matematica": 3.2, "Español": 3.5, "Ciencias": 4.0, "Literatura": 4.9, "Artes": 3.5, "promedio": 3.8}
e_3 = {"nombre": "nikolas", "Matematica": 4.5, "Español": 4.9, "Ciencias": 4.2, "Literatura": 2.9, "Artes": 3.5, "promedio": 4.0}
e_4 = {"nombre": "cristian", "Matematica": 3.6, "Español": 3.5, "Ciencias": 4.4, "Literatura": 3.9, "Artes": 3.0, "promedio": 3.6}
e_5 = {"nombre": "cristian", "Matematica": 4.0, "Español": 2.9, "Ciencias": 4.9, "Literatura": 4.1, "Artes": 4.0, "promedio": 3.9}

alumno = mejor_del_salon(e_1, e_2, e_3, e_4, e_5)
print(alumno)  
