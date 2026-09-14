import numpy as np

class cola:
    __dimension:int
    __cant:int
    __cola:np.ndarray

    def __init__(self):
        self.__dimension = 3
        self.__cant = 0
        self.__cola = np.empty(self.__dimension, dtype=object)

    def vacio(self):
        return(self.__cant == 0)

    def llena(self):
        return(self.__cant == self.__dimension)

    def insertar(self, x):
        if self.llena():
            print("No hay espacio disponible")
            aux = None
        else:
            self.__cola[self.__cant] = x
            self.__cant +=1
            aux = x
        return aux

    def suprimir(self):
        if self.vacio():
            print("No hay elementos a eliminar")
            aux = None
        else:
            aux = self.__cola[0]
            for i in range(self.__cant -1):
                self.__cola[i] = self.__cola[i+1]
            self.__cant -= 1
            self.__cant = None
        return aux