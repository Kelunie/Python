import random


def mansion() -> (list, list):
    house = [list(["⬜️"] * 4) for _ in range(4)]

    if random.choice([True, False]):
        # columnas perimetro
        puerta = [random.randint(0, 3), random.choice([0, 3])]
    else:
        # filas perimetro
        puerta = [random.choice([0, 3]), random.randint(0, 3)]

    house[puerta[0]][puerta[1]] = "🚪"

    def confite(puerta: list) -> list:
        conf = [random.randint(0, 3), random.randint(0, 3)]
        if conf[0] == puerta[0] or conf[1] == puerta[1]:
            return confite(puerta)
        return conf

    conf = confite(puerta)

    house[conf[0]][conf[1]] = "🍭"

    for fila in house:
        print("".join(map(str, fila)))

    return house, puerta


def pintar_mansion(house, position):
    for i in range(len(house)):
        for j in range(len(house[i])):
            if [i, j] == position:
                if house[i][j] == "🚪":
                    print("🚪", end=" ")
                else:
                    print("🤐", end=" ")
            else:
                print(house[i][j], end=" ")
        print()


def mover(position: list) -> list:

    fila, columna = position[0], position[1]

    movimientos = "N S E O"

    if fila == 0:
        movimientos = movimientos.replace("N ", "")
    if fila == 3:
        movimientos = movimientos.replace("S ", "")
    if columna == 0:
        movimientos = movimientos.replace("O ", "")
    if columna == 3:
        movimientos = movimientos.replace("E ", "")

    moverme = input("¿Donde quieres ir [ {movimientos} ]? \n".format(
        movimientos=movimientos))

    if moverme.upper() in movimientos:

        if moverme == "N":
            position = [fila - 1, columna]
        elif moverme == "S":
            position = [fila + 1, columna]
        elif moverme == "E":
            position = [fila, columna + 1]
        elif moverme == "O":
            position = [fila, columna - 1]
        return position
    else:
        print("No es una opción válida")
        return moverme(position)


def acertijos():
    preguntas = [
        ("¿Qué tipo de juego es Dota 2?",
         "Dota 2 es un videojuego de estrategia en tiempo real (MOBA) que se juega en línea."),
        ("¿Cuál es el objetivo principal en Dota 2?",
         "El objetivo principal en Dota 2 es destruir el Ancient enemigo, una estructura ubicada en la base enemiga."),
        ("¿Cuántos jugadores hay en un equipo en Dota 2?",
         "Cada equipo en Dota 2 tiene 5 jugadores, para un total de 10 jugadores en la partida."),
        ("¿Cuál es el rol más importante en Dota 2?",
         "No hay un rol más importante en Dota 2; todos los roles son esenciales para el éxito del equipo."),
        ("¿Cuál es el héroe más emblemático de Dota 2?",
         "El héroe más emblemático de Dota 2 es Pudge, conocido por su gancho y habilidades de control de masas."),
        ("¿Qué es el MMR en Dota 2?", "El MMR (Matchmaking Rating) es un sistema de calificación que determina la habilidad de un jugador y lo empareja con otros jugadores de habilidad similar."),
        ("¿Qué es el Aegis of the Immortal?",
         "El Aegis of the Immortal es un objeto que otorga una resurrección una vez al portador si muere en combate."),
        ("¿Cuál es el mapa principal de Dota 2?",
         "El mapa principal de Dota 2 se llama 'El Bosque Susurrante' (The Radiant/Dire Ancient) y cuenta con tres carriles y una jungla."),
        ("¿Qué significa 'Creep Equilibrium' en Dota 2?",
         "El 'Creep Equilibrium' se refiere al equilibrio de creeps en los carriles, donde los creeps enemigos se mantienen en una posición neutral sin avanzar."),
        ("¿Qué es el 'Last Hitting' en Dota 2?",
         "'Last Hitting' es la práctica de asestar el último golpe a un creep para obtener oro y experiencia."),
        ("¿Cuál es el torneo más grande de Dota 2?",
         "El torneo más grande de Dota 2 es The International, organizado por Valve, que tiene un premio millonario."),
        ("¿Qué son los 'Blink Dagger'?",
         "Los 'Blink Dagger' son objetos que permiten a los héroes teleportarse a una ubicación deseada en un instante."),
        ("¿Cuál es el héroe con más habilidades en Dota 2?",
         "Invoker es el héroe con más habilidades en Dota 2, con un total de 14 hechizos."),
        ("¿Cuál es la importancia de las runas en Dota 2?",
         "Las runas proporcionan ventajas temporales a los héroes y son fundamentales para el control del mapa."),
        ("¿Qué es el 'Roshan' en Dota 2?",
         "Roshan es un poderoso jefe neutro que otorga el Aegis of the Immortal al equipo que lo derrota."),
        ("¿Qué significa 'Stacking' y 'Pulling' en Dota 2?",
         "'Stacking' se refiere a agrupar creeps en un campamento de la jungla para aumentar la cantidad de creeps, mientras que 'Pulling' implica atraer creeps del carril hacia la jungla para cambiar el equilibrio del lane."),
        ("¿Cuál es la función del soporte en Dota 2?",
         "Los soportes en Dota 2 tienen la función de cuidar y asistir a sus compañeros de equipo, comprando objetos y proporcionando visión en el mapa."),
        ("¿Cuál es el tiempo de recarga del 'Courier' en Dota 2?",
         "El tiempo de recarga del 'Courier' en Dota 2 es de 3 minutos."),
        ("¿Cuál es el héroe más jugado en Dota 2?",
         "El héroe más jugado en Dota 2 puede variar con el tiempo, pero algunos populares incluyen a Sniper, Pudge y Juggernaut."),
        ("¿Qué es el 'Muting' en Dota 2?",
         "El 'Muting' es la capacidad de silenciar a otros jugadores en el juego para evitar mensajes o comunicación no deseada.")
    ]

    current_pregunta = preguntas[random.randint(0, len(preguntas) - 1)]
    while True:
        respuesta = input(f"{current_pregunta[0]}:  \n")

        if respuesta.lower() == current_pregunta[1].lower():
            print("Respuesta correcta! \n")
            return
        else:
            print("Respuesta incorrecta! \n")


house, puerta = mansion()

position = puerta
print(f"Posición Inicial: {position}\n")

print("""
👻 Bienvenido Heroe!
Si quieres encontrar el aegis 🍭 de la casa encantada 🏰
tendrás que buscarlos a través de sus habitaciones.
Pero recuerda, no podrás moverte si antes no respondes
correctamente a su enigma.
""")


while True:
    pintar_mansion(house, position)
    position = mover(position)
    print(f"Posición: {position}\n")

    house_room = house[position[0]][position[1]]

    if house_room == "⬜️":

        print("Responde correctamente a esta pregunta.")
        acertijos()

        ghost = random.randint(1, 10) == 1
        if ghost:
            print(
                "👻 BoooOOOoOoo! Para salir de esta habitación deberás responder otra pregunta más.")
            acertijos()

    elif house_room == "🍭":
        print("""
            👻 BoooOOOoOoo!
            Has encontrado Aegis 🍭 y escapado de la casa encantada 🏰
            Feliz Halloween! 🎃
                """)
        break
