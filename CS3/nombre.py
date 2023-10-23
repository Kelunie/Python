# Define tu nombre
nombre = "Joshua"

# Crea una matriz vacía con suficiente espacio para tu nombre
matriz = [[' ' for _ in range(25)] for _ in range(5)]

# Define las letras de tu nombre en la matriz
letras = {
    'J': ['   J   ',
          '   J   ',
          '   J   ',
          '   J   ',
          'JJJ    '],
    'o': ['  OOO  ',
          ' O   O ',
          ' O   O ',
          ' O   O ',
          '  OOO  '],
    's': ['  SSS  ',
          ' S    S',
          '  SSS  ',
          '     S ',
          '  SSS  '],
    'h': ['H   H  ',
          'H   H  ',
          'HHHHH  ',
          'H   H  ',
          'H   H  '],
    'u': ['U   U  ',
          'U   U  ',
          'U   U  ',
          'U   U  ',
          ' UUU   '],
    'a': ['  A   ',
          ' A A  ',
          'AAAAA ',
          'A   A ',
          'A   A ']
}

# Llena la matriz con tu nombre
col = 0
for letra in nombre:
    if letra in letras:
        for fila, fila_letra in enumerate(letras[letra]):
            matriz[fila] = list(matriz[fila])
            matriz[fila][col:col+len(fila_letra)] = fila_letra
            matriz[fila] = ''.join(matriz[fila])
        col += len(fila_letra) + 1  # Deja espacio entre las letras

# Imprime la matriz con tu nombre
for fila in matriz:
    print(fila)
