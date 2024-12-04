import sys

class Nodo:
    """
    Representa un nodo en el árbol binario. Cada nodo tiene un valor, un peso,
    una suma acumulada de su valor y la posición de los elementos en la lista de monedas.
    """
    def __init__(self, padre, valor, peso, posiciones):
        """
        Inicializa un nodo con los valores proporcionados.
        
        Argumentos:
        padre (Nodo): El nodo padre.
        valor (int): El valor del nodo.
        peso (int): El peso del nodo (None si no tiene peso).
        posiciones (list): La lista que contiene las posiciones de las monedas.
        """
        self.padre = padre
        self.valor = valor
        self.peso = peso
        self.suma = valor
        self.posiciones = posiciones
        self.hijo_izq = None
        self.hijo_der = None


    def obtener_posiones(self):
        """Devuelve las posiciones del nodo."""
        return self.posiciones

    def obtener_hijo_izq(self):
        """Devuelve el hijo izquierdo del nodo."""
        return self.hijo_izq

    def obtener_hijo_der(self):
        """Devuelve el hijo derecho del nodo."""
        return self.hijo_der

    def obtener_padre(self):
        """Devuelve el nodo padre."""
        return self.padre

    def agregar_hijo_izq(self, nodo):
        """Agrega un hijo izquierdo al nodo."""
        self.hijo_izq = nodo

    def agregar_hijo_der(self, nodo):
        """Agrega un hijo derecho al nodo."""
        self.hijo_der = nodo

    def obtener_valor(self):
        """Devuelve el valor del nodo."""
        return self.valor

    def modificar_valor(self, valor):
        """Modifica el valor del nodo."""
        self.valor = valor

    def modificar_suma(self, sumando):
        """Modifica la suma acumulada del nodo (agrega el valor 'sumando')."""
        self.suma += sumando

class ArbolBinario:
    """
    Representa un árbol binario, que contiene nodos organizados de acuerdo a las decisiones
    tomadas en el juego.
    """
    def __init__(self, raiz):
        self.raiz = raiz

def agregar_nodo_izq( padre, valor, peso,posiciones):
    """
    Agrega un nodo hijo izquierdo a un nodo padre y ajusta su suma.
    
    Argumentos:
    padre (Nodo): El nodo padre al cual agregar el hijo.
    valor (int): El valor del nuevo nodo.
    peso (int): El peso del nuevo nodo.
    posiciones (list): Las posiciones del nodo en el árbol.
    
    Retorna:
    Nodo: El nodo hijo izquierdo recién agregado.
    """
    nodo_izq = Nodo(padre,valor, peso,posiciones)
    padre.agregar_hijo_izq(nodo_izq)
    nodo_izq.modificar_suma(padre.suma)
    return nodo_izq

def agregar_nodo_der( padre, valor, peso,posiciones):
    """
    Agrega un nodo hijo derecho a un nodo padre y ajusta su suma.
    
    Argumentos:
    padre (Nodo): El nodo padre al cual agregar el hijo.
    valor (int): El valor del nuevo nodo.
    peso (int): El peso del nuevo nodo.
    posiciones (list): Las posiciones del nodo en el árbol.
    
    Retorna:
    Nodo: El nodo hijo derecho recién agregado.
    """
    nodo_der = Nodo(padre,valor, peso,posiciones)
    padre.agregar_hijo_der(nodo_der)
    nodo_der.modificar_suma(padre.suma)
    return nodo_der

def agregar_nodo_der_g(padre, nodo):
    """
    Agrega un nodo hijo derecho específico al nodo padre.
    
    Argumentos:
    padre (Nodo): El nodo padre al cual agregar el hijo.
    nodo (Nodo): El nodo hijo derecho a agregar.
    
    Retorna:
    Nodo: El nodo hijo derecho.
    """
    padre.agregar_hijo_der(nodo)
    return nodo

def agregar_nodo_izq_g(padre, nodo):
    """
    Agrega un nodo hijo izquierdo específico al nodo padre.
    
    Argumentos:
    padre (Nodo): El nodo padre al cual agregar el hijo.
    nodo (Nodo): El nodo hijo izquierdo a agregar.
    
    Retorna:
    Nodo: El nodo hijo izquierdo.
    """
    padre.agregar_hijo_izq(nodo)
    return nodo

def buscar_nodo(nodo:Nodo,nodos:list) -> list:
    """
    Busca un nodo en la lista de nodos y lo reemplaza si su suma es mayor.
    
    Argumentos:
    nodo (Nodo): El nodo a buscar y reemplazar si es necesario.
    nodos (list): La lista de nodos a inspeccionar.
    
    Retorna:
    list: La lista de nodos actualizada.
    """
    largo = len(nodos)
    reemplazdo = False
    i = 0
    while not reemplazdo and i < largo:
        if nodos[i].posiciones == nodo.posiciones:
            reemplazdo = True
            if nodos[i].suma < nodo.suma:
                nodos[i] = nodo
        i += 1
    if not reemplazdo:
        nodos.append(nodo)
    return nodos

