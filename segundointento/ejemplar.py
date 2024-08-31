class Ejemplar:
    ejemplares = []

    def __init__(self, titulo, edicion):
        self.titulo = titulo
        self.edicion = edicion

    @classmethod
    def crear(cls, titulo, edicion):
        nuevo_ejemplar = cls(titulo, edicion)
        cls.ejemplares.append(nuevo_ejemplar)
        return nuevo_ejemplar

    @classmethod
    def listar(cls):
        return cls.ejemplares