class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_carrito(self):
        print("\nCarrito de Compras:")
        for producto in self._productos:
            print(producto.mostrar_info())
        print(f"Total a pagar: ${self.calcular_total():.2f}")

    def calcular_total(self):
        return sum(producto.get_precio() for producto in self._productos)