from .Prenda import Prenda

class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self._talla}")