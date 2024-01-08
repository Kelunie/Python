# creamos el vector donde estara almacenado las preguntas y el examen
preguntas = []
examen = []
nombre = ""

# Creamos el menu


def menu():
    print("Bienvenido Sistema de creación de examen")
    print("1. Crear examen")
    print("2. Agregar pregunta")
    print("3. Realizar examen")
    print("4. Modificar Preguntas")
    print("5. Eliminar Preguntas")
    print("6. Salir")
    opcion = input("Ingrese una opcion: \n")
    return opcion


# creamos el metodo para agregar preguntas


def agregarPregunta():
    pregunta = input("Ingrese la pregunta que quiere agregar:\n ")
    opciones = input(
        "Ingrese las opciones que se van a agregar (separadas por comas):\n ").split(',')
    respuesta = input("Ingrese la respuesta correcta:\n ")
    preg = {
        "pregunta": pregunta,
        "opciones": opciones,
        "respuesta": respuesta
    }
    preguntas.append(preg)

# metodo para modificar pregunta


# Método para modificar una pregunta
def modificarPregunta():
    if len(preguntas) == 0:
        print("No hay preguntas para modificar")
    else:
        print("Lista de preguntas:")
        for i, pregunta in enumerate(preguntas):
            print(f"{i + 1}. {pregunta['pregunta']}")

        try:
            num_pregunta = int(
                input("Ingrese el número de la pregunta que desea modificar: ")) - 1

            if 0 <= num_pregunta < len(preguntas):
                nueva_pregunta = input("Ingrese la nueva pregunta:\n ")
                nuevas_opciones = input(
                    "Ingrese las nuevas opciones (separadas por comas):\n ").split(',')
                nueva_respuesta = input(
                    "Ingrese la nueva respuesta correcta:\n ")

                # Modificar la pregunta en la lista
                preguntas[num_pregunta]['pregunta'] = nueva_pregunta
                preguntas[num_pregunta]['opciones'] = nuevas_opciones
                preguntas[num_pregunta]['respuesta'] = nueva_respuesta

                print("Pregunta modificada con éxito.")
            else:
                print("Número de pregunta no válido.")
        except ValueError:
            print("Entrada no válida. Ingrese un número válido.")


# metodo para eliminar pregunta


def eliminarPregunta():
    if len(preguntas) == 0:
        print("No hay preguntas para eliminar")
    else:
        print("Preguntas disponibles para eliminar: ")
        for i, pregunta in enumerate(preguntas):
            print(f"{i + 1}. {pregunta['pregunta']}")
        num_pregunta = int(
            input("Ingrese el número de la pregunta que quiere eliminar: \n")) - 1

        if 0 <= num_pregunta <= len(preguntas):
            # eliminar la pregunta en la lista
            pregunta_eliminada = preguntas.pop(num_pregunta)
            print(
                f"Pregunta '{pregunta_eliminada['pregunta']}' eliminada con éxito.")
        else:
            print("Numero de pregunta no valido 😭")
# Creamos el metodo para crear el examen


def crearExamen():
    if len(preguntas) == 0:
        print("No hay preguntas para crear el examen")
    else:
        nombre = input("Ingrese el nombre del examen: \n")
        print("Examen creado con éxito ✅")
        print("Examen: " + nombre)
        print("Preguntas disponibles para agregar al examen: ")

        # Mostrar preguntas disponibles
        for i, pregunta in enumerate(preguntas):
            print(f"{i + 1}. {pregunta['pregunta']}")

        while True:
            # Permitir al usuario seleccionar una pregunta para agregar al examen
            seleccion = input(
                "Seleccione una pregunta (Ingrese el número) o presione Enter para finalizar:\n ")

            if not seleccion:
                break  # Salir del bucle si el usuario presiona Enter sin seleccionar una pregunta

            try:
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(preguntas):
                    examen.append(preguntas[seleccion - 1])
                    print("Pregunta agregada al examen.")
                else:
                    print("Número de pregunta no válido. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Ingrese un número válido.")

        # Imprimir las preguntas en el examen
        print(f"\nPreguntas en el examen '{nombre}':")
        for i, pregunta in enumerate(examen):
            print(f"{i + 1}. {pregunta['pregunta']}")


def RealizarExamen(examen, nombre):
    if len(examen) == 0:
        print("No se ha creado ningún examen")
    else:
        print("Examen: " + nombre)
        preguntas_totales = len(examen)
        puntaje = 0  # Contador de respuestas correctas
        preguntas_acertadas = []
        preguntas_erroneas = []

        # Iterar a través de cada pregunta en el examen
        for i, pregunta in enumerate(examen):
            print(f"\nPregunta {i + 1}: {pregunta['pregunta']}")

            # Mostrar opciones
            for j, opcion in enumerate(pregunta['opciones']):
                print(f"{j + 1}. {opcion}")

            # Solicitar la respuesta del usuario
            respuesta_usuario = input(
                "Ingrese la opción correcta: ")

            # Verificar la respuesta del usuario
            respuesta_correcta = pregunta['respuesta']
            if respuesta_usuario == respuesta_correcta:
                print("¡Respuesta correcta! ⭕")
                puntaje += 1
                preguntas_acertadas.append(pregunta)
            else:
                print(
                    f"Respuesta incorrecta ✖️. La respuesta correcta es {respuesta_correcta}")
                preguntas_erroneas.append({
                    "pregunta": pregunta['pregunta'],
                    "respuesta_correcta": respuesta_correcta
                })

        # Calcular y mostrar el puntaje final
        puntaje_final = (puntaje * 100) / preguntas_totales
        print("\nExamen completado.")
        print(f"Preguntas correctas: {puntaje}")
        print(f"Preguntas totales: {preguntas_totales}")
        print(f"Puntaje final: {puntaje_final:.2f}%")

        # Mostrar preguntas acertadas
        print("\nPreguntas acertadas:")
        for pregunta_acertada in preguntas_acertadas:
            print(f"- {pregunta_acertada['pregunta']}")

        # Mostrar preguntas erróneas y respuestas correctas
        print("\nPreguntas erróneas y respuestas correctas:")
        for pregunta_erronea in preguntas_erroneas:
            print(f"- {pregunta_erronea['pregunta']}")
            print(
                f"  Respuesta correcta: {pregunta_erronea['respuesta_correcta']}")


while True:
    opcion = menu()
    if opcion == "1":
        print("Creando examen...")
        crearExamen()
        print()
    elif opcion == "2":
        print("Agregando pregunta...")
        agregarPregunta()
        print()
    elif opcion == "3":
        RealizarExamen(examen, nombre)
        examen = []  # Limpiar el examen
        print()
    elif opcion == "4":
        print("Modificando pregunta...")
        modificarPregunta()
        print()
    elif opcion == "5":
        print("Eliminando pregunta...")
        eliminarPregunta()
        print()
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion no valida")
