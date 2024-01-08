import csv


def calcular_puntaje(goles_equipo, goles_rival, tarjetas_equipo, tarjetas_rival):
    if goles_equipo > goles_rival:
        return 3
    elif goles_equipo < goles_rival:
        return 1
    else:  # Empate en goles
        if tarjetas_equipo < tarjetas_rival:
            return 3
        elif tarjetas_equipo > tarjetas_rival:
            return 1
        else:  # Empate en goles y tarjetas
            return 0


# Crea un diccionario para almacenar los datos de los equipos
equipos = {}

# Abre el archivo CSV y lee los datos
with open(r'C:\Users\Julio\OneDrive\Escritorio\utn\Python\Copa_Mundial_2023.csv', newline='') as copa_mundo:
    reader = csv.DictReader(copa_mundo)
    for row in reader:
        equipo_local = row['equipoCasa']
        equipo_visitante = row['equipoVisita']
        goles_local = int(row['golesCasa'])
        goles_visitante = int(row['golesVisita'])
        tarjetas_local = int(row['targetasCasa'])
        tarjetas_visitante = int(row['tarjetasVisita'])

        # Actualiza las estadísticas para el equipo local
        if equipo_local not in equipos:
            equipos[equipo_local] = {'goles': 0, 'puntaje': 0, 'tarjetas': 0}
        equipos[equipo_local]['goles'] += goles_local
        equipos[equipo_local]['puntaje'] += calcular_puntaje(
            goles_local, goles_visitante, tarjetas_local, tarjetas_visitante)
        equipos[equipo_local]['tarjetas'] += tarjetas_local

        # Actualiza las estadísticas para el equipo visitante
        if equipo_visitante not in equipos:
            equipos[equipo_visitante] = {
                'goles': 0, 'puntaje': 0, 'tarjetas': 0}
        equipos[equipo_visitante]['goles'] += goles_visitante
        equipos[equipo_visitante]['puntaje'] += calcular_puntaje(
            goles_visitante, goles_local, tarjetas_visitante, tarjetas_local)
        equipos[equipo_visitante]['tarjetas'] += tarjetas_visitante

# Imprime las estadísticas de los equipos
for equipo, estadisticas in equipos.items():
    print(f'{equipo}:')
    print(f'Total de goles: {estadisticas["goles"]}')
    print(f'Total de puntaje: {estadisticas["puntaje"]}')
    print(f'Total de tarjetas: {estadisticas["tarjetas"]}')
    print()
