import algoritmos.batalla_naval
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
    df = pd.DataFrame(datos, columns=["Cantidad de barcos", "Tiempo de ejecución (ms)"])
    df.to_excel(archivo_salida, index=False)

def generar_barcos(cantidad):

    rango_min, rango_max = 1, 10  
    barcos = [random.randint(rango_min, rango_max) for _ in range(cantidad)]
    return barcos

def main():
    cant = 15
    datos = []

    for i in range(1, cant,1):  
        barcos = generar_barcos(i)  
        n, m = 30, 30
        demanda_filas = [random.randint(1, 25) for _ in range(n)]  
        demanda_columnas = [random.randint(1, 25) for _ in range(m)]  
        tablero = [[0] * m for _ in range(n)]  
        
        cantidad_espacio_ocupado = 0
        demanda_total = sum(demanda_columnas) + sum(demanda_filas)
        demanda_de_barcos = sum(barcos) * 2
        numero_barco = 1
        demanda_cumplida = 0
        lista_tableros = []
        cant_barcos = len(barcos)
        barcos_restantes = barcos
        cant_pasados = 0

        inicio = time.time()
        mejor_tablero = algoritmos.batalla_naval.resolver(tablero, barcos, demanda_filas, demanda_columnas, cantidad_espacio_ocupado, demanda_total, demanda_de_barcos, numero_barco, lista_tableros, demanda_cumplida, cant_barcos, barcos_restantes, cant_pasados)
        fin = time.time()

        if mejor_tablero is not None:
            datos.append([i, (fin - inicio) * 1000])  
        else:
            print(f"No se encontró solución para el caso con {i} barcos.")

    archivo_salida = "resultados_batalla_naval.xlsx"
    crear_excel(datos, archivo_salida)
    print(f"Archivo {archivo_salida} creado exitosamente.")

    np.random.seed(12345)
    sns.set_theme()

    points = datos
    x = [point[0] for point in points] 
    y = [point[1] for point in points]  

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, y, "bo")
    ax.set_title("Tiempo de ejecución del algoritmo Batalla Naval")
    ax.set_xlabel("Número de barcos")
    ax.set_ylabel("Tiempo de ejecución (ms)")

    A = np.vstack([np.array(x)**2, np.array(x), np.ones(len(x))]).T  # Matriz con x^2, x y una columna de unos
    a, b, c = np.linalg.lstsq(A, y, rcond=None)[0]

    ax.plot(x, a * np.array(x)**2 + b * np.array(x) + c, 'r-', label=f'Ajuste: y = {a:.2e}x^2 + {b:.2e}x + {c:.2e}')
    ax.legend()

    plt.show()

    print(f"Coeficientes del ajuste cuadrático:")
    print(f"a: {a:.2e}")
    print(f"b: {b:.2e}")
    print(f"c: {c:.2e}")

if __name__ == "__main__":
    main()
