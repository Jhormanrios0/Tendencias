from ejemplar import Ejemplar
from informacionPrestatario import InformacionPrestatario
from prestamo import Prestamo
from reserva import Reserva
from titulo import Titulo
from tituloLibro import TituloLibro
from tituloRevista import TituloRevista

def main():
    while True:
        print("1. Crear Título del Libro")
        print("2. Crear Título de Revista")
        print("3. Crear Ejemplar")
        print("4. Crear Préstamo")
        print("5. Crear Reserva")
        print("6. Crear Información del Prestatario")
        print("7. Encontrar Título")
        print("8. Destruir Título")
        print("9. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del título del libro: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            numero_reserva = int(input("Número de reserva: "))
            TituloLibro.crear(nombre, autor, isbn, numero_reserva)
            print(f"Título del libro '{nombre}' creado exitosamente.")

        elif opcion == '2':
            nombre = input("Nombre del título de la revista: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            numero_reserva = int(input("Número de reserva: "))
            TituloRevista.crear(nombre, autor, isbn, numero_reserva)
            print(f"Título de la revista '{nombre}' creado exitosamente.")

        elif opcion == '3':
            titulo = input("Título del ejemplar: ")
            edicion = input("Edición: ")
            Ejemplar.crear(titulo, edicion)
            print(f"Ejemplar del título '{titulo}' creado exitosamente.")

        elif opcion == '4':
            fecha = input("Fecha del préstamo: ")
            titulo = input("Título del préstamo: ")
            Prestamo.crear(fecha, titulo)
            print(f"Préstamo del título '{titulo}' creado exitosamente.")

        elif opcion == '5':
            fecha = input("Fecha de la reserva: ")
            titulo = input("Título de la reserva: ")
            Reserva.crear(fecha, titulo)
            print(f"Reserva del título '{titulo}' creada exitosamente.")

        elif opcion == '6':
            nombre = input("Nombre del prestatario: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            InformacionPrestatario.crear(nombre, direccion, telefono)
            print(f"Información del prestatario '{nombre}' creada exitosamente.")

        elif opcion == '7':
            nombre = input("Nombre del título a encontrar: ")
            titulo = Titulo.encontrar(nombre)
            if titulo:
                print(f"Título encontrado: {titulo.nombre}, Autor: {titulo.autor}, ISBN: {titulo.isbn}, Número de reserva: {titulo.numero_reserva}")
            else:
                print(f"Título '{nombre}' no encontrado.")

        elif opcion == '8':
            nombre = input("Nombre del título a destruir: ")
            if Titulo.destruir(nombre):
                print(f"Título '{nombre}' destruido exitosamente.")
            else:
                print(f"Título '{nombre}' no encontrado.")

        elif opcion == '9':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 9.")

if __name__ == "__main__":
    main()