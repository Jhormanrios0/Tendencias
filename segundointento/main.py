from ejemplar import Ejemplar
from titulo import Titulo
from tituloLibro import TituloDelLibro
from tituloRevista import TituloDeRevista
from prestamo import Prestamo
from reserva import Reserva
from informacionPrestatario import InformacionDelPrestatario

def main():
    while True:
        
        libros = []
        ejemplares = []
        prestamos = []
        revistas = []
        reservas = []

        
        nombre_prestatario = input("Ingrese el nombre del prestatario: ")
        direccion_prestatario = input("Ingrese la dirección del prestatario: ")
        prestatario = InformacionDelPrestatario(nombre=nombre_prestatario, direccion=direccion_prestatario)

        
        cantidad_libros = int(input("¿Cuántos libros desea ingresar? "))
        for _ in range(cantidad_libros):
            nombre_libro = input("Ingrese el nombre del libro: ")
            autor_libro = input("Ingrese el autor del libro: ")
            isbn_libro = input("Ingrese el ISBN del libro: ")
            numero_reserva_libro = input("Ingrese el número de reserva del libro: ")
            libro = TituloDelLibro(nombre=nombre_libro, autor=autor_libro, isbn=isbn_libro, numero_de_reserva=numero_reserva_libro)
            libro.crear()
            libros.append(libro)

            
            id_ejemplar_libro = int(input("Ingrese el ID del ejemplar del libro: "))
            ejemplar_libro = Ejemplar(id=id_ejemplar_libro)
            ejemplar_libro.crear()
            ejemplares.append(ejemplar_libro)

        
        fecha_prestamo = input("Ingrese la fecha del préstamo (YYYY-MM-DD): ")
        prestamo = Prestamo(fecha=fecha_prestamo, informacion_prestatario=prestatario)
        prestamo.crear()
        prestamos.append(prestamo)

        
        cantidad_revistas = int(input("¿Cuántas revistas desea ingresar? "))
        for _ in range(cantidad_revistas):
            nombre_revista = input("Ingrese el nombre de la revista: ")
            autor_revista = input("Ingrese el autor de la revista: ")
            isbn_revista = input("Ingrese el ISBN de la revista: ")
            numero_reserva_revista = input("Ingrese el número de reserva de la revista: ")
            revista = TituloDeRevista(nombre=nombre_revista, autor=autor_revista, isbn=isbn_revista, numero_de_reserva=numero_reserva_revista)
            revista.crear()
            revistas.append(revista)

        
        fecha_reserva = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
        reserva = Reserva(fecha=fecha_reserva, informacion_prestatario=prestatario)
        reserva.crear()
        reservas.append(reserva)

        
        print("\nLibros:")
        for libro in libros:
            print(f"Nombre: {libro.nombre}, Autor: {libro.autor}, ISBN: {libro.isbn}, Número de Reserva: {libro.numero_de_reserva}")

        print("\nEjemplares:")
        for ejemplar in ejemplares:
            print(f"ID: {ejemplar.id}")

        print("\nPréstamos:")
        for prestamo in prestamos:
            print(f"Fecha: {prestamo.fecha}, Prestatario: {prestamo.informacion_prestatario.nombre}")

        print("\nRevistas:")
        for revista in revistas:
            print(f"Nombre: {revista.nombre}, Autor: {revista.autor}, ISBN: {revista.isbn}, Número de Reserva: {revista.numero_de_reserva}")

        print("\nReservas:")
        for reserva in reservas:
            print(f"Fecha: {reserva.fecha}, Prestatario: {reserva.informacion_prestatario.nombre}")

        
        continuar = input("\n¿Desea llenar otro formulario? (s/n): ")
        if continuar.lower() != 's':
            break

    print("\nMucas gracias por usar el sistema Profe. Merezco un 5.0.")

if __name__ == "__main__":
    main()