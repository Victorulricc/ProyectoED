def Equipos(datosliga):
    equipos = set()
    for partido in datosliga:
        equipos.add(partido['Team 1'])
        equipos.add(partido['Team 2'])
    return equipos