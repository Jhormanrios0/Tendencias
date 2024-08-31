from titulo import Titulo
class TituloRevista(Titulo):
    tiempo_pendiente = 10  # Días de préstamo predeterminados

    def __init__(self, nombre, autor, isbn, numero_reserva):
        super().__init__(nombre, autor, isbn, numero_reserva)