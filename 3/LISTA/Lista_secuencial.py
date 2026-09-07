import numpy as np

class Lista:
    __dimension: int
    __cantidad: int
    __items: np.ndarray

    def __init__(self, dim):
        self.__dimension = dim
        self.__cantidad = 0
        self.__items = np.empty(self.__dimension, dtype=object)

    def vacia(self):
        return (self.__cantidad == 0)

    def insertar(self, otro, p):
        if self.__dimension == self.__cantidad:
            print("No hay lugar diferente")
            return
        if p < 1 or p > self.__dimension:
            print("Error: Posición inválida para inserción")
            return False

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
        eliminado = self.__items[posicion]

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


if __name__ == '__main__':
    lista1 = Lista(10)
    lista1.recorrer()
    lista1.insertar(1,1)
    lista1.insertar(3,2)
    lista1.insertar(5,3)
    lista1.insertar(4,2)
    lista1.suprimir(2)
    lista1.recorrer()