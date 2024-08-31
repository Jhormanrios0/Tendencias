class Reserva:
    reservas = []

    def __init__(self, fecha, titulo):
        self.fecha = fecha
        self.titulo = titulo  # Relación con Título

    @classmethod
    def crear(cls, fecha, titulo):
        nueva_reserva = cls(fecha, titulo)
        cls.reservas.append(nueva_reserva)
        return nueva_reserva

    @classmethod
    def destruir(cls, reserva):
        if reserva in cls.reservas:
            cls.reservas.remove(reserva)
            return True
        return False

    @classmethod
    def encontrar(cls, titulo):
        return [reserva for reserva in cls.reservas if reserva.titulo == titulo]

    @classmethod
    def listar(cls):
        return cls.reservas