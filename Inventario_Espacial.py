#Ernesto Daniel Piña Pérez

inventario = ["panel solar", "modulo de oxigeno", "comida deshidratada", "traje espacial"]
print(f"El inventario actual es: {inventario}")

while True:  # bucle principal del programa
    print("\nMenu de opciones")
    print("1. añadir")
    print("2. quitar")
    print("3. ver")
    print("4. inspeccionar")
    print("5. salir")

    opcion = input("\nEscribe una opcion: ").lower()

    try:  # manejo de errores principal
        if opcion == "añadir":  # opcion para agregar item
            nuevo_item = input("Escribe el articulo que deseas añadir: ").strip()
            if nuevo_item == "":
                print("Error: No puedes agregar un nombre vacio")
            else:
                inventario.append(nuevo_item)
                print(f"Articulo '{nuevo_item}' agregado correctamente")
            print(f"Inventario actual: {inventario}")

        elif opcion == "quitar":  # opcion para eliminar item
            quitar_item = input("Escribe el articulo que deseas quitar: ").strip()
            if quitar_item in inventario:  # if para comprobar existencia
                inventario.remove(quitar_item)
                print(f"Articulo '{quitar_item}' eliminado correctamente.")
            else:
                print("Error: Ese item no existe en el inventario.")
            print(f"Inventario actual: {inventario}")

        elif opcion == "ver":  # opcion para mostrar lista
            if len(inventario) == 0:  # if para verificar lista vacia
                print("El inventario esta vacio")
            else:
                print("\nInventario actual")
                for i, item in enumerate(inventario, start=1):  # bucle for para mostrar items
                    print(f"{i}. {item}")

        elif opcion == "inspeccionar":  # opcion para inspeccionar item
            if len(inventario) == 0:
                print("Inventario vacio, no hay nada que inspeccionar.")
            else:
                try:  # try anidado para manejar error de indice
                    indice = int(input("Que numero de item quieres inspeccionar?: "))
                    if indice < 1 or indice > len(inventario):
                        print(f"Error: numero fuera de rango (1 - {len(inventario)}).")
                    else:
                        print(f"Has inspeccionado el item: '{inventario[indice - 1]}'")
                except ValueError:
                    print("Error: Debes ingresar un numero valido.")
            print(f"Inventario actual: {inventario}")

        elif opcion == "salir":  # opcion para terminar programa
            print("Saliendo del sistema de inventario espacial...")
            break  # rompe el bucle principal

        else:  # opcion invalida
            print("Error: opcion no valida. Intenta de nuevo")

    except Exception as e:  # captura de error inesperado
        print(f"Error inesperado: {e}")

print("Programa terminado correctamente")
