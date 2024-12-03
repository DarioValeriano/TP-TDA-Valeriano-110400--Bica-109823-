import sys

def resolver(tablero, barcos, restricciones_filas, restricciones_columnas, cantidad_espacio_ocupado, demanda_total, demanda_de_barcos, numero_barco, lista_tableros, demanda_cumplida, cant_barcos, barcos_restantes, cant_pasados):
    if encontre_una_solucion(tablero, demanda_de_barcos, demanda_total):
        return tablero
    lista_tableros.append([tablero, demanda_cumplida])

    for barco in barcos_restantes:
        if cant_barcos >= numero_barco:
            barco_colocado = False
            i = 0
            posiciones = posiciones_posibles(tablero, barco, numero_barco)
            while i < len(posiciones) and not barco_colocado:
                posicion = posiciones[i]
                if puedo_poner(tablero, barco, posicion, restricciones_filas, restricciones_columnas):
                    colocar_barco(tablero, barco, posicion, numero_barco)
                    barco_colocado = True
                    imprimir_matriz(tablero)
                    barcos_restantes = barcos_restantes[:numero_barco-1] + barcos_restantes[numero_barco:] if len(barcos_restantes) > 1 else []
                    solucion = resolver(tablero, barcos, restricciones_filas, restricciones_columnas, cantidad_espacio_ocupado, demanda_total, demanda_de_barcos, numero_barco + 1, lista_tableros, demanda_cumplida + (barco * 2), cant_barcos, barcos_restantes, cant_pasados)
                    if solucion:
                        return solucion
                    quitar_barco(tablero, barco, posicion)
                    numero_barco -= 1

                i += 1
            numero_barco += 1
        else:
            cant_pasados += 1
            barcos_restantes = barcos[cant_pasados:]
            tablero = [[0] * len(tablero[0]) for _ in range(len(tablero))]
            cantidad_espacio_ocupado = 0
            numero_barco = 2
            cant_barcos = len(barcos_restantes)
            demanda_cumplida = 0
            resolver(tablero, barcos, restricciones_filas, restricciones_columnas, cantidad_espacio_ocupado, demanda_total, demanda_de_barcos, numero_barco, lista_tableros, demanda_cumplida, cant_barcos, barcos_restantes, cant_pasados)
    
    demanda_cumplida = 0
    tablero_respuesta = tablero
    for table in lista_tableros:
        if table[1] > demanda_cumplida:
            demanda_cumplida = table[1]
            tablero_respuesta = table[0]
    
    print("Demanda cumplida: ", demanda_cumplida)
    return tablero_respuesta


def contar_espacio_ocupado(tablero):
    cant_espacio_ocupado = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] != 0:
                cant_espacio_ocupado +=2 
    return cant_espacio_ocupado


def encontre_una_solucion(tablero, demanda_de_barcos, demanda_total):
    espacio_ocupado = contar_espacio_ocupado(tablero)
    if espacio_ocupado == demanda_de_barcos or espacio_ocupado == demanda_total :
        return True
    return False

def colocar_barco(tablero, barco, posicion, numero_barco):
    for casilla in posicion:
        tablero[casilla[0]][casilla[1]] = numero_barco

def quitar_barco(tablero, barco, posicion):
    for casilla in posicion:
        tablero[casilla[0]][casilla[1]] = 0

def determinar_direccion(coordenadas):
    filas = [coord[0] for coord in coordenadas]
    columnas = [coord[1] for coord in coordenadas]
    
    if len(set(filas)) == 1:
        return "h"
    elif len(set(columnas)) == 1:
        return "v"
    else:
        return "i"


