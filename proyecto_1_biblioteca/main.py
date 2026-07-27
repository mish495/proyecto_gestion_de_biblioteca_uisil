# ======================================================
# IMPORTACIONES
# ======================================================

from proyecto_1_biblioteca.base_datos.crear_tablas import crear_tablas
from proyecto_1_biblioteca.modulos.modulo_libros import menu_libros
from proyecto_1_biblioteca.modulos.modulo_usuarios import menu_usuarios
from proyecto_1_biblioteca.modulos.modulo_prestamos import menu_prestamos


# ======================================================
# FUNCIÓN PRINCIPAL
# ======================================================

def main():

    # Crear tablas de la base de datos
    crear_tablas()

    while True:

        print("\n========== SISTEMA DE BIBLIOTECA ==========")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Préstamos")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            menu_libros()

        elif opcion == "2":
            menu_usuarios()

        elif opcion == "3":
            menu_prestamos()

        elif opcion == "4":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


# ======================================================
# PUNTO DE ENTRADA
# ======================================================

if __name__ == "__main__":
    main()