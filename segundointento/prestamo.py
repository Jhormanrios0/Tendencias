class Prestamo:
    prestamos = []

    def __init__(self, fecha, titulo, prestatario):
        self.fecha = fecha
        self.titulo = titulo
        self.prestatario = prestatario

    @classmethod
    def crear(cls, fecha, titulo, prestatario):
        nuevo_prestamo = cls(fecha, titulo, prestatario)
        cls.prestamos.append(nuevo_prestamo)
        return nuevo_prestamo

    @classmethod
    def listar(cls):
        return cls.prestamos