def puedo_poner(tablero, barco, posicion, restricciones_filas, restricciones_columnas):
    suma_fila_total = 0
    suma_columna_total = 0
    for casilla in posicion:
        fila = casilla[0]
        columna = casilla[1]
        suma_fila = 0 
        for i in range(len(tablero)-1):
            if tablero[fila][i] != 0:
                suma_fila += 1

        suma_columna = 0
        for i in range(len(tablero[0])-1):
            if tablero[i][columna] != 0:
                suma_columna += 1

        if suma_fila + 1 > restricciones_filas[fila]:
            return False
        
        if suma_columna + 1 > restricciones_columnas[columna]:
            return False
        
        suma_fila_total = suma_fila
        suma_columna_total = suma_columna

    if determinar_direccion(posicion) == "h":
        if suma_fila_total + barco > restricciones_filas[fila]:
            return False
    elif determinar_direccion(posicion) == "v":
        if suma_columna_total + barco > restricciones_columnas[columna]:
            return False

    return True


def posiciones_posibles(tablero, barco, numero_barco):
    n = len(tablero)
    m = len(tablero[0])
    largo_barco = barco
    posiciones = []

    for i in range(n):
        for j in range(m - largo_barco + 1):  # barcos horizontales
            if all(tablero[i][j+k] == 0 for k in range(largo_barco)):  
                if not hay_barco_adyacente(tablero, i, j, largo_barco, 'h'):
                    posiciones.append([(i, j+k) for k in range(largo_barco)])

    if(largo_barco != 1):
        for i in range(n - largo_barco + 1):
            for j in range(m):
                if all(tablero[i+k][j] == 0 for k in range(largo_barco)):  
                    if not hay_barco_adyacente(tablero, i, j, largo_barco, 'v'):
                        posiciones.append([(i+k, j) for k in range(largo_barco)])

    return posiciones

def hay_barco_adyacente(tablero, i, j, largo_barco, direccion):
    n = len(tablero)
    m = len(tablero[0])
    for k in range(largo_barco):
        if direccion == 'h':
            fila, col = i, j + k
        elif direccion == 'v':
            fila, col = i + k, j

        adyacentes = [(fila - 1, col), (fila + 1, col), (fila, col - 1), (fila, col + 1), (fila - 1, col - 1), (fila - 1, col + 1), (fila + 1, col - 1), (fila + 1, col + 1)]
        
        for f, c in adyacentes:
            if 0 <= f < n and 0 <= c < m:
                if tablero[f][c] != 0:
                    return True
    return False


def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        seccion = 0  
        demanda_filas = []
        demanda_columnas = []
        barcos = []
        next(archivo)
        next(archivo)
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                seccion += 1
                continue
            if seccion == 0:
                demanda_filas.append(int(linea))
            elif seccion == 1:
                demanda_columnas.append(int(linea))
            elif seccion == 2:
                barcos.append(int(linea))
    
    n = len(demanda_filas)
    m = len(demanda_columnas)
    return n, m, barcos, demanda_filas, demanda_columnas

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def sumar_demandas(lista_demanda):
    suma = 0
    for demanda in lista_demanda:
        suma += demanda

    return suma

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Para ejecutar el programa por favor usar el siguiente comando: \n"
              "python3 juego_de_hermanos_greedy.py <ruta_relativa_al_archivo>")
    else:
        archivo_ruta = sys.argv[1]
        n, m, barcos, demanda_filas, demanda_columnas = leer_archivo(archivo_ruta)
        print(barcos)
        matriz = [[0] * m for _ in range(n)]
        imprimir_matriz(matriz)
        cantidad_espacio_ocupado = 0
        demanda_total = sumar_demandas(demanda_columnas) + sumar_demandas(demanda_filas)
        demanda_de_barcos = sumar_demandas(barcos) * 2
        numero_barco = 1
        demanda_cumplida = 0
        lista_tableros = []
        cant_barcos= len(barcos)
        barcos_restantes = barcos
        cant_pasados = 0
        mejor_tablero = resolver(matriz, barcos, demanda_filas, demanda_columnas, cantidad_espacio_ocupado, demanda_total, demanda_de_barcos, numero_barco, lista_tableros, demanda_cumplida, cant_barcos, barcos_restantes, cant_pasados)
        if mejor_tablero is not None:
            print("Tablero")
            imprimir_matriz(mejor_tablero)
        else:
            print("No se encontró una solución válida.")