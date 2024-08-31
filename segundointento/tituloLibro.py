from titulo import Titulo
class TituloLibro(Titulo):
    tiempo_pendiente = 30  # Días de préstamo predeterminados

    def __init__(self, nombre, autor, isbn, numero_reserva):
        super().__init__(nombre, autor, isbn, numero_reserva)