from functools import reduce
import time

# Decorador sencillo
def auditar_funcion(func):
    def envoltura(*args, **kwargs):
        print("\nEjecutando:", func.__name__)
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print("Duración:", round(fin - inicio, 5), "segundos")
        return resultado
    return envoltura

# Generador de datos
def leer_temperaturas():
    datos = [
        ("CDMX", 26),
        ("Monterrey", 34),
        ("Toluca", 19),
        ("Cancún", 38),
        ("Guadalajara", 31),
        ("Puebla", 28),
        ("Mérida", 40)
    ]
    for ciudad in datos:
        yield ciudad

@auditar_funcion
def procesar_datos():
    # Convertir el generador en lista   
    temperaturas = list(leer_temperaturas())

    # Filtrar temperaturas altas (>=30)
    altas = list(filter(lambda x: x[1] >= 30, temperaturas))

    # Ordenar de mayor a menor temperatura
    ordenadas = sorted(altas, key=lambda x: x[1], reverse=True)

    # Transformar en mensajes de alerta
    alertas = list(map(lambda x: f"Alerta de calor en {x[0]}: {x[1]}°C", ordenadas))

    # Calcular promedio de temperaturas
    if len(ordenadas) > 0:
        promedio = reduce(lambda acc, x: acc + x[1], ordenadas, 0) / len(ordenadas)
    else:
        promedio = 0

    # Mostrar resultados
    print("\nAlertas ordenadas:")
    for alerta in alertas:
        print(alerta)

    print(f"\nTemperatura promedio de alertas: {promedio:.1f}°C")

# Programa principal
if __name__ == "__main__":
    procesar_datos()
