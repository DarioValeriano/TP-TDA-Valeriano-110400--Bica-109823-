from algoritmos.juego_de_hermanos_greedy import juegos_de_hermanos
from collections import deque
import time
import pandas as pd
import random

# Imports necesarios para el notebook
from random import seed
from util import time_algorithm
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp


def crear_excel(datos, archivo_salida):
    """
    Crea un archivo Excel con los datos de a pares.

    :param datos: Lista de tuplas con los datos a guardar (por ejemplo, [(clave, valor), ...]).
    :param archivo_salida: Nombre del archivo Excel donde se guardarán los datos.
    """
    df = pd.DataFrame(datos, columns=["Monedas", "Tiempo"])
    df.to_excel(archivo_salida, index=False)

def generar_monedas(cantidad):
    """
    Genera una lista de 'cantidad' de monedas con valores aleatorios 
    entre 'rango_min' y 'rango_max'.

    :param cantidad: Número de monedas a generar.
    :param rango_min: Valor mínimo para las monedas.
    :param rango_max: Valor máximo para las monedas.
    :return: Lista de monedas con valores aleatorios.
    """
    rango_min, rango_max = 1, 1000
    monedas = [random.randint(rango_min, rango_max) for _ in range(cantidad)]
    monedas = deque(monedas)
    return monedas

def main():
    cant = 1002
    datos = []
    
    # Generamos los datos para la simulación
    for i in range(2, cant, 2):
        monedas = generar_monedas(i)
        inicio = time.time()
        juegos_de_hermanos(monedas)
        fin = time.time()
        datos.append([i, (fin - inicio) * 1000])  # Guardamos el tiempo en milisegundos

    archivo_salida = "datos_greedy.xlsx"
    crear_excel(datos, archivo_salida)
    print(f"Archivo {archivo_salida} creado exitosamente.")
    
    # Establecemos la semilla para resultados reproducibles
    seed(12345)
    np.random.seed(12345)
    sns.set_theme()

    # Extraemos los puntos de datos
    points = datos
    x = [point[0] for point in points]  # Tamaño del array
    y = [point[1] for point in points]  # Tiempo de ejecución

    # Graficamos los puntos experimentales
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, y, "bo")
    ax.set_title("Tiempo de ejecución de juegos de hermanos (Greedy)")
    ax.set_xlabel("Tamaño del arreglo de monedas")
    ax.set_ylabel("Tiempo de ejecución (ms)")

    # Método de ajuste por cuadrados mínimos para la recta y = mx + c
    # Preparamos la matriz A para la ecuación lineal
    A = np.vstack([x, np.ones(len(x))]).T  # Matriz con x y una columna de unos para el término c
    
    # Calculamos los coeficientes m (pendiente) y c (intersección)
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]

    # Graficamos la recta ajustada
    ax.plot(x, m * np.array(x) + c, 'r-', label=f'Ajuste: y = {m:.2e}x + {c:.2e}')
    ax.legend()

    # Mostrar gráfico
    plt.show()

    # Imprimir los valores de m y c
    print(f"Pendiente (m): {m:.2e}")
    print(f"Intersección (c): {c:.2e}")

main()
