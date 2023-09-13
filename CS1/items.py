class item:
    # python debes crear un constructor diferente a los demas lenguajes.
    def __init__(self, nombre, precio, efecto, estadistica):
        self.nombre = nombre
        self.precio = precio
        self.efecto = efecto
        self.estadistica = estadistica

    # Método para mostrar información del item
    def mostrar_informacion(self):
        print(f"{self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Efecto: {self.efecto}")
        print(f"Estadística: {self.estadistica}")
