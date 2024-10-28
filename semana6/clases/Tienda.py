from .Categoria import Categoria

class Tienda:
    def __init__(self):
        self._categorias = []

    def agregar_categoria(self, categoria):
        self._categorias.append(categoria)

    def mostrar_categorias(self):
        for categoria in self._categorias:
            categoria.mostrar_productos()

    def get_productos(self):
        productos = []
        for categoria in self._categorias:
            productos.extend(categoria.get_productos())
        return productos