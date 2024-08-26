from titulo import Titulo

class TituloDelLibro(Titulo):
    def __init__(self, nombre, autor, isbn, numero_de_reserva, tiempo_pendiente=30):
        super().__init__(nombre, autor, isbn, numero_de_reserva)
        self.tiempo_pendiente = tiempo_pendiente