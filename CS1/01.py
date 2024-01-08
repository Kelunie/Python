# Para mi pana, primero es lo clasico de ver en un tema de lenguaje de programación.

# Link de referencia https://fsymbols.com/es/teclado/windows/alt-codes/lista/

# El clasico poder imprimir en terminal o pantalla.
# Python es un  lenguaje que el ";" no es necesario pero se puede mantener
print("Soy una perra con Pudge")

# Tambien se puede usar las comillas simples.
print('Pero soy bueno con Muerta')

# ahora hay varios comandos que puedes usar para hacer salto de linea de esta forma nos ahorramos dos lineas de codigo en una
print("Este desgraciado no sabe rotar.")
print("Hace algo manco.")
print("Este desgraciado no sabe rotar. \nHace algo manco.")

# Repasemos los tipos de variables mas conocidos.
# String (texto)
# chart (un caracter)
# int (numero entero negativos o positivos sin decimales)
# double (numeros con decimales
# Booleano (esto solo pueden ser True o False)#

# hay algo interesante en python pero esto es importante en progra dependiendo del lenguaje.
# no se debe poner el tipo de variable antes del nombre de esta misma, ya que python tomara -
# el tipo de dato que se le asigne como el tipo de variable de esta.
# Esto quiere decir que son tipados mas info -> https://www.google.com/search?q=python+es+tipado%3F&oq=python+es+tipado%3F&aqs=chrome..69i57.2814j0j4&sourceid=chrome&ie=UTF-8#vhid=zDG2LlFPm3qxKM&vssid=l

# Las variables deben de seguir un nombre que vaya con el proyecto o la razon de la varaible
# si la varaible va a almacenar un nombre por profesionalidad tiene que ser algo relacionado al nombre
heroe1 = "Pudge"  # √
cosa = "Riki"  # X

heroe2 = "Zeus"
damage = 150
letra = 'ª'
Pi = 3.14
Muerto = True
enemigo = False

# Existen vectores que almacenan muchos datos
soportes = ["Jakiro", "Hoodwink", "Ogre Magic"]
atributos = ["Inteligencia", "Agilidad", "Fuerza"]

# vamos ahora a algo mas importante
# comandos simples de como funciona todo lenguaje

if heroe1 != "rikie":
    print("Ese heroe es Pudge.")

if heroe1 == "Pudge":
    print("Pudge hizo {0} de daño con la Q".format(damage))

if enemigo == True:
    print("El enemigo esta vivo")
else:
    print("El enemigo esta muerto")

# tenemos el for, que se usa para recorrer algo o contar
print()

for posicion in enumerate(soportes, 3):
    print(posicion)

print()

for x in soportes:
    print(x)

# o podemos deletrear cada letra y recorrerla del vector
print()
for soporte in enumerate(soportes, 3):
    print(soporte)
    for letra in soporte[1]:
        print(letra)
    print()

# se puede asignar el atributo al soporte con un for

# creamos un diccionario (los diccionaros relacion una cosa con otra que se le atribuye)
asignaciones = {}

for x in range(len(soportes)):
    asignaciones[soportes[x]] = atributos[x]

# Imprime las asignaciones
for soporte, atributo in asignaciones.items():
    print(f"{soporte}: {atributo}")

# asi se piden datos
print()
nickname = input("Ingrese su NickName\n")
print("Hola, " + nickname + "!")

# Ahora como todo input que se ingrese es un string, puede convertirlo despues o antes
# despues
edad = input("ingrese su edad \n")
edad = int(edad)
if isinstance(edad, int):
    print(True)

# python no tiene double, pero tiene float
# cuando se pide el dato
num = float(input("Ingrese un numero con decimales \n"))
if isinstance(num, float):
    print(True)

# Python no posee el do, pero se puede simular con while o for
salir = 1
while salir == 1:
    print("Bienvenido a una calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Division")
    print("4. Elevar")
    opcion = int(input("Ingrese una opción \n"))
    print()
    if opcion == 1:
        num1 = int(input("Ingrese el primero numero\n"))
        num2 = int(input("Ingrese el segundo numero\n"))
        resultado = num1 + num2
        print("Resultado: {0}".format(resultado))
    elif opcion == 2:
        num1 = int(input("Ingrese el primero numero\n"))
        num2 = int(input("Ingrese el segundo numero\n"))
        resultado = num1 - num2
        print("Resultado: {0}".format(resultado))
    elif opcion == 3:
        num1 = int(input("Ingrese el primero numero\n"))
        num2 = int(input("Ingrese el segundo numero\n"))
        resultado = num1 / num2
        print("Resultado: {0}".format(resultado))
    elif opcion == 4:
        num1 = int(input("Ingrese el primero numero\n"))
        num2 = int(input("Ingrese el segundo numero\n"))
        resultado = num1 ** num2
        print("Resultado: {0}".format(resultado))
    else:
        print("No ingrese un numero solicitado")
    salir = int(input("Desea realizar otra operacion?\n1. Sí\n2. No\n"))
