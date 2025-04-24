import csv

def LeerPartidos():
    partidos = []
    with open('liga.csv', mode='r', encoding='utf-8') as fichero:
        lector = csv.DictReader(fichero)
        for fila in lector:
            partidos.append(fila)
    print(partidos)
    return partidos


