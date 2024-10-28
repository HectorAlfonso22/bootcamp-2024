class Categoria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_productos(self):
        print(f"\nCategoría: {self._nombre}")
        for producto in self._productos:
            print(producto.mostrar_info())

    def get_productos(self):
        return self._productos