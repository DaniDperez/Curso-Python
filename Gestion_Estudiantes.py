#Ernesto Daniel Piña Pérez

from os import system
import math
from random import randint, choice

# Tupla con materias validas
materias_validas = (
    "Resistencia de los materiales",
    "Control clasico",
    "Programacion avanzada",
    "Algebra lineal",
    "Electronica de potencia",
    "Sistemas embebidos",
)

# Diccionario principal
estudiantes = {}

def pedir_opcion():
    while True:
        print("\nMenu: registrar | buscar | promedio | ver_todos | cursos_unicos | salir")
        op = input("Elige una opcion: ").strip().lower()
        if op in {"registrar", "buscar", "promedio", "ver_todos", "cursos_unicos", "salir"}:
            return op
        print("Opcion invalida. Intenta de nuevo")

def pedir_id():
    while True:
        dato = input("Ingresa el ID del alumno (ej. '103'): ").strip()
        if dato:
            return dato
        print("ID vacio. Intenta de nuevo.")

def pedir_nombre():
    while True:
        nom = input("Ingresa el nombre del alumno: ").strip()
        if nom:
            return nom
        print("Nombre vacio. Intenta de nuevo")

def normalizar(texto: str) -> str:
    return texto.strip().lower()

def pedir_materia():
    print("Materias validas:")
    for m in materias_validas:
        print(" -", m)
    validas_norm = {normalizar(m): m for m in materias_validas}
    while True:
        mat = input("Elige una materia: ").strip()
        m_norm = normalizar(mat)
        if m_norm in validas_norm:
            return validas_norm[m_norm]
        print("Materia invalida. Intenta de nuevo")

def pedir_calificaciones(n=3):
    califs = []
    i = 1
    while len(califs) < n:
        dato = input(f"Calificacion {i}/{n}: ").strip()
        try:
            val = float(dato)
            califs.append(val)
            i += 1
        except ValueError:
            print("Entrada no numerica. Intenta de nuevo")
    return califs

def accion_registrar():
    print("\n Registrar alumno ")
    alumno_id = pedir_id()
    if alumno_id in estudiantes:
        print("Error: el ID ya existe")
        return
    nombre = pedir_nombre()
    materia = pedir_materia()
    calificaciones = pedir_calificaciones(3)
    estudiantes[alumno_id] = {
        "nombre": nombre,
        "materia": materia,
        "calificaciones": calificaciones,
    }
    print("Alumno registrado correctamente")

def accion_buscar():
    print("\n Buscar alumno ")
    alumno_id = pedir_id()
    alumno = estudiantes.get(alumno_id)
    if alumno is None:
        print("No se encontro el alumno")
        return
    print(f"Nombre: {alumno['nombre']}")
    print(f"Materia: {alumno['materia']}")
    print(f"Calificaciones: {alumno['calificaciones']}")

def accion_promedio():
    print("\n Promedio de un alumno ")
    alumno_id = pedir_id()
    alumno = estudiantes.get(alumno_id)
    if alumno is None:
        print("No se encontro el alumno")
        return
    califs = alumno.get("calificaciones", [])
    if not califs:
        print("No hay calificaciones registradas")
        return
    prom = sum(califs) / len(califs)
    print(f"Promedio: {prom:.2f}")

def accion_ver_todos():
    print("\n Lista de todos los alumnos ")
    if not estudiantes:
        print("No hay alumnos registrados")
        return
    for aid, datos in estudiantes.items():
        print(f"ID: {aid} | Nombre: {datos.get('nombre', 'N/D')}")

def accion_cursos_unicos():
    print("\n Cursos unicos registrados ")
    cursos = {datos.get("materia") for datos in estudiantes.values() if datos.get("materia")}
    if not cursos:
        print("No hay cursos registrados aun")
        return
    for c in sorted(cursos):
        print(" -", c)

if __name__ == "__main__":
    print("Sistema de gestion de estudiantes")
    while True:
        opcion = pedir_opcion()
        if opcion == "registrar":
            accion_registrar()
        elif opcion == "buscar":
            accion_buscar()
        elif opcion == "promedio":
            accion_promedio()
        elif opcion == "ver_todos":
            accion_ver_todos()
        elif opcion == "cursos_unicos":
            accion_cursos_unicos()
        elif opcion == "salir":
            print("Gracias por usar el sistema")
            break
