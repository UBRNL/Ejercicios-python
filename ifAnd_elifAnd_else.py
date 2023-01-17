x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
    print(x)
    
def funcion(palabra: str, frase:str)->bool:
    return palabra in frase

frase = "alberto come ensalada, y juana prefiere el dulce"
p1 = "berto come ensa"
p2 = "juan prefiere el dulce"

print(funcion(p1, frase))
print(funcion(p2.upper(), frase.upper()))
print(funcion(p2.lower(), frase))


banco = {"nombre": "techo", "localidad": "kennedy",
         "donates": 0, "AB+": 360,"AB-":130}

llave1 = "localidad"
llave2 = "kennedy"
valor1 = banco.get(llave1, "ninguno")
valor2 = banco.get(llave2, "ninguno")

print("1)", valor1)
print("2)", valor2)

banco["nombre"] = "Banderas"
print("3)", valor1)

temporal1 = 0

if banco["AB+"] < 120:
    temporal1 = 300
elif banco["AB-"] < 350:
    temporal1 = 210
print("4:", temporal1)


banco = {"nombre": "shaio", "localidad": "suba",
         "donates": 1023, "sangre_O+": 100,"sangre_O-":200}
temporal1 = 0
if banco ["sangre_O+"] > 120:
    temporal1 = 3
elif banco ["sangre_O-"] > 50:
    temporal1 = 7

print("1)", temporal1)

if banco ["localidad"].lower() == "shaio":
    temporal1 = 5
if banco ["sangre_O+"] <= 700:
    temporal1 = 15
if banco["localidad"] != "suba":
    temporal1 = 20

print("2)", temporal1)


banco = {"nombre": "bachue", "localidad": "engativa",
         "donates": 367, "sangre_A+": 856, "sangre_A-":348}

banco ["localidad"] = "banderas"
temporal1 = 0
if banco ["localidad"].lower() == "engativa":
    temporal1 = 5
elif banco ["sangre_A+"] > 700:
    temporal1 = 15
elif banco ["localidad"] != "suba":
    temporal1 = 30
else:
    temporal = 20
print("1)", temporal1)
llave1 = "sangre_A+"
llave2 = "sangre_A-"
valor1 = banco.get("llave1", "ninguna")
valor2 = banco.get("llave2", "ninguno")
print("2)", valor1)
print("3)", valor2)

def cantidad_persona_a_ingresar(peso_promedio:float, cantidad_en_fila:int)->int:
    cantidad = 0
    if peso_promedio < 70:
        cantidad += 50
    elif cantidad_en_fila > 600:
        cantidad -=40
    elif cantidad_en_fila <= 600 and peso_promedio >= 70:
        cantidad += 25
    else:
        cantidad = 900
    pass
def ayuda_estudiantes(estudiante_pregunta:bool, nota_examen: float, nota_proyecto:float)->None:
    if estudiante_pregunta == True:
        respondele_a_estudiante()
    elif nota_examen < 3:
        preguntale_temas_debil()
        if nota_proyecto < 3:
            levatar_alerta()
    if nota_proyecto < 2.5:
        preguntale_que_paso_en_proyecto()
    else:
         responde_por_slack()
    animar_estuiante()
   

ayuda_estudiantes(False, 2.0, 2.7)
print(ayuda_estudiantes)



























































































