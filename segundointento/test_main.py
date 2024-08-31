import unittest
from ejemplar import Ejemplar
from informacionPrestatario import InformacionPrestatario
from prestamo import Prestamo
from reserva import Reserva
from titulo import Titulo
from tituloLibro import TituloLibro
from tituloRevista import TituloRevista

class TestBiblioteca(unittest.TestCase):

    def test_crear_titulo_libro(self):
        titulo = TituloLibro.crear("El Quijote", "Miguel de Cervantes", "123456789", 5)
        self.assertEqual(titulo.nombre, "El Quijote")
        self.assertEqual(titulo.autor, "Miguel de Cervantes")
        self.assertEqual(titulo.isbn, "123456789")
        self.assertEqual(titulo.numero_reserva, 5)

    def test_crear_titulo_revista(self):
        titulo = TituloRevista.crear("National Geographic", "Varios", "987654321", 10)
        self.assertEqual(titulo.nombre, "National Geographic")
        self.assertEqual(titulo.autor, "Varios")
        self.assertEqual(titulo.isbn, "987654321")
        self.assertEqual(titulo.numero_reserva, 10)

    def test_crear_ejemplar(self):
        ejemplar = Ejemplar.crear("El Quijote", "Primera Edición")
        self.assertEqual(ejemplar.titulo, "El Quijote")
        self.assertEqual(ejemplar.edicion, "Primera Edición")

    def test_crear_prestamo(self):
        prestamo = Prestamo.crear("2023-10-01", "El Quijote", "Juan Pérez")
        self.assertEqual(prestamo.fecha, "2023-10-01")
        self.assertEqual(prestamo.titulo, "El Quijote")
        self.assertEqual(prestamo.prestatario, "Juan Pérez")

    def test_crear_reserva(self):
        reserva = Reserva.crear("2023-10-01", "El Quijote")
        self.assertEqual(reserva.fecha, "2023-10-01")
        self.assertEqual(reserva.titulo, "El Quijote")

    def test_crear_informacion_prestatario(self):
        prestatario = InformacionPrestatario.crear("123", "Juan Pérez", "Calle Falsa 123", "555-1234")
        self.assertEqual(prestatario.codigo, "123")
        self.assertEqual(prestatario.nombre, "Juan Pérez")
        self.assertEqual(prestatario.direccion, "Calle Falsa 123")
        self.assertEqual(prestatario.telefono, "555-1234")

    def test_encontrar_titulo(self):
        TituloLibro.crear("El Quijote", "Miguel de Cervantes", "123456789", 5)
        titulo = Titulo.encontrar("El Quijote")
        self.assertIsNotNone(titulo)
        self.assertEqual(titulo.nombre, "El Quijote")

    def test_destruir_titulo(self):
        TituloLibro.crear("El Quijote", "Miguel de Cervantes", "123456789", 5)
        resultado = Titulo.destruir("El Quijote")
        self.assertTrue(resultado)
        titulo = Titulo.encontrar("El Quijote")
        self.assertIsNone(titulo)

if __name__ == '__main__':
    unittest.main()