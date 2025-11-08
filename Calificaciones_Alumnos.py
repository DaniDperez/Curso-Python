#Ernesto Daniel Piña Pérez

cantidad_alumnos = int(input("Cuantos alumnos desea registrar? "))

nombres = []
calificaciones = []

for i in range(cantidad_alumnos):  # bucle for para registrar los alumnos
    print(f"\nAlumno: {i+1}")
    nombre = input("Nombre: ")
    calificacion = float(input("Calificacion (0-10): "))
    nombres.append(nombre)
    calificaciones.append(calificacion)

aprobados = []
reprobados = []
excelentes = []

suma_total = 0.0
for calificacion in calificaciones:  # bucle for para sumar las calificaciones
    suma_total += calificacion

promedio_general = suma_total / cantidad_alumnos

for i in range(cantidad_alumnos):  # bucle for para clasificar alumnos
    if calificaciones[i] <= 5:  # condicion para reprobados
        reprobados.append(nombres[i])
    elif calificaciones[i] >= 6 and calificaciones[i] < 10:  # condicion para aprobados
        aprobados.append(nombres[i])
    elif calificaciones[i] == 10:  # condicion para excelentes
        excelentes.append(nombres[i])

print("\nReporte final")
print(f"Numero total de estudiantes: {cantidad_alumnos}")
print(f"Promedio general del grupo: {promedio_general:.2f}")
print(f"Calificacion mas baja: {min(calificaciones)}")
print(f"Calificacion mas alta: {max(calificaciones)}")

print("\nListas de Clasificacion")
print(f"Excelente(s): {excelentes}")
print(f"Aprobado(s): {aprobados}")
print(f"Reprobado(s): {reprobados}")


