# Instrucciones de Ejecución

Este repositorio contiene tres scripts de Python que implementan diferentes juegos de lógica con enfoques variados. A continuación se explica cómo ejecutar cada uno de estos archivos.

## 1. `batalla_naval.py`

Este script resuelve un problema de colocación de barcos en un tablero de batalla naval, utilizando un enfoque recursivo. El objetivo es encontrar una disposición de barcos que cumpla con ciertas restricciones de fila, columna y demanda.

### Ejecución:
Para ejecutar este script, necesitarás un archivo de entrada con los datos del tablero, los barcos y las restricciones. El formato del archivo es el siguiente:


Puedes ejecutar el script con el siguiente comando en la terminal:

python batalla_naval.py <ruta_del_archivo_de_entrada>

Donde `<ruta_del_archivo_de_entrada>` es el camino al archivo que contiene los datos.

### Función principal:

def main(archivo):
    # Llama a la función resolver con los datos del archivo.

## 2. `juego_de_hermanos_dinamica.py`

Este script implementa el "juego de los hermanos", un problema donde se toma una lista de monedas y se decide cuál hermano (Sophia o Mateo) debe tomar la primera o la última moneda en cada turno para maximizar su ganancia. El algoritmo utiliza programación dinámica para optimizar las decisiones.

### Ejecución:
Este script requiere un archivo de texto que contenga los valores de las monedas. Cada valor debe estar separado por un punto y coma `;`.

Para ejecutar el script, utiliza el siguiente comando:

python juego_de_hermanos_dinamica.py <ruta_del_archivo_de_entrada>

Donde `<ruta_del_archivo_de_entrada>` es el camino al archivo con los valores de las monedas.

### Función principal:

def juegos_de_hermanos(monedas: list) -> 0:
    # Simula el juego de los hermanos y muestra las decisiones óptimas.


## 3. `juego_de_hermanos_greedy.py`

Este script es una implementación del "juego de los hermanos" utilizando un enfoque codicioso. A diferencia de la versión dinámica, este enfoque toma la mejor decisión local (tomar la primera o última moneda) en cada paso sin considerar el futuro.

### Ejecución:
Al igual que el script anterior, este también requiere un archivo de texto con los valores de las monedas separados por punto y coma.

Para ejecutar el script, utiliza el siguiente comando:


python juego_de_hermanos_greedy.py <ruta_del_archivo_de_entrada>


### Función principal:

def juegos_de_hermanos(monedas: list) -> 0:
    # Simula el juego de los hermanos y muestra las decisiones óptimas.


## Requisitos
- Python 3.x
- Las librerías estándar de Python.

## Notas
- Los archivos deben estar en el formato especificado para ser procesados correctamente.
- Para más detalles sobre cómo estructurar los archivos de entrada, consulta el código fuente de cada script.
