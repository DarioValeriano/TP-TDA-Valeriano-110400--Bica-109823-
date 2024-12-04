import algoritmos.juego_de_hermanos_dinamica
import time
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def crear_excel(datos, archivo_salida):
    """
    Crea un archivo Excel con los datos de a pares.

    :param datos: Lista de tuplas con los datos a guardar (por ejemplo, [(clave, valor), ...]).
    :param archivo_salida: Nombre del archivo Excel donde se guardarán los datos.
    """
    df = pd.DataFrame(datos, columns=["Clave", "Valor"])
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
    return monedas

def main():
    cant = 1002
    datos = []

    # Generamos los datos para la simulación
    for i in range(2, cant, 2):
        monedas = generar_monedas(i)
        inicio = time.time()
        algoritmos.juego_de_hermanos_dinamica.juegos_de_hermanos(monedas)
        fin = time.time()
        datos.append([i, (fin - inicio) * 1000])  # Guardamos el tiempo en milisegundos

    archivo_salida = "datos_dinamica.xlsx"
    crear_excel(datos, archivo_salida)
    print(f"Archivo {archivo_salida} creado exitosamente.")

    # Establecemos la semilla para resultados reproducibles
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
    ax.set_title("Tiempo de ejecución de juegos de hermanos (Dinamica)")
    ax.set_xlabel("Tamaño del arreglo de monedas")
    ax.set_ylabel("Tiempo de ejecución (ms)")

    # Método de ajuste por cuadrados mínimos para una función cuadrática y = ax^2 + bx + c
    # Preparamos la matriz A para la ecuación cuadrática
    A = np.vstack([np.array(x)**2, np.array(x), np.ones(len(x))]).T  # Matriz con x^2, x y una columna de unos

    # Calculamos los coeficientes a, b y c
    a, b, c = np.linalg.lstsq(A, y, rcond=None)[0]

    # Graficamos la curva ajustada
    ax.plot(x, a * np.array(x)**2 + b * np.array(x) + c, 'r-', label=f'Ajuste: y = {a:.2e}x^2 + {b:.2e}x + {c:.2e}')
    ax.legend()

    # Mostrar gráfico
    plt.show()

    # Imprimir los valores de a, b y c
    print(f"Coeficientes del ajuste cuadrático:")
    print(f"a: {a:.2e}")
    print(f"b: {b:.2e}")
    print(f"c: {c:.2e}")

main()
