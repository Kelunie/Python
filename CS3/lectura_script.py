import csv
from tabulate import tabulate

archivo_csv = 'Copa_Mundial_2023.csv'  # Reemplaza con la ruta de tu archivo CSV

# Crea una lista vacía para almacenar los datos del archivo CSV
datos_csv = []

# Abre el archivo CSV y lee los datos
with open(archivo_csv, 'r') as archivo:
    lector_csv = csv.reader(archivo, delimiter=',')
    next(lector_csv)
    for fila in lector_csv:
        datos_csv.append(fila)

# Crear diccionarios para almacenar puntuaciones, goles y tarjetas de cada equipo
puntuaciones = {}
goles_por_pais = {}
tarjetas_por_pais = {}

# Procesar los partidos y calcular puntuaciones, goles y tarjetas
for partido in datos_csv:
    equipo_local = partido[0]
    equipo_visitante = partido[1]
    goles_local = int(partido[2])
    goles_visitante = int(partido[3])
    tarjetas_local = int(partido[4])
    tarjetas_visitante = int(partido[5])

    # Calcular las puntuaciones según las reglas de puntuación
    if goles_local > goles_visitante:
        puntuaciones[equipo_local] = puntuaciones.get(
            equipo_local, 0) + 3  # Equipo local gana
    elif goles_local < goles_visitante:
        puntuaciones[equipo_visitante] = puntuaciones.get(
            equipo_visitante, 0) + 3  # Equipo visitante gana
    else:
        puntuaciones[equipo_local] = puntuaciones.get(
            equipo_local, 0) + 1  # Empate
        puntuaciones[equipo_visitante] = puntuaciones.get(
            equipo_visitante, 0) + 1  # Empate

    # Calcular goles y tarjetas para el equipo local
    goles_por_pais[equipo_local] = goles_por_pais.get(
        equipo_local, 0) + goles_local
    tarjetas_por_pais[equipo_local] = tarjetas_por_pais.get(
        equipo_local, 0) + tarjetas_local

    # Calcular goles y tarjetas para el equipo visitante
    goles_por_pais[equipo_visitante] = goles_por_pais.get(
        equipo_visitante, 0) + goles_visitante
    tarjetas_por_pais[equipo_visitante] = tarjetas_por_pais.get(
        equipo_visitante, 0) + tarjetas_visitante

# Crear una nueva lista con los encabezados y los datos de goles y tarjetas
nueva_lista = [['País', 'Puntos', 'Goles', 'Tarjetas']]
for pais in puntuaciones.keys():
    puntos = puntuaciones.get(pais, 0)
    goles = goles_por_pais.get(pais, 0)
    tarjetas = tarjetas_por_pais.get(pais, 0)
    nueva_lista.append([pais, puntos, goles, tarjetas])

# Imprimir la nueva lista con los encabezados
tabla = tabulate(nueva_lista, headers="firstrow", tablefmt="fancy_grid")
print(tabla)
