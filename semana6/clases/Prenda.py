class Prenda:
    def __init__(self,nombre,precio,cantidad):
        self._nombre = nombre  # Atributo público
        self._precio = precio  # Atributo público
        self._cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Precio: ${self._precio}, Stock: {self._cantidad}")

    def get_precio(self):
        return self._precio