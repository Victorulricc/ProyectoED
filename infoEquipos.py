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