import csv

def LeerPartidos():
    partidos = []
    with open('liga.csv', mode='r', encoding='utf-8') as fichero:
        lector = csv.DictReader(fichero)
        for fila in lector:
            partidos.append(fila)
    print(partidos)
    return partidos

def Equipos(datosliga):
    equipos = set()
    for partido in datosliga:
        equipos.add(partido['Team 1'])
        equipos.add(partido['Team 2'])
    return equipos

def QuienGana(resultado):
    # Resultado en formato "X-Y", donde X es el equipo local y Y el visitante
    goles_local, goles_visitante = map(int, resultado.split('-'))
    if goles_local == goles_visitante:
        return 0  # Empate
    elif goles_local > goles_visitante:
        return 1  # Gana el equipo local
    else:
        return -1  # Gana el equipo visitante

def InfoEquipos(datosliga, equipos):
    # Crear un diccionario para llevar el control de los partidos de cada equipo
    estadisticas = {equipo: [0, 0, 0, 0] for equipo in equipos}  # [ganados, empatados, perdidos, puntos]
    
    for partido in datosliga:
        resultado = partido['FT']
        equipo_local = partido['Team 1']
        equipo_visitante = partido['Team 2']
        
        # Determinar quién ganó el partido
        resultado_partido = QuienGana(resultado)
        
        if resultado_partido == 1:  # Gana el equipo local
            estadisticas[equipo_local][0] += 1  # Gana el equipo local
            estadisticas[equipo_visitante][2] += 1  # Pierde el visitante
        elif resultado_partido == -1:  # Gana el equipo visitante
            estadisticas[equipo_local][2] += 1  # Pierde el equipo local
            estadisticas[equipo_visitante][0] += 1  # Gana el visitante
        else:  # Empate
            estadisticas[equipo_local][1] += 1  # Empate para el equipo local
            estadisticas[equipo_visitante][1] += 1  # Empate para el visitante
    
    # Convertir los resultados en tuplas y calcular los puntos
    info = []
    for equipo, stats in estadisticas.items():
        ganados, empatados, perdidos, _ = stats
        puntos = Puntos([ganados, empatados, perdidos])
        info.append((equipo, ganados, empatados, perdidos, puntos))
    
    return info

def Puntos(info):
    ganados, empatados, perdidos = info
    return ganados * 3 + empatados  # 3 puntos por victoria y 1 punto por empate

def Clasificacion(datos):
    # Ordenar por puntos (índice 4 de cada tupla)
    datos_ordenados = sorted(datos, key=lambda x: x[4], reverse=True)
    
    print("Clasificación:")
    print(f"{'Pos':<4} {'Equipo':<20} {'Ganados':<8} {'Empatados':<10} {'Perdidos':<8} {'Puntos'}")
    print("-" * 50)
    
    for i, (equipo, ganados, empatados, perdidos, puntos) in enumerate(datos_ordenados, 1):
        print(f"{i:<4} {equipo:<20} {ganados:<8} {empatados:<10} {perdidos:<8} {puntos}")

def impClasificacion(liga):
    equipos = Equipos(liga)  # Obtener los equipos
    info = InfoEquipos(liga, equipos)  # Obtener la información de los equipos
    Clasificacion(info)  # Imprimir la clasificación ordenada

liga = LeerPartidos()  # Obtener los datos de los partidos
impClasificacion(liga)  # Imprimir la clasificación