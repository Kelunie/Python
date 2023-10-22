from Heroe import hero

# creamos un metodo para ver la informacion de la clase


def verHero(lstHeroe):
    i = 1
    for her in lstHeroe:
        print('El hero {0} se llama {1} el nombre, su abtributo es {2} de sus habilidades son: {3}, {4}, {5}, {6} '.format
              (i, her.getNombre(), her.getAtributo(), her.getSpell1(), her.getSpell2(), her.getSpell3(), her.getSpell4()))
        i += 1
    print('')


# creamos la instancia de la clase
her1 = hero()

# Colocamos los valores con set
her1.setNombre('Arc Warden')
her1.setAtributo('Agilidad')
her1.setSpell1('Flujo')
her1.setSpell2('Campo Magnetico')
her1.setSpell3('Espectro Centellante')
her1.setSpell4('Duplicado de la Tempestad')


print('El Heroe se llama {0}'.format(her1.getNombre()))
print('Su atributo es {0}'.format(her1.getAtributo()))
print('Sus habilidades son:')
print(her1.getSpell1())
print(her1.getSpell2())
print(her1.getSpell3())
print(her1.getSpell4())


# Practica #1 Crea una clase con un constructor HeroesV2 con sus get y sett y agregue una lista de heroes y utilice
# el contructor dado def verHero(lstHero):'
