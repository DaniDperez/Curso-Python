#Ernesto Daniel Piña Pérez

# Clase Componente
class Componente:
    #El constructor recibe los datos
    def __init__(self, numero_serie, tipo_componente, costo):
        print(f"Creando componente {tipo_componente} con S/N {numero_serie}...")

        #Guardamos los datos dentro del objeto
        self.numero_serie = numero_serie
        self.tipo = tipo_componente
        self.costo = costo

        #Atributos por defecto
        self.historial_revisiones = []
        self.esta_activo = True

#Creacion de objetos
c1 = Componente("MTR-1001", "Motor", 550.75)
c2 = Componente("SNR-2050", "Sensor", 80.20)

#Modificando datos
c1.historial_revisiones.append("2025-10-25")
c1.historial_revisiones.append("2025-10-28")
c2.esta_activo = False

#Reporte
print("\n Reporte de Componentes")
print(f"S/N: {c1.numero_serie} | Tipo: {c1.tipo} | Costo: {c1.costo} | Revisiones: {c1.historial_revisiones} | Activo: {c1.esta_activo}")
print(f"S/N: {c2.numero_serie} | Tipo: {c2.tipo} | Costo: {c2.costo} | Revisiones: {c2.historial_revisiones} | Activo: {c2.esta_activo}")

