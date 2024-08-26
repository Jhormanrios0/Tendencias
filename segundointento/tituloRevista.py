from titulo import Titulo

class TituloDeRevista(Titulo):
    def __init__(self, nombre, autor, isbn, numero_de_reserva, tiempo_pendiente=10):
        super().__init__(nombre, autor, isbn, numero_de_reserva)
        self.tiempo_pendiente = tiempo_pendiente