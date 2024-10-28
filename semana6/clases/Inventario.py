from .Prenda import Prenda

class Inventario:
    def __init__(self,):
        self.prendas = []  # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda a la lista

    def mostrar_inventario(self):
        
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información de cada prenda
