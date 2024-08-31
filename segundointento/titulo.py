class Titulo:
    titulos = []

    def __init__(self, nombre, autor, isbn, numero_reserva):
        self.nombre = nombre
        self.autor = autor
        self.isbn = isbn
        self.numero_reserva = numero_reserva

    @classmethod
    def crear(cls, nombre, autor, isbn, numero_reserva):
        nuevo_titulo = cls(nombre, autor, isbn, numero_reserva)
        cls.titulos.append(nuevo_titulo)
        return nuevo_titulo

    @classmethod
    def destruir(cls, nombre):
        titulo = cls.encontrar(nombre)
        if titulo:
            cls.titulos.remove(titulo)
            return True
        return False

    @classmethod
    def encontrar(cls, nombre):
        for titulo in cls.titulos:
            if titulo.nombre == nombre:
                return titulo
        return None

    @classmethod
    def listar(cls):
        return cls.titulos