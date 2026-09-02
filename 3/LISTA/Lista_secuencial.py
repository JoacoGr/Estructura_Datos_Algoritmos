import numpy as np

class Lista:
    __dimension: int
    __cantidad: int
    __items: np.ndarray

    def __init__(self, dimension: int = 10):
        self.__dimension = dimension
        self.__cantidad = 0
        self.__items = np.empty(self.__dimension, dtype=object)

    def vacia(self):
        return (self.__cantidad == 0)

    def insertar(self, otro, p):
        if p < 1 or p > self.__cantidad + 1:
            print("Error: Posición inválida para inserción")
            return False

        if self.__cantidad == self.__dimension:
            self.__dimension += 5
            self.__items.resize(self.__dimension, refcheck=False)

        indice_fisico = p - 1

        i = self.__cantidad
        while i > indice_fisico:
            self.__items[i] = self.__items[i - 1]
            i -= 1

        self.__items[indice_fisico] = otro
        self.__cantidad += 1
        return True

    def suprimir(self, p):
        if p < 0 or p > self.__cantidad+1:
            print("Indice fuera de rango")
            return None

        posicion = p - 1
        eliminado = self.__item[posicion]

        for i in range(posicion, self.__cantidad-1):
            self.__items[i] = self.__items[i+1]

        self.__items[self.__cantidad-1] = None
        self.__cantidad -= 1
        return eliminado

    def recuperar(self, p):
        if p < 1 or p > self.__cantidad:
            print("Error: Posición fuera de rango")
            return None
        return self.__items[p - 1]

    def buscar(self, x):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__items[i] == x:
                encontrado = True
            i += 1
        
        if not encontrado:
            return -1
        
        return i+1

    def primer_elemento(self):
        if self.vacia():
            print("Error: Lista vacía")
            return None
        return self.__items[0]

    def ultimo_elemento(self):
        if self.vacia():
            print("Error: Lista vacía")
            return None
        return self.__items[self.__cantidad - 1]

    def siguiente(self, p):
        if p < 1 or p >= self.__cantidad:
            print("Error: No existe posición siguiente")
            return -1
        return p + 1 

    def anterior(self, p):
        if p <= 1 or p > self.__cantidad:
            print("Error: No existe posición anterior")
            return -1
        return p - 1

    def recorrer(self):
        for i in range(self.__cantidad):
            print(f"[{i + 1}] -> {self.__items[i]}")