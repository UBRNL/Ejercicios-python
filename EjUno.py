def calcular_tiempo_descarga(velocidad: int, tamanio_archivo: int)->int:
    gb_megas = tamanio_archivo * 1000
    v = velocidad * 8
    tiempo = gb_megas / v
    return round(tiempo)
