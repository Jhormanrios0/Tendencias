class InformacionPrestatario:
    prestatarios = []

    def __init__(self, codigo, nombre, direccion, telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    @classmethod
    def crear(cls, codigo, nombre, direccion, telefono):
        nuevo_prestatario = cls(codigo, nombre, direccion, telefono)
        cls.prestatarios.append(nuevo_prestatario)
        return nuevo_prestatario

    @classmethod
    def listar(cls):
        return cls.prestatarios