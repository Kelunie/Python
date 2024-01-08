soportes = ["Jakiro", "Hoodwink", "Ogre Magic",
            "cristal maiden", "tiny", "rubick"]
atributos = ["Inteligencia", "Agilidad", "Fuerza"]

asignaciones = {}


for x in range(len(soportes)):
    if soportes[x] == "cristal maiden":
        asignaciones[soportes[x]] = atributos[0]
    elif soportes[x] == "rubick":
        asignaciones[soportes[x]] = atributos[0]
    elif soportes[x] == "Jakiro":
        asignaciones[soportes[x]] = atributos[0]
    elif soportes[x] == "Ogre Magic":
        asignaciones[soportes[x]] = atributos[2]
    elif soportes[x] == "tiny":
        asignaciones[soportes[x]] = atributos[2]
    elif soportes[x] == "Hoodwink":
        asignaciones[soportes[x]] = atributos[1]

# Imprime las asignaciones
for clave, asignacion_a_la_clave in asignaciones.items():
    print(f"{clave}: {asignacion_a_la_clave}")

print(asignaciones)
