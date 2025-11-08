# Ernesto Daniel Piña Perez

lista_compras = ["leche", "pan", "manzanas"]
print("Lista inicial de compras:", lista_compras)
print("\nOpciones disponibles:")
print("1. Agregar un articulo (escribe: agregar)")
print("2. Quitar un articulo (escribe: quitar)")
print("3. Revisar lista (escribe: revisar)")

accion = input("\nQue deseas hacer?: ").lower()

# if se usa para evaluar una condicion principal
if accion == "agregar":
    nuevo_articulo = input("Que articulo deseas agregar?: ")
    if nuevo_articulo in lista_compras:
        print("El articulo ya esta en la lista")
    else:
        lista_compras.append(nuevo_articulo)
        print("Articulo agregado correctamente")
    print("Lista actualizada:", lista_compras)

# elif se usa para evaluar una segunda condicion si la primera no se cumple
elif accion == "quitar":
    articulo_quitar = input("Que articulo deseas quitar?: ")
    if articulo_quitar in lista_compras:
        lista_compras.remove(articulo_quitar)
        print("Articulo eliminado correctamente.")
    else:
        print("No se encontro el articulo en la lista")
    print("Lista actualizada:", lista_compras)

# otro elif para una tercera opcion
elif accion == "revisar":
    print("\nLista actual de compras:")
    if len(lista_compras) > 0:
        for articulo in lista_compras:
            print("-", articulo)
    else:
        print("La lista esta vacia.")
    print("Lista actualizada:", lista_compras)

# else se usa cuando ninguna de las condiciones anteriores se cumple
else:
    print("Opcion no reconocida. Escribe: agregar, quitar o revisar")

print("\nPrograma finalizado")
