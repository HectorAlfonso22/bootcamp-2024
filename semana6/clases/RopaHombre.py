from .Prenda import Prenda

class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self._talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        info = super().mostrar_info()  # Llama al método de la clase padre
        print(f"{info}: {self._talla}")