import numpy as np

class cola:
    __dimension:int
    __cant:int
    __inicio:int
    __ultimo:int
    __cola: np.ndarray

    def __init__(self):
        self.__dimension = 3
        self.__cant = 0
        self.__inicio = 0
        self.__ultimo = 0
        self.__cola = np.empty(self.__dimension, dtype=object)

    def vacio(self):
        return (self.__cant == 0)

    def insertar(self, x):
        if self.__cant < self.__dimension:
            self.__cola[self.__ultimo] = x
            self.__ultimo = (self.__ultimo + 1) % self.__dimension
            self.__cant += 1

    def suprimir(self):
        if self.vacio():
            print("No hay elementos a eliminar")
            x = None
        else:
            x = self.__cola[self.__inicio]
            self.__cola[self.__inicio] = None
            self.__inicio=(self.__inicio + 1) % self.__dimension
            self.__cant -= 1
        return x

    def recorrer(self):
            if self.vacio():
                print("Cola vacía")
                return
            for i in range(self.__cant):
                indice_real = (self.__inicio + i) % self.__dimension
                print(self.__cola[indice_real])

if __name__=='__main__':
    cola1 = cola()
    cola1.insertar(1)
    cola1.insertar(2)
    cola1.insertar(3)
    cola1.recorrer()
    print("---------")
    cola1.suprimir()
    cola1.recorrer()