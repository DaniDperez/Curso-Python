#Ernesto Daniel Piña Pérez

# Funcion para contar palabras en un texto
def contar_palabras(texto):
    # Convertir a minusculas
    texto = texto.lower()
    # Quitar signos de puntuacion
    signos = ",.;:!?¿¡()\"'"
    for s in signos:
        texto = texto.replace(s, "")
    # Separar palabras
    palabras = texto.split()
    # Crear diccionario
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

# Leer el texto desde archivo
with open("texto.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

# Contar palabras
resultado = contar_palabras(contenido)

# Guardar el conteo en un nuevo archivo
with open("conteo_palabras.txt", "w", encoding="utf-8") as f:
    for palabra, cantidad in resultado.items():
        f.write(f"{palabra}: {cantidad}\n")

print("Conteo completado y guardado en conteo_palabras.txt")
