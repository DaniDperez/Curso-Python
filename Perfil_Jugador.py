# Ernesto Daniel Piña Pérez

Nombre = input("Ingresa tu nombre: ")
Nacimiento = int(input("Ingresa tu año de nacimiento: "))
Videojuegos = input(f"Por favor {Nombre}, ingresa tus tres videojuegos favoritos separados por comas: ")

perfil = [Nombre]

Edad = 2025 - Nacimiento
perfil.append(Edad)  # append() Agrega un elemento al final de la lista

Lista_juegos = Videojuegos.split(",")  # split() Separa el texto en partes usando la coma
Lista_juegos = [j.strip() for j in Lista_juegos]  # strip() Quita espacios en blanco al inicio y final
perfil.extend(Lista_juegos)  # extend() Une otra lista a la lista actual

perfil.insert(0, True)  # Insert() Agrega un elemento en una posicion especifica

juego_favorito = perfil.pop(3)  # pop() Elimina un elemento según su posicion y lo devuelve

es_mayor_de_edad = int(perfil[2]) >= 18
nombre_largo = len(perfil[1]) > 10  # len() Cuenta cuantos caracteres o elementos hay
es_gamer_retro = "pacman" in [str(j).lower() for j in perfil]  # lower() Convierte el texto a minusculas

print("Perfil final:", perfil)
print("Juego favorito:", juego_favorito)
print("¿Mayor de edad?:", es_mayor_de_edad)
print("¿Nombre largo?:", nombre_largo)
print("¿Gamer retro?:", es_gamer_retro)
