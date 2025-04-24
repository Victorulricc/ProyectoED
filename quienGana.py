def QuienGana(resultado):
    # Resultado en formato "X-Y", donde X es el equipo local y Y el visitante
    goles_local, goles_visitante = map(int, resultado.split('-'))
    if goles_local == goles_visitante:
        return 0  # Empate
    elif goles_local > goles_visitante:
        return 1  # Gana el equipo local
    else:
        return -1  # Gana el equipo visitante