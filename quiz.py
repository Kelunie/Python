contador_externo = 0
mensaje = 0
while contador_externo < 3000:
    contador_externo += 1
    contador_interno = 0
    while contador_interno < 5000:
        contador_interno += 1
        mensaje += 1

print(mensaje)
