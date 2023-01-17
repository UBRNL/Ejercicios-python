d = {}
d["Juan"] = "3135832749"
d["Julian"] = "3135832750"
d["Jose"] = "3135832745"
d["Juana"] = "3135832755"
for cada_llave in d.keys(): ## Para recorrer las iiaves del diccionario
    print(cada_llave)
for cada_valor in d.values(): ## Para recorrer cada valor de la llaves, en el diccionario
    print(cada_valor)
for cada_valor in d: ## Para ver tanto llaves y valor a la vez
    print(cada_valor,":",d[cada_valor])
