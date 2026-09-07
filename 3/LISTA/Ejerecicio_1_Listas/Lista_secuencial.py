import numpy as np

class lista:
    __cantidad: int
    __dimension:int
    __lista: np.ndarray

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 5
        self.__lista = np.empty(self.__dimension, dtype=object)

    def insertar(self, otro, p):
        if p < 1 or p > self.__cantidad +1 or self.__cantidad == self.__dimension:
            print("Error")
            retorna = None
        else:
            indice_fisico = p -1
            i = self.__cantidad
            while i > indice_fisico:
                self.__lista[i] = self.__lista[i-1]
                i-=1
            self.__lista[indice_fisico] = otro
            self.__cantidad += 1
            retorna = otro
        return retorna

    def suprimir(self, p):
        if p < 1 or p > self.__cantidad+1:
            print("Error")
            retorna = None
        else:
            i = p-1
            eliminado = self.__lista[i]
            while i < self.__cantidad-1:
                self.__lista[i] = self.__lista[i+1]
                i+=1
            self.__lista[self.__cantidad-1] = None
            self.__cantidad -= 1
            return eliminado

    def recorrer(self):
        i = 0
        while i < self.__cantidad:
            print(self.__lista[i])
            i+=1

if __name__ == '__main__':
    li = lista()
    li.insertar(1,1)
    li.insertar(2,2)
    li.insertar(3,3)
    li.insertar(4,4)
    li.insertar(5,5)
    li.suprimir(5)
    li.recorrer()