def cargar_arbol(nodo_actual:Nodo,monedas):
    """
    Carga el árbol de decisiones para el juego de los hermanos, calculando las jugadas.
    
    Argumentos:
    nodo_actual (Nodo): El nodo raíz del árbol de decisiones.
    monedas (list): La lista de monedas a considerar en el juego.
    
    Retorna:
    list: Una lista de nodos con las decisiones tomadas.
    """
    jugadas_guardadas = {}
    nodos = []
    posiciones = nodo_actual.obtener_posiones()
    primera = posiciones[0]
    ultima = posiciones[1]
    hijo_izq = None
    hijo_der = None
    while primera <= ultima:
        mateo = None
        clave = str(primera) + "," + str(ultima)
        if clave in jugadas_guardadas:
            nodos_guardados = jugadas_guardadas[clave]
            hijo_izq = agregar_nodo_izq(nodo_actual,nodos_guardados[0].valor,nodos_guardados[0].peso,nodos_guardados[0].posiciones)
            hijo_der = agregar_nodo_der(nodo_actual, nodos_guardados[1].valor,nodos_guardados[1].peso,nodos_guardados[1].posiciones)
            if hijo_izq.suma > nodos_guardados.suma:
                nodos = buscar_nodo(hijo_izq, nodos)
            if hijo_der.suma > nodos_guardados.suma:
                nodos = buscar_nodo(hijo_der, nodos)
        else:
            if primera +1 <= ultima:
                if monedas[(primera+1)] >= monedas[ultima]:
                    mateo = ["Mateo agarra la primera", monedas[(primera+1)]]
                    hijo_izq = agregar_nodo_izq(nodo_actual,monedas[primera],mateo,[primera + 2,ultima])
                    nodos = buscar_nodo(hijo_izq, nodos)
                else:
                    mateo = ["Mateo agarra la ultima", monedas[ultima]]
                    hijo_izq = agregar_nodo_izq(nodo_actual,monedas[primera],mateo,[primera + 1,ultima - 1])
                    nodos = buscar_nodo(hijo_izq, nodos)
                if monedas[primera] >= monedas[ultima - 1]:
                    mateo = ["Mateo agarra la primera", monedas[primera]]
                    hijo_der = agregar_nodo_der(nodo_actual,monedas[ultima],mateo,[primera + 1,ultima - 1])
                    nodos = buscar_nodo(hijo_der, nodos)
                else:
                    mateo = ["Mateo agarra la ultima" ,monedas[(ultima - 1)]]
                    hijo_der = agregar_nodo_der(nodo_actual,monedas[ultima],mateo,[primera ,ultima - 2])
                    nodos = buscar_nodo(hijo_der, nodos)
            else:
                hijo_izq = agregar_nodo_izq(nodo_actual,monedas[primera],mateo,[primera + 2,ultima])
                nodos = buscar_nodo(hijo_izq, nodos)
                hijo_der = agregar_nodo_der(nodo_actual,monedas[ultima],mateo,[primera ,ultima - 2])
                nodos = buscar_nodo(hijo_der, nodos)
            clave = str(primera) + "," + str(ultima)
            jugadas_guardadas[clave] = [hijo_izq,hijo_der]
        nodo_actual = nodos.pop(0)
        posiciones = nodo_actual.obtener_posiones()
        primera = posiciones[0]
        ultima = posiciones[1]
    nodos.append(nodo_actual)
    return nodos

def juegos_de_hermanos(monedas:list) -> 0:
    """
    Simula el juego de los hermanos, donde el objetivo es maximizar la suma de monedas
    obtenidas a través de decisiones óptimas de agarrar la primera o última moneda.
    
    Argumentos:
    monedas (list): Lista de valores de las monedas en orden.
    
    Retorna:
    int: El valor máximo que el hermano mayor puede obtener.
    """
    primera_moneda = 0
    ultima_moneda = len(monedas) - 1
    raiz = Nodo(None,0,None,[primera_moneda,ultima_moneda])
    arbol_binario = ArbolBinario(raiz)
    nodos = cargar_arbol(raiz,monedas)
    ganancia_sophia = 0
    sumatoria_monedas = sum(monedas)
    nodo_max = None
    jugadas = []
    for nodo in nodos:
        if nodo.suma >= ganancia_sophia:
            nodo_max = nodo
            ganancia_sophia = nodo.suma
    if nodo_max.peso is None:
        jugadas.append(["Sophia debe agarrar la ultima ->", nodo_max.valor])
        nodo_max = nodo_max.padre
    while nodo_max.padre != None:
        jugadas.append([nodo_max.peso[0] + " ->", nodo_max.peso[1]])
        if nodo_max.padre.hijo_izq == nodo_max:
            jugadas.append(["Sophia debe agarrar la primera ->", nodo_max.valor])
        else:
            jugadas.append(["Sophia debe agarrar la ultima ->", nodo_max.valor])
        nodo_max = nodo_max.padre
    for jugada in jugadas[::-1]:
        print(jugada[0],jugada[1] ,"\n")
    print("Ganancia Sophia: " ,ganancia_sophia)
    print("Ganancia Mateo: ", sumatoria_monedas - ganancia_sophia)
    if ganancia_sophia > sumatoria_monedas - ganancia_sophia:
        print("Felicidades Sophia, has ganado el juego")
    else:
        print("Parece que Mateo ha logrado hacer magia y romper el algoritmo, lo siento Sophia, no has ganado")
    return ganancia_sophia

def obtener_lista(archivo):
    """
    Lee un archivo de texto que contiene valores numéricos separados por punto y coma
    (;) y los convierte en una lista de enteros.

    Parámetros:
    archivo_txt (str): Ruta del archivo de texto a leer.

    Retorna:
    list: Una lista de enteros representando las monedas extraídas del archivo.
    """
    with open(archivo, 'r',encoding='utf-8') as archivo:
        next(archivo)
        contenido = archivo.read()
        numeros_str = contenido.split(';')
        lista_numeros = [int(numero) for numero in numeros_str]
    return lista_numeros

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Para ejecutar el programa por favor usar el siguiente comando: \n"
              "python3 juego_de_hermanos_dinamica.py <ruta_relativa_al_archivo>")
    else:
        archivo_ruta = sys.argv[1]
        monedas= (obtener_lista(archivo_ruta))
        juegos_de_hermanos(monedas)
