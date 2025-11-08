#Ernesto Daniel Piña Pérez

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
frase_favorita = input("Ingresa tu frase favorita: ")
dinero = float(input("Ingresa la cantidad de dinero disponible: "))

print(f"\nHola amigo {nombre}, tienes {edad} años, tu frase favorita es \"{frase_favorita}\" y actualmente cuentas con una cantidad de ${dinero:.2f} disponibles")
