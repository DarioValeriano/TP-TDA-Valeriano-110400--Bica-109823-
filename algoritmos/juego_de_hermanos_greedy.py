"""Módulo que permite procesar un archivo de entrada proporcionado como parámetro
al ejecutar el código"""
import sys

from collections import deque

def obtener_lista(archivo_txt:str) -> list:
    """
    Lee un archivo de texto que contiene valores numéricos separados por punto y coma
    (;) y los convierte en una lista de enteros.

    Parámetros:
    archivo_txt (str): Ruta del archivo de texto a leer.

    Retorna:
    list: Una lista de enteros representando las monedas extraídas del archivo.
    """
    with open(archivo_txt, 'r', encoding='utf-8') as archivo:
        next(archivo)
        monedas = archivo.read()
        monedas_str = (monedas.split(';'))
        monedas_int = [int(moneda) for moneda in monedas_str]
    return monedas_int

def juegos_de_hermanos(monedas:deque) -> 0:
    """
    Simula el juego entre Sofía y Mateo siguiendo una estrategia en la que SoPhia siempre gana.

    Parámetros:
    monedas (deque): Una cola con los valores de las monedas del juego.

    Efectos secundarios:
    Muestra por consola la secuencia a seguir para asegurar la victoria de Sophia
    y los resultados finales.
    """
    turnos = len(monedas) // 2
    ganancia_sophia = 0
    ganancia_mateo = 0
    moneda = None
    for _ in range(turnos):
        if monedas[0] >= monedas[-1]:
            moneda = monedas.popleft()
            print("Primera moneda para Sophia -> ", moneda, "\n")
            ganancia_sophia += moneda
        else:
            moneda = monedas.pop()
            print("Última moneda para Sophia -> ", moneda, "\n")
            ganancia_sophia += moneda
        if monedas[0] >= monedas[-1]:
            moneda = monedas.pop()
            print("Ultima moneda para Mateo -> ", moneda, "\n")
            ganancia_mateo += moneda
        else:
            moneda = monedas.popleft()
            print("Primera moneda para Mateo -> ", moneda, "\n")
            ganancia_mateo += moneda
    if  len(monedas) != 0:
        moneda = monedas.pop()
        print("Ultima moneda para Sophia -> ", moneda, "\n")
        ganancia_sophia += moneda
    print("Ganancia de Sophia: ", ganancia_sophia)
    print("Ganancia de Mateo: ", ganancia_mateo)
    if ganancia_sophia > ganancia_mateo:
        print("Felicidades Sophia, has ganado el juego")
    else:
        print("Parece que Mateo ha logrado hacer magia y romper el algoritmo,"
            " lo siento Sophia, no has ganado")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Para ejecutar el programa por favor usar el siguiente comando: \n"
              "python3 juego_de_hermanos_greedy.py <ruta_relativa_al_archivo>")
    else:
        archivo_ruta = sys.argv[1]
        monedas_deque = deque(obtener_lista(archivo_ruta))
        juegos_de_hermanos(monedas_deque)
