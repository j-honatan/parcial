import random  # Importamos el módulo 'random' para generar números aleatorios.
import math    # Importamos el módulo 'math' para realizar cálculos matemáticos.
from tabulate import tabulate  # Importamos la función 'tabulate' para crear una tabla con colores.

# Datos de las conferencias, incluyendo nombre, duración, horario preferido y asientos disponibles.
conferencias = [
   {"nombre": "Conferencia 1", "duracion": 1.5, "horarioPreferido": "Mañana", "asientosDisponibles": 50},
    {"nombre": "Conferencia 2", "duracion": 2, "horarioPreferido": "Tarde", "asientosDisponibles": 30},
    {"nombre": "Conferencia 3", "duracion": 2, "horarioPreferido": "Tarde", "asientosDisponibles": 30},
]

salas = ["Sala 1", "Sala 2", "Sala 3"]  # Lista de salas disponibles.
horarios = ["Mañana", "Tarde", "Noche"]   # Lista de horarios disponibles.

# Función para calcular la asistencia total en una programación dada.
def calcular_asistencia_total(programacion):
    asistencia_total = 0
    for conferencia in programacion:
        asistencia_total += conferencia["conferencia"]["asientosDisponibles"]
    return asistencia_total

# Función para generar una programación aleatoria de conferencias en salas y horarios.
def generar_programacion_aleatoria(conferencias, salas, horarios):
    programacion = []
    for conferencia in conferencias:
        sala = random.choice(salas)     # Se elige una sala aleatoriamente.
        horario = random.choice(horarios)  # Se elige un horario aleatoriamente.
        programacion.append({"conferencia": conferencia, "sala": sala, "horario": horario})
    return programacion

# Función que implementa el algoritmo de recocido simulado para optimizar la programación.
def recocido_simulado(conferencias, salas, horarios, temperatura_inicial, enfriamiento):
    programacion_actual = generar_programacion_aleatoria(conferencias, salas, horarios)
    asistencia_actual = calcular_asistencia_total(programacion_actual)

    mejor_programacion = list(programacion_actual)
    mejor_asistencia = asistencia_actual

    temperatura = temperatura_inicial

    while temperatura > 1:
        i, j = random.sample(range(len(conferencias)), 2)
        programacion_actual[i]["horario"], programacion_actual[j]["horario"] = programacion_actual[j]["horario"], programacion_actual[i]["horario"]

        nueva_asistencia = calcular_asistencia_total(programacion_actual)

        diferencia = nueva_asistencia - asistencia_actual

        if diferencia > 0 or random.random() < math.exp(diferencia / temperatura):
            asistencia_actual = nueva_asistencia
            if asistencia_actual > mejor_asistencia:
                mejor_programacion = list(programacion_actual)
                mejor_asistencia = asistencia_actual
        else:
            programacion_actual[i]["horario"], programacion_actual[j]["horario"] = programacion_actual[j]["horario"], programacion_actual[i]["horario"]

        temperatura *= enfriamiento

    return mejor_programacion

# Ejemplo de uso
temperatura_inicial = 1000
enfriamiento = 0.98

programacion_optima = recocido_simulado(conferencias, salas, horarios, temperatura_inicial, enfriamiento)

encabezados = ["Conferencia", "Duración (h)", "Horario Pref.", "Asientos Disp.", "Sala Asignada", "Horario Asignado"]

tabla_conferencias = []
for conferencia in programacion_optima:
    conf_datos = conferencia['conferencia']
    fila = [
        conf_datos['nombre'],
        str(conf_datos['duracion']),
        conf_datos['horarioPreferido'],
        str(conf_datos['asientosDisponibles']),
        conferencia['sala'],
        conferencia['horario']
    ]
    tabla_conferencias.append(fila)

# Imprimir la tabla usando tabulate con colores
tabla_coloreada = tabulate(tabla_conferencias, headers=encabezados, tablefmt="fancy_grid")
print(tabla_coloreada)
print("Asistencia total óptima:", calcular_asistencia_total(programacion_optima))
