import random
import string

# Parámetros del algoritmo genético
tamaño_poblacion = 100
tasa_mutacion = 0.05
num_generaciones = 1000
objetivo = "HELLO WORLD"
elitismo = True

# Funciones del algoritmo genético
def cadena_aleatoria():
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(len(objetivo)))

def calcular_aptitud(cadena):
    return sum(1 for c1, c2 in zip(cadena, objetivo) if c1 == c2)

def seleccionar_padre(poblacion, aptitudes):
    total_aptitud = sum(aptitudes)
    seleccion = random.uniform(0, total_aptitud)
    suma = 0
    for individuo, aptitud in zip(poblacion, aptitudes):
        suma += aptitud
        if suma >= seleccion:
            return individuo
    return poblacion[-1]

def cruzar(padre1, padre2):
    punto = random.randint(0, len(padre1) - 1)
    return padre1[:punto] + padre2[punto:]

def mutar(cadena):
    if random.random() < tasa_mutacion:
        posicion = random.randint(0, len(cadena) - 1)
        caracter = random.choice(string.ascii_uppercase + ' ')
        return cadena[:posicion] + caracter + cadena[posicion+1:]
    return cadena

# Algoritmo genético
poblacion = [cadena_aleatoria() for _ in range(tamaño_poblacion)]
for generacion in range(num_generaciones):
    aptitudes = [calcular_aptitud(individuo) for individuo in poblacion]
    
    # Verificar si ya se encontró la solución
    if max(aptitudes) == len(objetivo):
        print(f"Generación {generacion} - Mejor aptitud: {max(aptitudes)} - Cadena: {poblacion[aptitudes.index(max(aptitudes))]}")
        print(f"Solución encontrada en la generación {generacion}!")
        break
    
    print(f"Generación {generacion} - Mejor aptitud: {max(aptitudes)} - Cadena: {poblacion[aptitudes.index(max(aptitudes))]}")
    
    # Aplicar Elitismo si está habilitado
    if elitismo:
        elite = [poblacion[aptitudes.index(max(aptitudes))]]
    else:
        elite = []
    
    # Seleccionar padres para la próxima generación
    nuevos_padres = [seleccionar_padre(poblacion, aptitudes) for _ in range(tamaño_poblacion - len(elite))]
    
    # Asegurarse de que hay un número par de padres para cruzar
    if len(nuevos_padres) % 2 != 0:
        nuevos_padres.append(random.choice(nuevos_padres))
    
    # Aplicar operadores de cruza y mutación
    poblacion = elite + [mutar(cruzar(nuevos_padres[i], nuevos_padres[i+1])) for i in range(0, len(nuevos_padres), 2)]
else:
    print("No se encontró la solución en el número de generaciones definido.")