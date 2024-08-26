from informacionPrestatario import InformacionDelPrestatario

class Prestamo:
    def __init__(self, fecha, informacion_prestatario):
        self.fecha = fecha
        self.informacion_prestatario = informacion_prestatario

    def crear(self):
        # Implementar lógica para crear un nuevo préstamo
        return self

    def destruir(self):
        # Implementar lógica para destruir un préstamo
        return True

    def encontrar(self, id):
        # Implementar lógica para encontrar un préstamo específico
        return self